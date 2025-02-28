"""Has all the functionalities to gather hydration time information for the messaging fixture."""
from read_google_spreadsheet import read_google_sheet
# always pull from google sheets?

RANGE_NAME = "A:Z"

def parse_hydration_times():
    """Reads times from spreadsheet and reformats them into a list of times."""
    hydration_times = []
    values = read_google_sheet(RANGE_NAME)
    if values != None:
        times = values[1]
    else:
        return
    times = times[1:]
    for time in times:
        time = convert_to_millitary_time(time)
        hydration_times.append(time)
    return hydration_times

def convert_to_millitary_time(time):
    """Helper function to convert time to Millitary time."""
    if time[8:] == 'PM' or time[9:] == 'PM':
        match time[0:2]:
            case '10':
                time = '22' + time[2:]
                return time[:-3]
            case '11':
                time = '23' + time[2:]
                return time[:-3]
            case '12':
                time = '24' + time[2:]
                return time[:-3]
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
    return time[:-3]

