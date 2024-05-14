FastAPI’s dependency injection system is highly efficient for managing dependencies and reducing code repetition. However, there are cases where using HTTP protocol directly might be preferred. One such case could be when dealing with low-level network operations or custom protocols.

For instance, if we need to implement a WebSocket server that communicates via a specific binary protocol, FastAPI’s dependency injection may not provide the necessary control over the raw data stream. In this scenario, it would be more appropriate to use an ASGI server like Uvicorn or Hypercorn directly along with Python’s built-in asyncio library for handling asynchronous I/O operations.

Here’s a simplified example of how you might set up a WebSocket server using Uvicorn:
```python
import uvicorn
from starlette.websockets import WebSocket

async def app(scope, receive, send):
    websocket = WebSocket(scope, receive, send)
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Process data here...
        await websocket.send_text(f"Processed: {data}")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```
In this example, we have direct access to the incoming data stream and can process it as needed without any abstraction layers introduced by FastAPI’s dependency injection system.
