from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('ImportantFiles/token_email.pickle'):
        with open('ImportantFiles/token_email.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'ImportantFiles/credentials_email.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('ImportantFiles/token_email.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    #emails = service.users().messages().get(userId='me', id='174444e387be243f', format='minimal').execute()
    #print(emails)
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', ["INBOX"])

    if not labels:
        print('No labels found.')
    else:
        print(labels[2])
        print('Labels:')
        for label in labels:
            print(label)

if __name__ == '__main__':
    main()