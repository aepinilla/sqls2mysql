#import pymysql
# import pandas as pd
from sqlalchemy import create_engine
from read_sql_server import get_data

from settings import settings_mysql


def write_data():
    print('Escribiendo en el servidor...')

    documento_tipos = get_data()
    engine = create_engine("mysql+pymysql://{user}:{pw}@localhost:5432/{db}"
                           .format(user = settings_mysql["user"],
                                   pw = settings_mysql["password"],
                                   db = settings_mysql["db"],

    documento_tipos.to_sql('movements', con = engine, if_exists = 'replace', chunksize = 1000)

if __name__ == "__main__":
    write_data()