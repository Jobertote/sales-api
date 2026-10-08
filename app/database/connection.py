import os

import pyodbc
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    connection_string = (
        f"DRIVER={{{os.getenv('DB_DRIVER')}}};"
        f"SERVER={{{os.getenv('DB_SERVER')}}};"
        f"DATABASE={{{os.getenv('DB_DATABASE')}}};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return pyodbc.connect(connection_string)