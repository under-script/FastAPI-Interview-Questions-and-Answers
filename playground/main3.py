import requests

url = "https://large-text-to-speech.p.rapidapi.com/tts"

payload = {
    "text": """Explore our comprehensive article on FastAPI interview questions and answers. It's designed to help you prepare effectively for your upcoming interview, providing insights into the framework's most pertinent aspects.

FastAPI, a modern and fast-growing web framework for building APIs with Python 3.6+ based on standard Python type hints, has been rapidly gaining ground in the world of programming. Known for its high speed, FastAPI is touted to be one of the quickest Python frameworks available, only outpaced by NodeJS and Go.

What sets FastAPI apart from other frameworks is its intuitive nature. It’s designed to be easy-to-use while still maintaining high performance levels. Moreover, it provides automatic interactive API documentation, which can significantly streamline the development process.

In this article, we delve into an extensive list of interview questions centered around FastAPI. These questions 
encompass fundamental concepts as well as more intricate aspects of this powerful framework. Whether you’re a 
beginner looking to get your feet wet or an experienced developer wanting to brush up your knowledge, these questions 
will provide valuable insights into the workings of FastAPI."""}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "1e1d2a82ffmshb6a17563e825c0ap1849f8jsne813e5cb8fbd",
    "X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
