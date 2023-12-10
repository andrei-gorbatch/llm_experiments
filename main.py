# Main framework for asking a question to two different models and recording the results

import os
import sys
import argparse
import random
import requests
import json
from datetime import datetime

from dotenv import load_dotenv; load_dotenv()
from string import ascii_lowercase as alc
from openai import OpenAI

from config import llm_models
from anyscale_access import ask_any_scale
from openai_access import ask_open_ai
import privateGPT  #TODO: fix impoort


def main():

    """
    Main function for asking a question to two different models and recording the results.
    """

    # Ask the user for a question
    question = input("What would you like to ask?")

    # Ask the models
    model_dict=dict()
    for model, letter in zip(random.sample(llm_models, len(llm_models)), alc):
        # Only serve two models
        if letter == "c":
            break
        
        print(f"Model {letter}")
        model_dict[letter] = model

        if model == "any_scale":
            ask_any_scale(question)
        elif model == "open_ai":
            ask_open_ai(question)
        elif model == "privateGPT":
            sys.argv = ["privateGPT.py", "--query", f'"{question}"', "-S", "-M", "-O"]
            privateGPT.main()
        else:
            print("Invalid model name. Please check config.py.")
            sys.exit()
        

    # Ask the user which model they prefer
    answer = input("Which model do you prefer? Type A or B.")

    # Record the results
    # Check which model the user chose
    if answer.lower() == "a":
        winner = "model_a"
    elif answer.lower() == "b":
       winner = "model_b"
    else:
        print("Invalid answer. Please type A or B.")
        sys.exit()
    
    # Create a json file if it doesn't exist and record the results
    json_file = "model_comparison.json"
    if not os.path.exists(json_file):
        with open(json_file, "w") as f:
            json.dump({"model_a": model_dict["a"], "model_b": model_dict["b"], "winner": winner, "time_now": datetime.timestamp(datetime.now())}, f)
            f.write("\n")
    # Append the results to the results.json file
    else:
        with open(json_file, "a") as f:
            json.dump({"model_a": model_dict["a"], "model_b": model_dict["b"], "winner": winner, "time_now": datetime.timestamp(datetime.now())}, f)
            f.write("\n")


if __name__ == "__main__":
    main()

