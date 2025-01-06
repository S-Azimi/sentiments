
import requests
import json
# request to Ollama server

url= "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}
data = {
    "model": "llama3.2:latest",
    "prompt": "What is water made of?"
}
response = requests.post(url, headers=headers, data=json.dumps(data))

response_text= ""
for s in response.text.split('\n'):
    try:
        obj = json.loads(s)
        response_text= response_text + obj["response"]

    except json.JSONDecodeError as e:
        print("error!")

print(response_text)





if response.status_code == 200:
    try:
        print("\nJSON response:")
        print(response.json())
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
else:
    print("Error:", response.status_code, response.text)

