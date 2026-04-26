#!/bin/bash
# Run Interanimos Flask application

cd "$(dirname "$0")"

# Activate virtual environment
source ../.virt-env/bin/activate

# Run Flask in debug mode
flask run