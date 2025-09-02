# Use Python 3.13.5 (Or whatever version you are running)
FROM python:3.13.5

# To prevent .pyc generation and unbuffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install the OS dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY requirements.txt /app/
COPY pyproject.toml /app/
COPY src/ /app/src/
COPY eve.json /app/
COPY .env* /app/
COPY setup-linux.sh setup-mac.sh setup.bat /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Optional but install CrewAI CLI if needed
RUN pip install crewai

# Default command
CMD ["crewai", "run"]
