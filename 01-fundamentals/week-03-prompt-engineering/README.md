# W03 · Prompt Engineering & LLMs as a Service (Fundamentals)

**Goal:** Learn how to call LLMs from Python and craft effective prompts. Practice zero-shot, few-shot, roles (system/user/assistant), formatting, reliable JSON outputs, and basic error handling.

---

## Learning outcomes
- Make your first call to an LLM API (e.g., OpenAI).
- Understand **zero-shot vs. few-shot prompting**.
- Use **roles** (system, user, assistant) to guide model behavior.
- Control **formatting**: lists, tables, markdown.
- Produce **valid JSON outputs** and validate them in Python.
- Implement **basic error handling**: auth failures, rate limits, timeouts, and transient errors.
- Complete two DeepLearning.AI short courses:  
  1. *ChatGPT Prompt Engineering for Developers*  
  2. *Building Systems with the ChatGPT API*

---

## Prerequisites
- Python **3.11+**
- API key for an LLM provider (e.g., OpenAI) exported as an environment variable (`OPENAI_API_KEY`).

---

## Plan: Your Step-by-Step Guide

### 1) Prepare your Lab
**Goal:** Be ready to call an LLM API.

1. Create and activate `.venv`.
2. Install dependencies (`openai`, `httpx`, `jsonschema`).
3. Export your `OPENAI_API_KEY`.

Ref → [OpenAI Quickstart Guide](https://platform.openai.com/docs/quickstart)

---

### 2) First API Call (Hello, model!)
**Goal:** Get your first response from a model.

- Open `exercises/01_openai_basics.py` and implement your first chat completion.
- Print the model’s response.

Ref → [OpenAI Chat Completions API](https://platform.openai.com/docs/guides/chat)

---

### 3) Prompt Engineering Basics
**Goal:** See how different prompting styles change results.

- Open `exercises/02_prompt_styles.py`.
- Implement:
  - **Zero-shot**: “Translate this sentence to French.”
  - **Few-shot**: provide 2–3 examples.
  - **Roles**: define `system`, `user`, `assistant`.

Ref → [Prompt Engineering Guide (DAIR.AI)](https://www.promptingguide.ai/)

➡️ **After finishing this step, start the first sections of the course:**  
[ChatGPT Prompt Engineering for Developers (Andrew Ng & Isa Fulford, DeepLearning.AI short course)](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/?utm_source=chatgpt.com)

---

### 4) Controlling Formatting
**Goal:** Force structured outputs like tables and markdown.

- Ask: “Give me a table of 3 programming languages, with columns: Language | Paradigm | Year.”
- Verify the table is usable.

Ref → [OpenAI Cookbook — Formatting Inputs](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb)

---

### 5) Reliable JSON Outputs
**Goal:** Produce machine‑readable responses.

- Open `exercises/03_json_outputs.py`.
- Prompt: “Extract entities (name, date, location) and return JSON only.”
- Parse with `json.loads`.
- Validate with `jsonschema`.

Ref → [OpenAI JSON Mode](https://platform.openai.com/docs/guides/text-generation/json-mode)  
Ref → [jsonschema docs](https://pypi.org/project/jsonschema/)

---

### 6) Robustness (Production-Minded Basics)
**Goal:** Handle errors gracefully.

- Open `exercises/04_error_handling.py`.
- Wrap calls in `try/except`.
- Handle invalid API key, rate limits, connection errors, timeouts.
- Add exponential backoff with limited retries.

➡️ **Before continuing, complete the full course:**  
[ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/?utm_source=chatgpt.com)  
Mandatory deliverable for Week 03.

---

### 7) Building Systems with the ChatGPT API (Mandatory)
**Goal:** Learn to chain prompts, automate workflows, and build chatbots.

- Complete the course: [Building Systems with the ChatGPT API](https://www.deeplearning.ai/short-courses/building-systems-with-chatgpt/?utm_source=chatgpt.com)

Duration ~1h45min. Covers orchestration patterns, multi-step prompts, and workflow design.

---

### 8) Wrap-Up & Reflection
**Goal:** Ensure you can explain concepts clearly.

- In your own words, explain:
  - Zero-shot vs. few-shot prompting.
  - The role of the `system` message.
  - How to reliably request JSON.
  - How your error handling works (retries, timeouts).

---

## Deliverables
- `env/requirements.txt` generated and committed.
- Scripts completed: `01_openai_basics.py`, `02_prompt_styles.py`, `03_json_outputs.py`, `04_error_handling.py`.
- JSON validation passing.
- Completed DeepLearning.AI courses:
  1. *ChatGPT Prompt Engineering for Developers*  
  2. *Building Systems with the ChatGPT API*  
- Clear self-explanations of the above concepts.

---

## Folder layout (Week 03)
```
01-fundamentals/
  week-03-prompt-engineering/
    README.md
    CHECKLIST.md
    .gitignore
    env/
      setup.ps1
      setup.sh
      requirements.base.txt
      requirements.txt
    resources/
      links.md
    exercises/
      01_openai_basics.py
      02_prompt_styles.py
      03_json_outputs.py
      04_error_handling.py
```
