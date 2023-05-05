import re
import sqlite3
from model.conexion_db import ConexionDB
from tkinter import messagebox
from model.logger import Logger


class Banco:
    def __init__(self, name, cif, tlf, direccion, iban):
        self.id_banco = None
        self.name = name
        self.cif = cif
        self.tlf = tlf
        self.direccion = direccion
        self.iban = iban

    def __str__(self):
        return f'Banco[{self.name}, {self.cif}, {self.tlf}, {self.direccion}, {self.iban}]'


logger = Logger("settings.yaml").logger


def save_data_bank(banco, table):
    conexion = ConexionDB()
    datos = list(filter(lambda x: not x.startswith("__") and not callable(getattr(banco, x)), dir(banco)))
    for dato in datos:
        if banco.__dict__[dato] == '':
            banco.__dict__[dato] = None

    sql = f"""INSERT INTO BANCO (NOMBRE, CIF, TLF, DIRECCION, IBAN) VALUES 
    ('{banco.name}', '{banco.cif}', '{banco.tlf}', '{banco.direccion}', '{banco.iban}')"""

    try:
        conexion.cursor.execute(sql)
        sql = f"SELECT NOMBRE, CIF, TLF, DIRECCION " \
              f"FROM banco WHERE cif = '{banco.cif}'"

        try:
            conexion.cursor.execute(sql)
            rows = conexion.cursor.fetchall()

            i = 0
            for row in rows:
                table.insert('', i, text='1', values=row)
                int(i) + 1
            conexion.close_db()
            title = 'Crear Banco'
            message = f'Banco con CIF {banco.cif} se ha creado correctamente'
            messagebox.showinfo(title, message)
            logger.info(f'Banco con CIF {banco.cif} se ha creado correctamente')

        except Exception as e:
            print(e)
            title = 'Listar Banco Nuevo'
            message = 'Error al listar el banco'
            messagebox.showerror(title, message)
    except sqlite3.IntegrityError as e:
        fail = re.search(r'length\(([^)]+)\)', str(e))
        title = 'Crear Banco'
        message = f'Error al crear el banco, revise el campo {fail.group(1)}'
        messagebox.showerror(title, message)
