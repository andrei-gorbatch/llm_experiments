' This file is used to test access the OpenAI API. '

import os
from dotenv import load_dotenv; load_dotenv()
from openai import OpenAI

def ask_open_ai(question):

    client = OpenAI()

    completion = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": question},
            {
              "type": "image_url",
              "image_url": {
                "url": "https://i.ibb.co/r2VCKKs/test.png",
              },
            },
          ],
        }
      ],
      max_tokens=300,
    )

    print(completion.choices[0])


def main():
    question = "This is an image of a break test on a vehicle. Did it pass the test? Format the answer as a Json with vehicle registration number and test result. Put NaN if the information is unknown"
    ask_open_ai(question)

if __name__ == "__main__":
    main()
