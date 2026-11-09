# Minimal base image with Python installed
FROM python:3.11-slim

# Working directory inside the container
WORKDIR /app

# Install dependencies first so Docker can cache this layer
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the app and the model
COPY . .

EXPOSE 8501

# Run the Streamlit app on port 8501, reachable from outside the container
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
