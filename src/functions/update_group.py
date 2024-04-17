#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""


# UPDATE
def db_update_product_price(cursor,
                            connection,
                            table,
                            column_2,
                            column_3,
                            product_name,
                            new_price):

    command = f'UPDATE {table} SET {column_3} = {new_price} WHERE {column_2} = "{product_name}"'

    cursor.execute(command)
    connection.commit()
