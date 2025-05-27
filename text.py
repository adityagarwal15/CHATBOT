import requests

API_KEY = "AIzaSyBvzm06ye4GxewbPx8sKNGZcUz3uEnwPKQ"  # Replace with your regenerated key

# Use a valid model name from the list you fetched
model_name = "models/gemini-1.5-pro"

url = f"https://generativelanguage.googleapis.com/v1/{model_name}:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {"text": "Hello, Gemini!"}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
print("Status Code:", response.status_code)
print("Response:", response.json())
