FastAPI can serve static files using the StaticFiles class from starlette.staticfiles. First, import FastAPI and StaticFiles from fastapi and starlette.staticfiles respectively. Then create an instance of FastAPI and mount a new instance of StaticFiles to it. The directory parameter in StaticFiles should point to your static files’ location. For example:

```python
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
```

In this code, “/static” is the path where your app will look for static files. “directory” is the folder with your static files.