from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)