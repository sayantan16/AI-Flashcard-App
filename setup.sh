#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install python3."
    exit
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found. Please create a requirements.txt file with the necessary dependencies."
    exit
fi

# Install required packages
pip install -r requirements.txt

# Run the application on port 8080
python3 app.py --port 8080
