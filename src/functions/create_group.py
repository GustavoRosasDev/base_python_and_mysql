#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# CREATE
def db_create_product(cursor,
                      connection,
                      table,
                      column_2,
                      column_3,
                      product_name,
                      price):

    command = f'INSERT INTO {table} ({column_2}, {column_3}) VALUES ("{product_name}", {price})'

    cursor.execute(command)
    connection.commit()
