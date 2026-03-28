FROM python:3.10-slim

WORKDIR /app

# Step 1: Install required libraries
RUN pip install --no-cache-dir openenv-core fastapi uvicorn

# Step 2: Copy everything from your server folder
COPY . .

# Step 3: Run the app using uvicorn
# Note: app:app means "file name is app.py" and "variable name is app"
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
