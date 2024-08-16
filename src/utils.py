import openai
import json

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
