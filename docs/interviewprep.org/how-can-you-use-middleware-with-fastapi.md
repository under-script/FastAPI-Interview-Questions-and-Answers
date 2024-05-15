FastAPI allows the use of middleware for common functionalities like authentication, CORS, etc. Middleware is a function that works with each request before it’s processed by any specific path operation and also with each response before returning it.

To add middleware in FastAPI, you can use the add_middleware() method on an instance of FastAPI(). The first argument to this method is the middleware class you want to add, followed by any keyword arguments needed for its configuration.

For example, if we wanted to add a middleware for handling CORS, we could do:

```python
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
In this code snippet, we’re adding the CORSMiddleware from Starlette (which FastAPI is built upon) and configuring it to allow all origins, methods, headers, and credentials.
