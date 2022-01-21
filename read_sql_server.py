import pandas as pd
import pyodbc

from settings import settings_sqlserver


def get_data(settings):
    print('Leyendo la base de datos...')

    conn = pyodbc.connect(
        Trusted_Connection = settings_sqlserver['trusted_connection'],
        Driver = settings_sqlserver['driver'],
        Server = settings_sqlserver['server'],
        Database = settings_sqlserver['database'],
        UID = settings_sqlserver['USER_NAME'],
        PWD = settings_sqlserver['PASSWORD'])

    documento_tipos_query = 'SELECT * FROM DOCUMENTO_TIPOS'
    documento_tipos = pd.read_sql(documento_tipos_query, conn)

    return documento_tipos