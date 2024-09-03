import os
from dotenv import load_dotenv
from enum import Enum
from typing import Dict, List

class DatabaseKeys(Enum):
    DBNAME = "dbname"
    USER = "user"
    PASSWORD = "password"
    HOST = "host"
    PORT = "port"

__author__ = "Vubon Roy"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_environment_variable(var_name: str) -> str:
    return os.environ.get(var_name)

ALLOWED_HOSTS: List[str] = get_environment_variable('ALLOWED_HOSTS').split(',')

DATABASE: Dict[DatabaseKeys, str] = {
    DatabaseKeys.DBNAME: get_environment_variable('DATABASE_NAME'),
    DatabaseKeys.USER: get_environment_variable('DATABASE_USERNAME'),
    DatabaseKeys.PASSWORD: get_environment_variable('DATABASE_PASSWORD'),
    DatabaseKeys.HOST: get_environment_variable('DATABASE_HOST'),
    DatabaseKeys.PORT: get_environment_variable('DATABASE_PORT')
}

required_variables = ['ALLOWED_HOSTS', 'DATABASE_NAME', 'DATABASE_USERNAME', 'DATABASE_PASSWORD', 'DATABASE_HOST', 'DATABASE_PORT']
for var in required_variables:
    if not os.environ.get(var):
        raise ValueError(f"Missing environment variable: {var}")