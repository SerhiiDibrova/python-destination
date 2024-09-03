import os
from dotenv import load_dotenv
from pathlib import Path

__author__ = "Vubon Roy"

"""
All of settings information of this Rest API project will hold here
Created at: 28-07-2018
"""

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'), encoding='utf-8')

ALLOWED_HOSTS = [host.strip() for host in os.getenv('ALLOWED_HOSTS', '').split(',')]

DATABASE = {
    "dbname": os.getenv('DATABASE_NAME'),
    "user": os.getenv('DATABASE_USERNAME'),
    "password": os.getenv('DATABASE_PASSWORD'),
    "host": os.getenv('DATABASE_HOST'),
    "port": int(os.getenv('DATABASE_PORT'))
}