```
ollama --version
ollama run llama3.2
ollama ps
```

import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "What is an LLM? Explain in two simple sentences.",
    "stream": False
}

response = requests.post(url, json=data, timeout=120)

response.raise_for_status()

result = response.json()

print("AI Answer:")
print(result["response"])