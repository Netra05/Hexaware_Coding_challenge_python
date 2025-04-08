from util.db_conn_util import get_connection

try:
    conn = get_connection()
    print("Database connection established successfully!")

    cursor = conn.cursor()
    cursor.execute("SELECT GETDATE();")
    result = cursor.fetchone()
    print("Current DB Time:", result[0])

    conn.close()

except Exception as e:
    print("Connection failed:", e)
