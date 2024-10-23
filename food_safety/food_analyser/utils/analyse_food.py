import os
import base64
from openai import OpenAI
from dotenv import load_dotenv

from utils import food_report_schema

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("KEY"))

def encode_image(image_path: str) -> str:
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  

def analyse_food(image: str) -> dict:

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        response_format=food_report_schema,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What do you see here?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image}"
                        }
                    }
                ]
            }
        ]
    )

    print(response)

    report = response.choices[0].message.content
    print(f"{type(report) = }")

    if type(report) == str:
       print("converting to dict")
       report = dict(report)
       
    return report