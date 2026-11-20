## Mini Project: GenAI Prompt Reader & Response Writer

- Read a prompt from a text file, 
- send it to an AI API, receive the response, and save the response into another text file.

```
GenAI-Mini-Project/
│
├── prompt.txt
├── main.py
└── output.txt
```

## Step 1 – Write the prompt - ***prompt.txt***
```
    Explain what is Python.

    I am a beginner.
    Use simple English.
    Give me one real-world example.
```

###  Step 2 – Read the prompt using Python - ***main.py***
```
# Open the file
file = open("prompt.txt", "r")

# Read the content
prompt = file.read()

# Close the file
file.close()

# Print the prompt
print(prompt)
```

### Step 3 – Connect to GenAI API

```
    pip install requests
```

### Step 4 Send prompt to Ollama
```
import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=data )

result = response.json()

print(result["response"])
```

### Save AI response to output.txt
```
# Save AI response

file = open("output.txt", "w")

file.write(result)

file.close()

print("Response saved successfully!")
```
### 8. Complete main.py program
```

import requests

# Step 1: Read prompt from file

file = open("prompt.txt", "r")
prompt = file.read()
file.close()

print("Input Prompt:")
print(prompt)


# Step 2: Ollama API URL

url = "http://localhost:11434/api/generate"


# Step 3: Prepare request data

data = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False
}


# Step 4: Send request to Ollama

response = requests.post(url, json=data)

# Step 5: Get AI response

result = response.json()["response"]

print("\nAI Generated Response:")
print(result)


# Step 6: Save response to file

file = open("output.txt", "w")
file.write(result)
file.close()

print("\nResponse saved successfully!")

```