# Use an official Python image as the base image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY . .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY . .

# Set environment variables
#ENV FLASK_APP=app.py
#ENV FLASK_ENV=development

# Expose the default Flask port
EXPOSE 5000

# Define the command to run the application
ENTRYPOINT ["python"]
CMD ["app.py"]
#CMD ["flask", "run", "--host=0.0.0.0"]