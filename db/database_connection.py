from psycopg2 import connect
from psycopg2.extras import DictCursor

from settings.settings import DATABASE

"""
This module establishes a connection to an existing database.

It uses the psycopg2 library to create a connection object and a cursor object.
The connection is established using the parameters defined in the DATABASE dictionary.

Author: Vubon Roy
"""

with connect(**DATABASE, cursor_factory=DictCursor) as db_connection:
    with db_connection.cursor() as db:
        pass