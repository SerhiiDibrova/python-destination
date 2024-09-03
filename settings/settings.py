import os
from pathlib import Path
from decouple import config, AutoConfig

# Load environment variables from .env file
AutoConfig(search_path=os.path.join(Path(__file__).resolve().parent.parent, '.env'))

BASE_DIR = Path(__file__).resolve().parent.parent

# Read environment variables
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

DATABASE = {
    "dbname": config('DATABASE_NAME'),
    "user": config('DATABASE_USERNAME'),
    "password": config('DATABASE_PASSWORD'),
    "host": config('DATABASE_HOST'),
    "port": config('DATABASE_PORT')
}

# Validate DATABASE dictionary values
for key, value in DATABASE.items():
    if not value:
        raise Exception(f"Missing or empty value for '{key}' in DATABASE settings")