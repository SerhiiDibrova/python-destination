import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import logging

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    load_dotenv(find_dotenv())
except FileNotFoundError as e:
    logging.error(f"Error loading .env file: {e}")

def get_env_var(var_name):
    var_value = os.getenv(var_name)
    if not var_value:
        raise KeyError(f"Environment variable '{var_name}' is not set")
    return var_value

ALLOWED_HOSTS = [host.strip() for host in get_env_var('ALLOWED_HOSTS').split(',')]

DATABASE = {
    "dbname": get_env_var('DATABASE_NAME'),
    "user": get_env_var('DATABASE_USERNAME'),
    "password": get_env_var('DATABASE_PASSWORD'),
    "host": get_env_var('DATABASE_HOST'),
    "port": int(get_env_var('DATABASE_PORT'))  # Convert port to integer
}

# Validate DATABASE_PORT value
if not (0 <= DATABASE["port"] <= 65535):
    raise ValueError("Invalid port number for DATABASE_PORT")