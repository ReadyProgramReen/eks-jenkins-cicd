# Use a lightweight, official Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (for build caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app code
COPY . .

# Document which port the app listens on
EXPOSE 5000

# Run the app using Gunicorn instead of Flask's dev server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]