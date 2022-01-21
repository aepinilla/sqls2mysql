import pandas as pd
import pyodbc

from settings import settings_sqls


def read_sqls(settings):
    print('Leyendo la base de datos...')

    conn = pyodbc.connect(
        Trusted_Connection='No',
        Driver='{ODBC Driver 17 for SQL Server}',
        Server=settings_sqls['server'],
        Database=settings_sqls['database'],
        UID=settings_sqls['user'],
        PWD=settings_sqls['password'])

    data_query = 'SELECT * FROM DataTable'
    data = pd.read_sql(data_query, conn)

    return data