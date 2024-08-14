# Need to read another spreadsheet with a specified format
# Get the workout for that day
# send message of the workout
    # While loop loops until trigger at the wake up time for the day
from read_google_spreadsheet import read_google_sheet

# TODO: User inputs
WAKE_UP = '5:59:00 AM'
WORKOUT_RANGE = "Sheet2!A:Z"

class WorkoutProgram:
    def __init__(self, title=""):
        self.title = title
        self.workouts = []
    def add_workout(self, workout):
        self.workouts.append(workout)
    def get_workout_by_day(self, week, day):
        for workout in self.workouts:
            if week == workout.week and day == workout.day:
                return workout

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
    week_num = -1
    for row in values:
        if 'Swim' in row:
            week_num = int(row[0])
            parse_swim_row(wp, row, week_num)
        elif 'Bike' in row:
            parse_bike_row(wp, row, week_num)
        elif 'Run' in row:
            parse_run_row(wp, row, week_num)
        else:
            raise Exception("Incorrect formatting of row. Please include workouts")
    return wp


def parse_workout_sheet_title(values):
    return values[0][0]

def parse_swim_row(workout_program, week_workouts, week_num):
    swims = week_workouts[2:]
    day = 0
    for swim in swims:
        day += 1
        if swim == 'Rest':
            # TODO: handle rest day
            pass
        elif swim != '':
            workout = Workout(day, week_num, 'Swim', swim)
            workout_program.add_workout(workout)

def parse_bike_row(workout_program, week_workouts, week_num):
    bikes = week_workouts[2:]
    day = 0
    for bike in bikes:
        day += 1
        if bike == 'Rest':
            pass
        elif bike != '':
            workout = Workout(day, week_num, 'Bike', bike)
            workout_program.add_workout(workout)

def parse_run_row(workout_program, week_workouts, week_num):
    runs = week_workouts[2:]
    day = 0
    for run in runs:
        day += 1
        if run == 'Rest':
            pass
        elif run != '':
            workout = Workout(day, week_num, 'Run', run)
            workout_program.add_workout(workout)
