from utils import *

def build_morning_message(workout):
    file = open("goggins_transcript.txt", "r")
    goggins_transcript = file.read()
    file.close()
    prompt = f"""
    Read the following transcript delimited by triple backticks \
    and create a personality to give a motivational speech (75 \
    words max) for a workout in the excercise \
    {workout.excercise} for the distance {workout.distance}, here \
    is the transcript to build the motivational speech: 
    ```{goggins_transcript}```
    """
    response = get_completion(prompt)
    print(response)
    return response
    # return get_completion(prompt)

