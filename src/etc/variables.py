#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.manager import os, mysql, load_dotenv

# Loads and instantiates data saved in the .env file
load_dotenv()
user = os.getenv("user")
_password = os.getenv("password")
database = os.getenv("database")

# Initiates the connection to the database
connection = mysql.connector.connect(
    host='localhost',
    user=user,
    password=_password,
    database=database,
)

# Creates the cursor (responsible for executing commands in the database)
cursor = connection.cursor()
