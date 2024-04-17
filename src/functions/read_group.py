#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# READ
def db_read_all(cursor,
                table):

    command = f'SELECT * FROM {table}'

    cursor.execute(command)
    result = cursor.fetchall()
    print(result)
