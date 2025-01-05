
import requests
import json

url= "http://localhost:11434/api/generate"
headers = {'Content-Type': 'application/json'}
data = {
    "model": "llama3.2:latest",
    "prompt": "What is water made of?"
}
response = requests.post(url, headers=headers, data=json.dumps(data))


# Print the raw response content
print("Raw response content:")
print(response.text)
print("type:  ",type(response))
# for text in response:
#     print((text))
    # print("-----------------------------------------------------")
if response.status_code == 200:
    try:
        print("JSON response:")
        print(response.json())
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
else:
    print("Error:", response.status_code, response.text)


# if response.status_code == 200:
#     print(response.json())
# else:
#     print("Error:", response.status_code, response.text)