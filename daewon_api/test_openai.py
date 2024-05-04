'''
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

print("start")

load_dotenv()
# 환경 변수에서 API 키를 가져오고, 설정되지 않았다면 오류 메시지를 출력
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key is not set. Please set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

# Example OpenAI Python library request
MODEL = "gpt-3.5-turbo"
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
    temperature=0,
)

# Properly print the JSON response
print(json.dumps(json.loads(response.model_dump_json()), indent=4))
print("end")
'''

'''
# import the OpenAI Python library for calling the OpenAI API
from openai import OpenAI
import os
import json

print("start")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
#client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "<your OpenAI API key if not set as env var>"))

# Example OpenAI Python library request
MODEL = "gpt-3.5-turbo"
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
    temperature=0,
)

print(json.dumps(json.loads(response.model_dump_json()), indent=4))
print("end")
'''


'''
from openai import OpenAI

from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key = API_KEY)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
'''

'''
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key = API_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Tell me about the GPT-4 Turbo and GPT-4 models available in OpenAI-API."},
    ]
)

print(test = response.choices[0].message.content)

'''


from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI()
#client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)


'''
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "당신은 파이썬 프로그래머입니다.",
        },
        {
            "role": "user",
            "content": "피보나치 수열을 생성하는 파이썬 프로그램을 작성해주세요.",
        },
    ],
)
print(completion.choices[0].message.content)
'''