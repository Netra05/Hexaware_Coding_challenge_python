# util/db_conn_util.py

import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={your driver name};"
            "SERVER=your server name;"
            "DATABASE=your database name;"
            "Trusted_Connection=yes;"
        )
        print("Database connection established successfully.")
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None
