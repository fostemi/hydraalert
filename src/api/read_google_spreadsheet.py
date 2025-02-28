"""
Extracted function to read the single spreadsheet for multiple page reading. Should need to authenticate once when running the function and then call the function wherever you have a new sheet within the same spreadsheet to read.
"""
import os.path
import introcs

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SPREADSHEET_URL = (
    "https://docs.google.com/spreadsheets/d/1QPrWQh2f8m0EFWZF_Qf_AlE6ErnNjTGQYKNfwBxQqgE/"
)

# TODO: Make any spreadsheet readable

def read_google_sheet(range):
    """Function from google to read cells in a google spreadsheet."""
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
        with open("token.json", "w", encoding='UTF-8') as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=parse_spreadsheet_id(SPREADSHEET_URL), range=range)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        return values
    except HttpError as err:
        print(err)

def parse_spreadsheet_id(url):
    """Helper function to parse spreadsheet url into the Spreadsheet id."""
    id_start = introcs.find_str(url, '/d/', 0) + 3
    id_end = introcs.find_str(url, '/', id_start)
    return url[id_start:id_end]
