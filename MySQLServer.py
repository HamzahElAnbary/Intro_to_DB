import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server using your credentials
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="SQLHamzah@123"
        # Note: Do not include 'database' here since we're creating it
    )

    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close resources
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
