import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="mysql123")
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE IF EXISTS Library")
    print("Database reset successfully! The new names will be applied next time you run ProjectLogin.py.")
except Exception as e:
    print(f"Error resetting database: {e}")
