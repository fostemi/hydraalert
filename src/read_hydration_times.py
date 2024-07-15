import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SPREADSHEET_ID = "1QPrWQh2f8m0EFWZF_Qf_AlE6ErnNjTGQYKNfwBxQqgE"
RANGE_NAME = "A:Z"

def read_hydration_times():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        return values
    except HttpError as err:
        print(err)

def convert_to_millitary_time(time):
    if time[8:] == 'PM' or time[9:] == 'PM':
        match time[0:1]:
            case '1':
                time = '13' + time[1:]
            case '2':
                time = '14' + time[1:]
            case '3':
                time = '15' + time[1:]
            case '4':
                time = '16' + time[1:]
            case '5':
                time = '17' + time[1:]
            case '6':
                time = '18' + time[1:]
            case '7':
                time = '19' + time[1:]
            case '8':
                time = '20' + time[1:]
            case '9':
                time = '21' + time[1:]
        match time[0:2]:
            case '10':
                time = '22' + time[:2]
            case '11':
                time = '23' + time[:2]
            case '12':
                time = '24' + time[:2]
    return time[:-3]

def get_hydration_times():
    hydration_times = []
    values = read_hydration_times()
    times = values[1]
    times = times[1:]
    for time in times:
        time = convert_to_millitary_time(time)
        hydration_times += time
    return hydration_times
    
get_hydration_times()
