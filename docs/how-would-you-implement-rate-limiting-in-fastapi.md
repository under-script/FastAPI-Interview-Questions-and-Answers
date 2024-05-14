Rate limiting in FastAPI can be implemented using a middleware, such as SlowApi. This is an ASGI middleware for rate limiting based on the standard Python library ratelimit. To use it, you need to install SlowApi and its dependencies, then import and add it to your FastAPI application.

Here’s a basic example:
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/home", dependencies=[Depends(limiter.limit("5/minute"))])
async def home(request: Request):
    return {"Hello": "World"}
```
In this code, we’re setting a limit of 5 requests per minute for the “/home” endpoint. The key_func parameter determines how to identify different clients, here we’re using the client’s IP address.
