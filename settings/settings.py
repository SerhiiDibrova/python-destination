import os
from pathlib import Path
from typing import Dict, List
from dotenv import load_dotenv

"""
All of settings information of this Rest API project will hold here
Created at: 28-07-2018
"""

__author__ = "Vubon Roy"

BASE_DIR: str = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

ALLOWED_HOSTS: List[str] = os.getenv('ALLOWED_HOSTS').split(',')

DATABASE: Dict[str, str] = {
    "dbname": os.getenv('DATABASE_NAME'),
    "user": os.getenv('DATABASE_USERNAME'),
    "password": os.getenv('DATABASE_PASSWORD'),
    "host": os.getenv('DATABASE_HOST'),
    "port": os.getenv('DATABASE_PORT')
}