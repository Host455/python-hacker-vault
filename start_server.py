import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path

def check_python():
    """Check if Python is installed and accessible"""
    try:
        subprocess.run([sys.executable, '--version'], check=True)
        return True
    except:
        print("Error: Python is not installed or not in PATH")
        return False

def check_virtual_env():
    """Check if virtual environment exists and is activated"""
    if not hasattr(sys, 'real_prefix') and not hasattr(sys, 'base_prefix'):
        print("Virtual environment is not activated")
        return False
    return True

def install_requirements():
    """Install required packages"""
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        return True
    except:
        print("Error: Failed to install requirements")
        return False

def run_migrations():
    """Run database migrations"""
    try:
        subprocess.run([sys.executable, 'manage.py', 'migrate'], check=True)
        return True
    except:
        print("Error: Failed to run migrations")
        return False

def start_server():
    """Start the Django development server"""
    try:
        # Start the server in a new process
        server_process = subprocess.Popen([sys.executable, 'manage.py', 'runserver'])
        
        # Wait a moment for the server to start
        time.sleep(2)
        
        # Open the browser
        webbrowser.open('http://127.0.0.1:8000/')
        
        print("\nServer is running! Press Ctrl+C to stop.")
        print("You can access the application at: http://127.0.0.1:8000/")
        
        # Wait for the server process
        server_process.wait()
        
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server_process.terminate()
    except Exception as e:
        print(f"Error: {e}")
        server_process.terminate()

def main():
    print("Starting IDS System...")
    
    # Check Python installation
    if not check_python():
        return
    
    # Check virtual environment
    if not check_virtual_env():
        print("Activating virtual environment...")
        if sys.platform == 'win32':
            activate_script = Path('venv/Scripts/activate.bat')
        else:
            activate_script = Path('venv/bin/activate')
        
        if not activate_script.exists():
            print("Error: Virtual environment not found")
            return
    
    # Install requirements
    print("Checking requirements...")
    if not install_requirements():
        return
    
    # Run migrations
    print("Running database migrations...")
    if not run_migrations():
        return
    
    # Start the server
    print("Starting server...")
    start_server()

if __name__ == '__main__':
    main() 