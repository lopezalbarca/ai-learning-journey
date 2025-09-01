"""
01_openai_basics.py

Goal: Make your first API call to an LLM (OpenAI).
Steps:
- Read API key from environment variable OPENAI_API_KEY.
- Create a client.
- Send a simple user message and print the model's reply.
"""

import os
from openai import OpenAI

# TODO: read API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Please set the OPENAI_API_KEY environment variable.")

# TODO: create client
client = OpenAI(api_key=api_key)

# TODO: make first call
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello in Spanish."}]
)

print(resp.choices[0].message.content)
