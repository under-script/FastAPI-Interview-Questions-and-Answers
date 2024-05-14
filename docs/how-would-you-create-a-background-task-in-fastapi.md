FastAPI allows the creation of background tasks using BackgroundTasks class. To create a task, first import BackgroundTasks from fastapi and define your function for the task. For instance, if you want to write logs in the background, define a function ‘write_log’. Now, include BackgroundTasks as a parameter in your path operation function. Inside this function, use the ‘add_task’ method on the BackgroundTasks object to add your log writing function as a task. This will execute the task after sending a response.

Here’s an example:

```python
from fastapi import FastAPI, BackgroundTasks

def write_log(message: str):
    with open("log.txt", "w") as file:
        file.write(message)

app = FastAPI()

@app.post("/send/{message}")
async def send_message(message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, message)
    return {"Message": "Message sent!"}
```
