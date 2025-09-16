#!/bin/bash
# Quick setup for IDS 3000

# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Install tensorflow Same for linux + windows, different on mac
pip install tensorflow


crewai install

echo "Setup complete. To run the project, activate the environment:"
echo "	source .venv/bin/activate"
echo "	crewai run"
