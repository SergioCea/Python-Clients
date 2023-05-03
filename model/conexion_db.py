import sqlite3
import os.path

class ConexionDB:
    def __init__(self):
        self.database = "db/python.db"
        if os.path.isfile(self.database) and os.path.isfile(self.database):
            self.connection = sqlite3.connect(database=self.database)
            self.cursor = self.connection.cursor()
            return

        self.connection = sqlite3.connect(database=self.database)
        self.cursor = self.connection.cursor()

        if not self.table_exists('CLIENTE'):
            sql = """CREATE TABLE CLIENTE (
            ID_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(25),
            CIF VARCHAR(9),
            TLF VARCHAR(10),
            TLF2 VARCHAR(10),
            PROVINCIA VARCHAR(25),
            POBLACION VARCHAR(25),
            DIRECCION VARCHAR(50),
            CP VARCHAR(5),
            BANCO VARCHAR(50))"""
            self.cursor.execute(sql)

        if not self.table_exists('BANCO'):
            sql = """CREATE TABLE BANCO (
            ID_BANCO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            CIF VARCHAR(9),
            TLF VARCHAR(10),
            DIRECCION VARCHAR(50))"""
            self.cursor.execute(sql)

        self.close_db()

    def close_db(self):
        self.connection.commit()
        self.connection.close()

    def table_exists(self, table):
        sql = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
        self.cursor.execute(sql)
        if len(self.cursor.fetchall()) > 0:
            return True
        return False