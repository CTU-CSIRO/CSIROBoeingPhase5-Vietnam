import pyodbc

# Example connection string, modify based on your environment
connection = pyodbc.connect("DSN=Your_DSN_Name;UID=your_username;PWD=your_password")

# Create a cursor
cursor = connection.cursor()

# Execute a query (example: reading table)
cursor.execute("SELECT * FROM your_table")

# Fetch the data
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()
