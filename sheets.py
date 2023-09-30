from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

credentials=None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1vgIhl4taJWmI97rgZU_A-KDNNZzZXtEeL5rNHaoVJvI'

try:
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Sheet1!A1:B2').execute()
    print(result)
    request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range='Sheet2',valueInputOption='USER_ENTERED',body={'values':[['wake','down'],['wake','up']]}).execute()
    print(request)
    # values = result.get('values', [])

    # if not values:
    #     print('No data found.')

    # print('Name, Major:')
    # for row in values:
    #     # Print columns A and E, which correspond to indices 0 and 4.
    #     print('%s, %s' % (row[0], row[4]))
except HttpError as err:
    print(err)