# W03 · Checklist

### Setup
- [ ] Virtual environment created and activated.
- [ ] Dependencies installed and `env/requirements.txt` generated.
- [ ] API key set as `OPENAI_API_KEY` environment variable.

### First LLM Call
- [ ] `01_openai_basics.py` runs and prints a model response.

### Prompting Techniques
- [ ] Zero-shot example works (translation).
- [ ] Few-shot example works (with at least 2 examples).
- [ ] Role-based prompt tested (`system`, `user`, `assistant`).

### Formatting & Outputs
- [ ] Model produces a table or markdown list on request.
- [ ] `03_json_outputs.py` produces valid JSON.
- [ ] JSON schema validation passes without errors.

### Robustness (Error Handling)
- [ ] `04_error_handling.py` wraps API calls in `try/except` and surfaces friendly messages.
- [ ] Missing or invalid API key handled (authentication error).
- [ ] Rate limit (HTTP 429) handled with exponential backoff retries.
- [ ] Network/timeouts handled with retries and timeout configured.
- [ ] Non-retriable API errors reported clearly.
- [ ] Invalid JSON responses detected and reported.

### Mandatory Courses
- [ ] Completed **ChatGPT Prompt Engineering for Developers** (Andrew Ng & Isa Fulford, DeepLearning.AI Short Course).
- [ ] Completed **Building Systems with the ChatGPT API** (DeepLearning.AI Short Course).

### Consolidation
- [ ] I can explain zero-shot vs. few-shot prompting.
- [ ] I can explain the role of the `system` message.
- [ ] I can describe the retry/backoff + timeout strategy.
- [ ] I can demonstrate how to force and validate JSON outputs.
