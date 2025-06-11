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

dataBase = mysql.connector.connect(
    host=get_secret('DB_HOST'),
    user='root',
    passwd=get_secret('MYSQL_ROOT_PASSWORD')
)

cursorObject = dataBase.cursor()

cursorObject.execute(f"CREATE DATABASE {get_secret('DB_NAME')}")

print("Database created successfully")