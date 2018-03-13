#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3
import lib.SQLScript
import lib.master

# sql = lib.SQLScript
# conn = sqlite3.connect('..\DBDOM.db')
# cur = conn.cursor()
# cur.execute("select * from Street")
# value = cur.fetchone()
# print(value)

class connect:
    conn = sqlite3.connect('..\DBDOM.db')
    cur = conn.cursor()

    @staticmethod
    def select(select):
        return connect.cur.execute(select).fetchall()
    @staticmethod
    def insertMaster(master):
        connect.cur.executemany("INSERT INTO Master VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [master.getValue()])
        connect.conn.commit()
    @staticmethod
    def insertAllMaster(listMaster):
        listError = []
        if(list == type(listMaster)):
            for master in listMaster:
                try:
                    connect.insertMaster(master)
                except Exception as ex:
                    print("Ошибка внесения в базу '{0}'\n{1}".format(master, ex))
                    listError.append(master)
        else:
            print("Ошибка не список master")
        return listError

if __name__ == "__main__":
    conn = connect
    mas = lib.master.master()
    print(conn.select("select count(*) from Master"))

    err = conn.insertAllMaster(mas.getValueJson())
    print(len(err))
