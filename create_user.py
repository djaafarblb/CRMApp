import mysql.connector

try:
    # Connect to MySQL as root
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='djaafar24'
    )
    
    cursor = conn.cursor()
    
    # Create a new user
    cursor.execute("CREATE USER IF NOT EXISTS 'django_user'@'localhost' IDENTIFIED BY 'django_password'")
    
    # Grant all privileges on elderco database
    cursor.execute("GRANT ALL PRIVILEGES ON elderco.* TO 'django_user'@'localhost'")
    cursor.execute("FLUSH PRIVILEGES")
    
    print("User 'django_user' created successfully with all privileges on 'elderco' database")
    
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}") 