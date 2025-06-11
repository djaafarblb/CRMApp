import mysql.connector
import os
from pathlib import Path

def get_secret(setting):
    base_dir = Path(__file__).resolve().parent
    secrets_file = os.path.join(base_dir, 'secrets.txt')
    try:
        with open(secrets_file) as f:
            secrets = dict(line.strip().split('=', 1) for line in f)
        return secrets[setting]
    except (KeyError, FileNotFoundError):
        error_msg = f"Set the {setting} in secrets.txt"
        raise Exception(error_msg)

try:
    # Connect to MySQL as root
    conn = mysql.connector.connect(
        host=get_secret('DB_HOST'),
        user='root',
        password=get_secret('MYSQL_ROOT_PASSWORD')
    )
    
    cursor = conn.cursor()
    
    # Create a new user
    cursor.execute(f"CREATE USER IF NOT EXISTS '{get_secret('DB_USER')}'@'localhost' IDENTIFIED BY '{get_secret('DB_PASSWORD')}'")
    
    # Grant all privileges on elderco database
    cursor.execute(f"GRANT ALL PRIVILEGES ON {get_secret('DB_NAME')}.* TO '{get_secret('DB_USER')}'@'localhost'")
    cursor.execute("FLUSH PRIVILEGES")
    
    print("User created successfully with all privileges on database")
    
    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print(f"Error: {err}") 