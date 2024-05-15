FastAPI provides a simple way to handle file uploads using the File and UploadFile classes. To upload a file, you would define an endpoint that includes a parameter of type UploadFile. This parameter will be treated as a “form data” parameter.
Here’s a basic example:

```python
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
```
In this code, file: UploadFile = File(...) declares a new parameter of type UploadFile. The File function is a “special function” used to declare it.

The uploaded file is stored in memory up to a limit, and then passed to a temporary file stored on disk. You can access the file with .file, get metadata like filename or content type with .filename and .content_type.
