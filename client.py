import requests

# Replace with your actual API key
API_KEY = "{enter your api key here}"

# API URL
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Function to send a request to Gemini API
def generate_text(prompt):
    headers = {"Content-Type": "application/json"}
    prompt_with_instruction=f"{prompt}\n\nPlease provide a brief and concise answer."
    data = {
        "contents": [{
            "parts": [{"text": prompt_with_instruction}]
        }]
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}