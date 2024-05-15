import requests

url = "https://large-text-to-speech.p.rapidapi.com/tts"

querystring = {"id": "0a18a06e-e371-4c02-8dec-41c5cfa31d77"}

headers = {
    "X-RapidAPI-Key": "1e1d2a82ffmshb6a17563e825c0ap1849f8jsne813e5cb8fbd",
    "X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
