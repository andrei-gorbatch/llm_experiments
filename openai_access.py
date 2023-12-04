' This file is used to test access the OpenAI API. '

import os
from dotenv import load_dotenv; load_dotenv()
from openai import OpenAI

def ask_open_ai(question):

    client = OpenAI()

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
      ]
    )

    print(completion.choices[0].message)


def main():
    question = "Say 'Test'."
    ask_open_ai(question)

if __name__ == "__main__":
    main()
