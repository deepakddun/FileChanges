import sqlite3
from sqlite3.dbapi2 import Connection
import logging

logging.basicConfig(level=logging.DEBUG)


def create_db():
    """
    create a database and return the connection
    :return: Connection object
    """
    conn = None
    try:
        conn = sqlite3.connect("filechanges.db")
        logging.info('Database created successfully')
    except Exception as e:
        logging.error(e.with_traceback())
    return conn


create_db()