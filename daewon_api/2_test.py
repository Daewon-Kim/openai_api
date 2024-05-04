import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

# 파일 경로 설정
appl_data_path = "C:\\Users\\김대원\\캡스톤 설계\\edgar-data-pipeline\\datasets\\EXTRACTED_FILINGS\\320193_10K_2022_0000320193-22-000108.json"
msft_data_path = "C:\\Users\\김대원\\캡스톤 설계\\edgar-data-pipeline\\datasets\\EXTRACTED_FILINGS\\789019_10K_2022_0001564590-22-026876.json"
#amzn_data_path ="copy and paste the path of your EXTRACTED_FILINGS"

# prompt_list
prompt_list = [
    "in this disclosure data, summarize the main products and services in one or two lines, and if there is a new product, please explain it in one or two lines, like this format. products and service: ... \n new product:... {prompt_data}",
    "In this disclosure data, tell me about main products {prompt_data}"          
    ]

# 회사 리스트
company_AAPL = ["애플", "AAPL", "APPLE", "Apple", "apple", "appl", "320193"]
company_MSFT = ["마이크로소프트", "MSFT", "MICROSOFT", "Microsoft", "microsoft", "msft", "789019"]
company_AMZN = ["아마존", "AMZN", "AMAZON", "Amazon", "amazon",  "amzn", "1018724"]

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def gpt_api(prompt_data):
    api_key = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)
    prompt = prompt_list[1].format(prompt_data=prompt_data)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": prompt}
        ]
    )
    return completion.choices[0].message.content

# 사용자 입력 처리
while True:
    prompt_company = input("애플(APPL), 마이크로소프트(MSFT), 아마존(AMZN) 중 검색할 회사를 입력하세요. 종료를 원하면 종료를 입력하십시오: ")
    if prompt_company.strip() == "종료":
        print("프로그램을 종료합니다.")
        break    
    elif prompt_company.strip() in company_AAPL:
        data = load_data(appl_data_path)
        result = gpt_api(data['item_1A'])
        print(result)
        break
    elif prompt_company.strip() in company_MSFT:
        data = load_data(msft_data_path)
        result = gpt_api(data['item_1A'])
        print(result)
        break
    elif prompt_company.strip() in company_AMZN:
        data = load_data(msft_data_path)
        result = gpt_api(data['item_1A'])
        print(result)
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")
