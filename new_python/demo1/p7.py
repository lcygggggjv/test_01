import json
from pymysql import *
import pymysql

# list2 = ['{"k": 2}', {"e": 2}, '{"w": "k"}', ('y', 2), ('v', 5)]
#
# for s in list2:
#
#     if isinstance(s, str):
#         w = json.loads(s)
#     elif isinstance(s, tuple):
#
#         w = dict([s])
#
#     else:
#         w = s
#
#     print(type(w), w)


def connect():

    db = pymysql.connect(host='127.0.0.1', user='root', password='123456789', database='lcy1', charset='utf8')

    return db


db = connect()


def create_database(db):

    cursor = db.cursor()

    sql = '''CREATE TABLE persons
        (id INT PRIMARY KEY     NOT NULL,
        name        TEXT        NOT NULL,
        age          INT        NOT NULL,
        address       CHAR(200),
        salary        REAL);
        '''

    try:
        cursor.execute(sql)

        db.commit()

        return True
    except:

        db.rollback()

    return False


create_database(db)
