from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("User not authentiated")

GMAIL = discovery.build('gmail', 'v1', http=creds.authorize(Http()))

threads = GMAIL.users().threads().list(userId='me').execute().get('threads', [])
for thread in threads:
    tdata = GMAIL.users().threads().get(userId='me', id=thread['id']).execute()
    nmsgs = len(tdata['messages'])

    if nmsgs > 2:
        msg = tdata['messages'][0]['payload']
        subject = ''
        for header in msg['headers']:
            if header['name'] == 'Subject':
                subject = header['value']
                break
        if subject:
            print('%s (%d msgs)' % (subject, nmsgs))