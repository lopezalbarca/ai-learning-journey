"""
02_prompt_styles.py

Goal: Explore different prompting styles: zero-shot, few-shot, and roles.
"""

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)
MODEL = "gpt-4o-mini"

# Zero-shot
# TODO: implement a simple translation request

# Few-shot
# TODO: provide 2–3 examples before the actual input

# Roles
# TODO: set a system message (e.g., "You are a formal translator.")
# TODO: compare with/without system instructions
