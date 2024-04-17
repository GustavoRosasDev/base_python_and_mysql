#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# DELETE
def db_delete_product(cursor,
                      connection,
                      table,
                      column_2,
                      product_name):

    command = f'DELETE FROM {table} WHERE {column_2} = "{product_name}"'

    cursor.execute(command)
    connection.commit()
