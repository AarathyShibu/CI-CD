Use the official Python image from the Docker Hub

FROM python:3.9-slim
Set the working directory in the container

WORKDIR /app
Copy the requirements file into the working directory

COPY requirements.txt .
Install the dependencies

RUN pip install --no-cache-dir -r requirements.txt
Copy the application code into the working directory

COPY . .
Expose the port that the application will run on

EXPOSE 5000
Command to run the application using Gunicorn
Gunicorn is used for production, while Flask's built-in server is for development

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
