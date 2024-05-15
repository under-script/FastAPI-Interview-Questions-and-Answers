FastAPI deployment involves several steps. First, develop the FastAPI application locally and ensure it’s functioning as expected. Next, containerize your app using Docker for consistency across environments. Create a Dockerfile in your project directory that includes instructions to build an image of your app.

Here is a basic example:
```docker
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY ./app /app
```
Then, build the Docker image with docker build -t myimage . and run it with docker run -d --name mycontainer -p 80:80 myimage.

For production, consider deploying on a cloud platform like AWS or Google Cloud. Use their respective services (ECS/Fargate for AWS, Kubernetes Engine for GCP) to manage your containers. Ensure you have set up proper logging and monitoring for your deployed application.
