import openai
import json
from datetime import datetime

with open('./secrets/openai_api_key.json') as f:
    data = json.load(f)
    openai_api_key = data['apiKey']

openai.api_key = openai_api_key

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

def get_current_weekday():
    """Helper function to get formatted current week day."""
    return int(datetime.today().strftime('%w'))

def get_current_time():
    """Helper function to get current time."""
    return str(datetime.now().time())[:-7]

def get_current_day():
    """Helper function to get current day."""
    return datetime.now().date().day
