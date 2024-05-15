FastAPI supports asynchronous request handling through Python’s async and await keywords. This allows for concurrent processing of requests, improving application performance. When a FastAPI route is defined with an async function, it becomes a coroutine that can be paused and resumed, allowing other tasks to run in the meantime.

For instance:

```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
```
In this example, read_root is an asynchronous function. If it calls another async function with await, execution returns to the event loop, freeing up resources until the awaited function completes.

This non-blocking nature of async I/O operations means your app can handle more requests with fewer resources, as idle time waiting for I/O (like network or disk access) can be used to serve other requests. It also simplifies code by avoiding callback hell or threading complexities, making it easier to write and maintain.
