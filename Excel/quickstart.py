from __future__ import print_function
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class GoogleSheet:
    SPREADSHEET_ID = '1PUfehztvyH1rzkrDqHI_3gCvPPemwMNeLTLiLeGUBCo'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValues(self, range, values):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                                  body=body).execute()
        print('{0} cells updated.'.format(result.get('totalUpdatedCells')))


def main():
    gs = GoogleSheet()
    data_range = 'Bank-1S!K2:U3'
    data_values = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],

    ]
    gs.updateRangeValues(data_range, data_values)


if __name__ == '__main__':
    main()
