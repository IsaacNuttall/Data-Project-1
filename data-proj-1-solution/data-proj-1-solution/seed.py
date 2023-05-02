import psycopg2
from psycopg2 import Error

from database import get_connected

from customer_table import create_customers, insert_customers
from invoices_table import create_invoices, insert_invoices

try:
    
    # connection to database

    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()

    print("Connection successful.")

    ############### CREATING TABLES AND INSERTING INFORMATION ###############

    print("Seeding database...")

    cursor.execute(create_customers)
    connection.commit()
    print("Customer table was created successfully.")

    cursor.execute(insert_customers)
    connection.commit()
    print("Customer information was inserted successfully.")

    cursor.execute(create_invoices)
    connection.commit()
    print("Invoices table was created successfully.")

    cursor.execute(insert_invoices)
    connection.commit()
    print("Invoices were inserted successfully")

# handles errors and prints them to the console - DO NOT ALTER OR DELETE

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")