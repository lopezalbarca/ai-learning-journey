"""
03_json_outputs.py

Goal: Request structured JSON output and validate it.
"""

import os, json
from openai import OpenAI
from jsonschema import validate

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)
MODEL = "gpt-4o-mini"

prompt = "Extract name, date, and location from: 'John met Anna in Paris on 2023-05-10.' Return JSON only."

# TODO: make request using JSON mode if supported
resp = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": prompt}]
)

output = resp.choices[0].message.content
print("Raw output:", output)

# TODO: parse JSON
data = json.loads(output)

# TODO: validate with schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "date": {"type": "string"},
        "location": {"type": "string"}
    },
    "required": ["name", "date", "location"]
}

validate(instance=data, schema=schema)
print("✅ JSON is valid:", data)
