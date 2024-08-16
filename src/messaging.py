"""Twilio messaging env setting and sending messages given the times."""
from read_hydration_times import parse_hydration_times
from read_workouts import build_workout_program
from handle_messaging import handle_workout_messaging, handle_hydration_messaging
from utils import get_current_time, get_current_day

# TODO: User input
WAKE_UP = '06:00:00'
HYDRATION_ENABLED = False

def schedule_texts():
    """Forever loop triggers messages when time equals message time."""
    message_times = parse_hydration_times()
    workout_program = build_workout_program()
    day = get_current_day()
    wakeup_times_users = {WAKE_UP: [workout_program]}
    while True:
        if get_current_time() in message_times and HYDRATION_ENABLED:
            handle_hydration_messaging()
        if get_current_time() in wakeup_times_users:
            for wp in wakeup_times_users[get_current_time()]:
                handle_workout_messaging(wp)
        if get_current_day() != day:
            message_times = parse_hydration_times()
            day = get_current_day()

