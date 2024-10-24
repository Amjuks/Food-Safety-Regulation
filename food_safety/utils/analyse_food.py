import os
import base64
import json

from openai import OpenAI
from dotenv import load_dotenv

from utils.food_schema import food_report_schema

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("KEY"))

def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
  
def encode_memory_image(image) -> str:
    file_content = image.read()
    encoded_string = base64.b64encode(file_content).decode('utf-8')
    content_type = image.content_type
    data_url = f"data:{content_type};base64,{encoded_string}"

    return data_url

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
                        "text": "Give a safety report on the food you see."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"{image}"
                        }
                    }
                ]
            }
        ]
    )

    print(f"{response = }")

    report = json.loads(response.choices[0].message.content)

    return report