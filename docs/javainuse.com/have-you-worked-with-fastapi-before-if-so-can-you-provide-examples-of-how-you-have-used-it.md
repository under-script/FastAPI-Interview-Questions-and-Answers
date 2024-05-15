FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ based on type hints. It provides a straightforward way to define API endpoints using Python's asynchronous capabilities, making it highly efficient and scalable.
Here's an example to showcase how FastAPI can be used:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```
In this example, we import the `FastAPI` class from the FastAPI library and create an instance called `app`. We then define two routes, represented by the `@app.get` decorator. The first route handles the root URL ("/") and returns a simple message as a JSON response. The second route handles the endpoint "/items/{item_id}" and takes two parameters: `item_id` as a required integer and `q` as an optional query parameter of type string.

By running this FastAPI application, you can access the root URL and the "/items/{item_id}" endpoint. The "{item_id}" part of the URL will be dynamically replaced by the corresponding value provided. For example, if you make a GET request to "/items/42?q=test", the response will be `{"item_id": 42, "q": "test"}`.

FastAPI provides many more features, such as automatic generation of interactive API documentation, validation of request/response models based on type hints, dependency injection, and more. It also has excellent performance due to leveraging async and type hinting capabilities.

Remember that this is just a simple example, and FastAPI is capable of much more. You can explore the official FastAPI documentation and additional examples to get a deeper understanding of its features and how to use them in your own projects.
