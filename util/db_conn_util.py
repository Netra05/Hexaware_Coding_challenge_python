# util/db_conn_util.py

import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=LAPTOP-A3LRA9TF;"
            "DATABASE=PetPals;"
            "Trusted_Connection=yes;"
        )
        print("Database connection established successfully.")
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None
