"""
04_error_handling.py

Goal: Add robustness to your client with try/except, timeouts, and retries.
"""

import os, time
from openai import OpenAI
from openai import APIConnectionError, APIError, AuthenticationError, RateLimitError

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key, timeout=20)
MODEL = "gpt-4o-mini"

def call_llm(prompt: str, retries: int = 3) -> str:
    for attempt in range(1, retries + 1):
        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}]
            )
            return resp.choices[0].message.content

        except AuthenticationError as e:
            raise RuntimeError("❌ Invalid API key.") from e
        except RateLimitError:
            if attempt == retries:
                raise
            wait = 2 ** attempt
            print(f"⚠️ Rate limit hit. Retrying in {wait}s...")
            time.sleep(wait)
        except APIConnectionError:
            if attempt == retries:
                raise
            wait = 2 ** attempt
            print(f"⚠️ Connection error. Retrying in {wait}s...")
            time.sleep(wait)
        except APIError as e:
            if getattr(e, "status", 500) >= 500 and attempt < retries:
                wait = 2 ** attempt
                print(f"⚠️ Server error {e.status}. Retrying in {wait}s...")
                time.sleep(wait)
                continue
            raise RuntimeError(f"❌ OpenAI API error: {e}") from e

if __name__ == "__main__":
    answer = call_llm("Say hello in French.")
    print(answer)
