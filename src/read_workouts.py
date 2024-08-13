# Need to read another spreadsheet with a specified format
# Get the workout for that day
# send message of the workout
    # While loop loops until trigger at the wake up time for the day
# Hard code wake up time for now
from read_google_spreadsheet import read_google_sheet

WAKE_UP = '6:00:00 AM'
WORKOUT_RANGE = "Sheet2!A:Z"

class WorkoutProgram:
    def __init__(self):
        self.title = ""
        self.workouts = []
    def add_workout(workout):
        workouts += workout

class Workout:
    def __init__(self, day, week, excercise, distance):
        self.day = day
        self.week = week
        self.excercise = excercise
        self.distance = distance

def parse_workout_sheet_title(values):
    return values[0][0]

def build_workout_program():
    wp = WorkoutProgram
    values = read_google_sheet(WORKOUT_RANGE)
    wp.title = parse_workout_sheet_title(values)

# We are reading the same spreadsheet so we just have to refactor the existing code to extract the read_sheet() function to it's own file
