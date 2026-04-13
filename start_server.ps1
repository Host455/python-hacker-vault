# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Green
.\venv\Scripts\Activate.ps1

# Install requirements
Write-Host "Installing requirements..." -ForegroundColor Green
pip install -r requirements.txt

# Run migrations
Write-Host "Running database migrations..." -ForegroundColor Green
python manage.py migrate

# Start the server
Write-Host "Starting Django server..." -ForegroundColor Green
python manage.py runserver 