FastAPI has a built-in middleware for managing CORS, which can be added to the application instance. To enable it, import CORSMiddleware from fastapi.middleware.cors and add it to your FastAPI app using the .add_middleware() method. You need to specify parameters like allow_origins (a list of origins that are allowed), allow_credentials (whether cookies can be supported), allow_methods (HTTP methods allowed), and allow_headers (which HTTP headers are permitted). Here’s an example:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}
```
