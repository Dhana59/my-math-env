FROM python:3.10-slim

WORKDIR /app

# Install basic dependencies
RUN pip install --no-cache-dir openenv-core fastapi uvicorn

# Copy all files from the current directory to /app
COPY . .

# Expose the port OpenEnv uses
EXPOSE 7860

# Start the server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
