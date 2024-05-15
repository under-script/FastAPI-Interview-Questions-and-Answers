To deploy a FastAPI application in a production environment, you will typically follow a set of steps that involve setting up a web server, configuring the application, and integrating it with any necessary tools or services. Here is an example of how you could deploy a FastAPI application using Gunicorn as the web server and NGINX as a reverse proxy.

1. Install the necessary dependencies:
```
$ pip install fastapi uvicorn gunicorn
```
2. Create a FastAPI application in a file `main.py`:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```
3. Test the application locally using Uvicorn:
```
$ uvicorn main:app --reload
```
4. Configure Gunicorn to serve the FastAPI application:
Create a file `wsgi.py` with the following content:
```python
from main import app

if __name__ == "__main__":
    app.run()
```
5. Start Gunicorn to run the application:
```
$ gunicorn -w 4 -k uvicorn.workers.UvicornWorker wsgi:app
```
6. Install and configure NGINX as a reverse proxy:
```
$ sudo apt-get install nginx
```
Create an NGINX server block file in `/etc/nginx/sites-available/my_app`:
```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
Enable the server block:
```
$ sudo ln -s /etc/nginx/sites-available/my_app /etc/nginx/sites-enabled/
$ sudo service nginx restart
```
Now, your FastAPI application is deployed in a production environment using Gunicorn as a web server and NGINX as a reverse proxy. Accessing the domain associated with your server will route requests to the FastAPI application.
Remember, the actual deployment process may vary depending on your specific infrastructure, so adjust these steps accordingly. It's important to tailor the deployment to your production environment's requirements and configurations.
