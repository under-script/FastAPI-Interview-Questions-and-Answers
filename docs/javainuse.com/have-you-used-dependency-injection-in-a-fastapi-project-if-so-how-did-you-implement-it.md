Yes, I have experience using dependency injection in a FastAPI project. In FastAPI, dependency injection can be implemented using the Dependency Injection Container (DI Container) provided by the `fastapi` module. This container simplifies the management and injection of dependencies throughout your application.

To demonstrate how it can be implemented, let's consider a simple FastAPI project with two modules: `main.py` and `services.py`. In `services.py`, we define a basic service that we want to inject into our FastAPI routes.
```python
# services.py
class MyService:
    def get_data(self):
        return "Some data from MyService"
```
Next, in `main.py`, we can create an instance of the DI Container and register our service within it. We can then define a FastAPI route that uses this injected service.
```python
# main.py
from fastapi import Depends, FastAPI

from services import MyService

app = FastAPI()
container = {}

def get_my_service() -> MyService:
    # retrieve the MyService instance from the DI container
    return container.get(MyService.__name__)

@app.get("/")
def read_root(my_service: MyService = Depends(get_my_service)):
    # use the injected MyService instance
    data = my_service.get_data()
    return {"message": data}

if __name__ == "__main__":
    # Register the MyService instance in the DI container
    container[MyService.__name__] = MyService()

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
Here, we define a `get_my_service` function that relies on the DI container to retrieve the instance of `MyService`. We specify the `my_service` parameter in our route function with the `Depends` class, which signals that it should be injected using the provided dependency injection mechanism.

Before running the FastAPI application, we register an instance of `MyService` in the DI container so that it can be resolved and injected when needed.
With this implementation, the `MyService` instance is injected into the `read_root` route, allowing us to call its `get_data` method and return the result as a response.
Remember that this is just a basic example to illustrate the concept of dependency injection in FastAPI. In more complex applications, you may want to consider using libraries such as `pydantic` or `Inject` for more advanced dependency management.
