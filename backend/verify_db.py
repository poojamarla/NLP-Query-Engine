import sqlite3
import os

# Path to test.db inside backend folder
db_path = os.path.join(os.path.dirname(__file__), "test.db")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Connected to DB:", db_path)

# Show tables
print("\nAvailable tables:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for t in tables:
    print("-", t[0])

# Print departments
print("\nDepartments:")
cursor.execute("SELECT * FROM departments;")
for row in cursor.fetchall():
    print(row)

# Print employees
print("\nEmployees:")
cursor.execute("SELECT * FROM employees;")
for row in cursor.fetchall():
    print(row)

conn.close()