import os
from dotenv import load_dotenv
from pathlib import Path

__author__ = "Vubon Roy"

"""
This module contains all settings information for the Rest API project.

It loads environment variables from a .env file and sets up database connections.
"""

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'), encoding='utf-8')

ALLOWED_HOSTS = [host.strip() for host in os.getenv('ALLOWED_HOSTS', '').split(',')]

if not ALLOWED_HOSTS:
    raise ValueError("At least one allowed host must be specified")

DATABASE = {
    "dbname": os.getenv('DATABASE_NAME'),
    "user": os.getenv('DATABASE_USERNAME'),
    "password": os.getenv('DATABASE_PASSWORD'),
    "host": os.getenv('DATABASE_HOST'),
    "port": os.getenv('DATABASE_PORT')
}

if not all(DATABASE.values()):
    raise ValueError("Database settings are not fully configured")

try:
    DATABASE["port"] = int(DATABASE["port"])
except ValueError:
    raise ValueError("Invalid database port. It must be an integer.")

if not 0 <= DATABASE["port"] <= 65535:
    raise ValueError("Invalid database port range. It must be between 0 and 65535.")