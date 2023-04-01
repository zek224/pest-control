#!/bin/bash

# Run the Virtual Environment
python3 -m venv venv

# Activate the Virtual Environment
source venv/bin/activate
. venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload

# Deactivate the Virtual Environment
deactivate
