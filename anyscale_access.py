# Quick test of anyscale connection

import os
import requests
from dotenv import load_dotenv; load_dotenv()

s = requests.Session()

api_base = os.environ["ANYSCALE_API_BASE"]
token = os.environ["ANYSCALE_API_KEY"]
url = f"{api_base}/chat/completions"
body = {
  "model": "meta-llama/Llama-2-70b-chat-hf",
  "messages": [{"role": "system", "content": "You are a helpful assistant."}, 
               {"role": "user", "content": "Say 'Test'."}],
  "temperature": 0.7
}

with s.post(url, headers={"Authorization": f"Bearer {token}"}, json=body) as resp:
    print(resp.json())


