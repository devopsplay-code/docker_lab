# Use a small Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port the app will run on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
