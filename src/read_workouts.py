# Need to read another spreadsheet with a specified format
# Get the workout for that day
# send message of the workout
    # While loop loops until trigger at the wake up time for the day
from read_google_spreadsheet import read_google_sheet

# TODO: User inputs
WORKOUT_RANGE = "Sheet2!A:Z"

class WorkoutProgram:
    def __init__(self, title=""):
        self.title = title
        self.workouts = []
    def add_workout(self, workout):
        self.workouts.append(workout)
    def add_workout_in_pos(self, pos, workout):
        self.workouts.insert(pos, workout)
    def get_workout_by_day(self, week, day):
        for workout in self.workouts:
            if workout != None:
                if week == workout.week and day == workout.day:
                    return workout
        return None
    def remove_workout(self, workout):
        for i in range(len(self.workouts)):
            if self.workouts[i] == None:
                pass
            elif workout.day == self.workouts[i].day and workout.week == self.workouts[i].week and workout.excercise == self.workouts[i].excercise:
                self.workouts.pop(i)
                return i

class Workout:
    def __init__(self, day=0, week=0, excercise="", distance=""):
        self.day = day
        self.week = week
        self.excercise = excercise + " " + distance
    def add_workout(self, excercise, distance):
        self.excercise = self.excercise + " and " +excercise + " " + distance
        

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
    """ Monday is considered day 1. """
    bikes = week_workouts[2:]
    day = 0
    for bike in bikes:
        day += 1
        if bike == 'Rest':
            pass
        elif bike != '':
            prev_workout = workout_program.get_workout_by_day(week_num, day)
            if prev_workout != None:
                pos = workout_program.remove_workout(prev_workout)
                workout = prev_workout.add_workout('Bike', bike)
                workout_program.add_workout_in_pos(pos, prev_workout)
            else:
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
            prev_workout = workout_program.get_workout_by_day(week_num, day)
            if prev_workout != None:
                pos = workout_program.remove_workout(prev_workout)
                workout = prev_workout.add_workout('Run', run)
                workout_program.add_workout_in_pos(pos, prev_workout)
            else:
                workout = Workout(day, week_num, 'Run', run)
                workout_program.add_workout(workout)
