# Step 1: Use the official Python image from Docker Hub
FROM python:3.12.3-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the local requirements.txt to the container
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire project to the container
COPY . .

EXPOSE 5000

# Step 6: Command to run your Python app (e.g., app.py)
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000"]
