import mysql.connector
from datetime import datetime, timedelta
import time

# MySQL database configuration
db_config = {
    "host": "sarthakjain",
    "user": "root",
    "password": "sarthakjain",
    "database": "your_database"
}

# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Table and column names
table_name = "your_table"
time_column = "time_column"

try:
    while True:
        # Retrieve rows from the table
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Update each row's time value by one second and execute the update query
        for row in rows:
            current_time = row[1]  # Assuming the time column is the second column (index 1)
            new_time = current_time + timedelta(seconds=1)
            update_query = f"UPDATE {table_name} SET {time_column} = %s WHERE id = %s"
            cursor.execute(update_query, (new_time, row[0]))  # Assuming id is the first column (index 0)
            connection.commit()
            

        print("Time values updated.")
        time.sleep(1)  # Wait for 1 second before the next iteration

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    cursor.close()
    connection.close()
