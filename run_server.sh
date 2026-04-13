#!/bin/bash
echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing/Updating requirements..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate

echo "Starting server..."
python manage.py runserver 