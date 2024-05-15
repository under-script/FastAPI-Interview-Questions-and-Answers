FastAPI provides built-in exception handling. To handle exceptions, use the HTTPException class from fastapi.exceptions module. This class accepts status_code and detail parameters to define HTTP status code and error message respectively.

For custom error responses, create a subclass of HTTPException and override its attributes. You can also customize the validation error response body by creating a route operation function that raises RequestValidationError from fastapi.exceptions and catch it in an exception handler.

Here’s a coding example:
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oops! {exc.detail}"},
    )

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
```
