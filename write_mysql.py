from sqlalchemy import create_engine
from read_sqls import read_sqls

from settings import settings_mysql, settings_sqls


def write_mysql():
    print('Escribiendo en el servidor...')

    data = read_sqls(settings_sqls)
    engine_call = "mysql+pymysql://{user}:{pw}@" + settings_mysql['host'] + "/{db}"
    engine = create_engine(engine_call
                           .format(user=settings_mysql["user"],
                                   pw=settings_mysql["password"],
                                   db=settings_mysql["db"]))

    data.to_sql('movements', con = engine, if_exists = 'replace', chunksize = 1000)


if __name__ == "__main__":
    write_mysql()