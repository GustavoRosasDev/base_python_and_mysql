#!/usr/bin/env python3

"""
Developer: Gustavo Rosas
Profile: https://www.linkedin.com/in/gustavorosas-/
"""

from src.manager import connection, cursor
from src.functions_manager import db_create_product, db_read_all, db_update_product_price, db_delete_product


def main(chosen_command):
    match chosen_command:
        case "CREATE":
            db_create_product(cursor, connection, table_name, column_2_name, column_3_name, product_name, product_price)
        case "READ":
            db_read_all(cursor, table_name)
        case "UPDATE":
            db_update_product_price(cursor, connection, table_name, column_2_name, column_3_name, product_name,
                                    product_price)
        case "DELETE":
            db_delete_product(cursor, connection, table_name, column_2_name, product_name)

    cursor.close()
    connection.close()


if __name__ == "__main__":
    command = 'CREATE'  # Options: CREATE, READ, UPDATE and DELETE

    table_name = "your_table_name"

    column_2_name = "second_column_name"
    column_3_name = "third_column_name"

    product_name = "Water"
    product_price = "5"

    main(command)
