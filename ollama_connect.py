
import requests
import json
# request to Ollama server

# url= "http://localhost:11434/api/generate"
url= "http://192.168.0.192:11434/api/generate"
headers = {'Content-Type': 'application/json'}
data = {
    "model": "llama3.2:latest",
    "prompt": "What is mellat bank?"
}


response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    try:
        response_text= ""
        for s in response.text.split('\n'):
            try:
                obj = json.loads(s)
                response_text= response_text + obj["response"]
            except json.JSONDecodeError as e:
                print(e)
        print("\n",response_text)

    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
else: print(response.status_code)


