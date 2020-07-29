# Name:         Roger Silva Santos Aguiar
# Function:     This module has all the information about the database
# Initial date: July 29, 2020
# Last update:  July 29, 2020

# Required modules
import psycopg2


class DatabaseConnection:
    @staticmethod
    def my_connection():
        connection = psycopg2.connect\
            (
                user='postgres',
                password='983453069',
                host='localhost',
                port='5432',
                database='company'
            )

        return connection
