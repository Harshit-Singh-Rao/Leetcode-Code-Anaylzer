import sys
import os

# Add the 'backend' folder to the Python path so 'app.x' imports work
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from app.main import app
