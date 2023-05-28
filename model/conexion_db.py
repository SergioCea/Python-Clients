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
            NOMBRE VARCHAR(25) UNIQUE CHECK(length(NOMBRE) <= 25) NOT NULL,
            CIF VARCHAR(9) UNIQUE CHECK(length(CIF) == 9) NOT NULL,
            TLF VARCHAR(10) CHECK(length(TLF) <= 10) NOT NULL,
            TLF2 VARCHAR(10) CHECK(length(TLF2) <= 10),
            PROVINCIA VARCHAR(25) CHECK(length(PROVINCIA) <= 25),
            POBLACION VARCHAR(25) CHECK(length(POBLACION) <= 25),
            DIRECCION VARCHAR(50) CHECK(length(DIRECCION) <= 50),
            CP VARCHAR(5) CHECK(length(CP) == 5),
            BANCO VARCHAR(50) CHECK(length(BANCO) <= 50) NOT NULL)"""
            self.cursor.execute(sql)

        if not self.table_exists('BANCO'):
            sql = """CREATE TABLE BANCO (
            ID_BANCO INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50)CHECK(length(NOMBRE) <= 50),
            CIF VARCHAR(9) UNIQUE CHECK(length(CIF) == 9)  NOT NULL,
            CIF_CLIENTE VARCHAR(9) UNIQUE CHECK(length(CIF) == 9) NOT NULL,
            TLF VARCHAR(10) CHECK(length(TLF) <= 10),
            DIRECCION VARCHAR(50) CHECK(length(DIRECCION) <= 50),
            IBAN VARCHAR(25) UNIQUE CHECK(length(IBAN) <= 25) NOT NULL)"""
            self.cursor.execute(sql)

        self.close_db()

    def close_db(self):
        """
        Función para cerrar la conexión y confirmar los cambios
        """
        self.connection.commit()
        self.connection.close()

    def table_exists(self, table):
        """
        Función para comprobar si una tabla existe
        """
        sql = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'"
        self.cursor.execute(sql)
        if len(self.cursor.fetchall()) > 0:
            return True
        return False
