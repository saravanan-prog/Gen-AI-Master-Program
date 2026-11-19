
3. Create the project folder

```
genai_file_project/
│
├── input/
│   └── prompt.txt
│
├── output/
│   └── response.txt
│
├── main.py
│
└── requirements.txt
```
### Install Ollama and download model

```
ollama pull llama3.2
```
Start the model:

```
ollama run llama3.2
```
### Step 2: Install Python dependencies
```
requests
pip install -r requirements.txt

```
### Step 3: Create the input prompt
Open input/prompt.txt.
```
You are a customer support assistant.

Analyze the following customer complaint.

Customer complaint:
I purchased a laptop five days ago.
The laptop is not switching on.

Please provide:
1. Complaint summary
2. Possible reason
3. Suggested solution
4. Customer support response

Use simple English.
```
### Step 4: Write the Python application
Open ***main.py***
```

import requests
from pathlib import Path

# File locations
INPUT_FILE = Path("input/prompt.txt")
OUTPUT_FILE = Path("output/response.txt")

# Ollama API details
API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"


def read_prompt():

    print("Reading prompt from file...")

    if not INPUT_FILE.exists():
        raise FileNotFoundError("Prompt file not found!")

    prompt = INPUT_FILE.read_text(encoding="utf-8")

    if not prompt.strip():
        raise ValueError("Prompt file is empty!")

    return prompt


def call_genai_api(prompt):

    print("Sending prompt to Ollama...")

    data = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        API_URL,
        json=data,
        timeout=180
    )

    response.raise_for_status()

    result = response.json()

    return result["response"]


def save_response(ai_response):

    print("Saving AI response...")

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        ai_response,
        encoding="utf-8"
    )


def main():

    try:
        prompt = read_prompt()

        ai_response = call_genai_api(prompt)

        save_response(ai_response)

        print("Project completed successfully!")
        print("Check output/response.txt")

    except requests.exceptions.RequestException as error:
        print("API connection error:", error)

    except Exception as error:
        print("Application error:", error)


if __name__ == "__main__":
    main()

```