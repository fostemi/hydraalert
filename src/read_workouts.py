# Need to read another spreadsheet with a specified format
# Get the workout for that day
# send message of the workout
    # While loop loops until trigger at the wake up time for the day
# Hard code wake up time for now
from read_google_spreadsheet import read_google_sheet

WAKE_UP = '6:00:00 AM'
WORKOUT_RANGE = "Sheet2!A:Z"

class WorkoutProgram:
    def __init__(self, title=""):
        self.title = title
        self.workouts = []
    def add_workout(workout):
        workouts += workout

class Workout:
    def __init__(self, day=0, week=0, excercise="", distance=""):
        self.day = day
        self.week = week
        self.excercise = excercise
        self.distance = distance

def build_workout_program():
    values = read_google_sheet(WORKOUT_RANGE)
    wp = WorkoutProgram(title=parse_workout_sheet_title(values))
    values = values[2:][:]
    for row in values:
        if 'Swim' in row:
            week_num = int(row[0])
            parse_swim_row(row, week_num)
            # print(week_num)
            # print(row)
        # elif 'Bike' in row:
            # handle bike row
        # elif 'Run' in row:
            # handle run row
        # else:
            # handle error
    print(wp.title)
    return wp


def parse_workout_sheet_title(values):
    return values[0][0]

def parse_swim_row(week_workouts, week_num):
    swims = week_workouts[2:]
    workouts = []
    day = 0
    for swim in swims:
        day += 1
        if swim == 'Rest':
            # TODO
            # handles rest day
            print("rest day")
        elif swim != '':
            workout = Workout(day, week_num, 'Swim', swim)
            workouts.append(workout)
    return workouts

