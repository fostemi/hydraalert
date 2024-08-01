# Need to read another spreadsheet with a specified format
# Get the workout for that day
# send message of the workout
    # While loop loops until trigger at the wake up time for the day
# Hard code wake up time for now
from read_google_spreadsheet import read_google_sheet

WAKE_UP = '6:00:00 AM'
WORKOUT_RANGE = "Sheet2!A:Z"

def parse_workout_sheet_title():
    values = read_google_sheet(WORKOUT_RANGE)
    return values[0]
    


# We are reading the same spreadsheet so we just have to refactor the existing code to extract the read_sheet() function to it's own file
