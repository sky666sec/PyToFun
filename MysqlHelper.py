# encoding=utf8
import pymysql


class MysqlHelper():
    def __init__(self, host, port, db, user, passwd, charset="utf8"):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db,
                                    user=self.user, password=self.passwd, charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql, params):
        result = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)
        return result

    def insert(self, sql, params):
        return self.__edit(sql, params)

    def update(self, sql, params):
        return self.__edit(sql, params)

    def delete(self, sql, params):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        try:
            self.connect()
            conut = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return conut
