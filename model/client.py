import sqlite3
import re
from model.conexion_db import ConexionDB
from tkinter import messagebox
from model.logger import Logger


class Cliente:
    def __init__(self, nombre, cif, tlf, tlf2, provincia, poblacion, direccion, cp, banco):
        self.id_cliente = None
        self.nombre = nombre
        self.cif = cif
        self.tlf = tlf
        self.tlf2 = tlf2
        # self.fax = fax
        self.provincia = provincia
        self.poblacion = poblacion
        self.direccion = direccion
        self.cp = cp
        self.banco = banco

    def __str__(self):
        return f'Cliente[{self.nombre}, {self.cif}, {self.tlf}, {self.tlf2}, {self.provincia}, {self.poblacion}, ' \
               f'{self.direccion}, {self.cp}, {self.banco}]'


logger = Logger("settings.yaml").logger


def save_data_client(cliente, table):
    conexion = ConexionDB()
    datos = list(filter(lambda x: not x.startswith("__") and not callable(getattr(cliente, x)), dir(cliente)))
    vacios = [dato for dato in datos if cliente.__dict__[dato] == '' or cliente.__dict__[dato] is None]

    valores = tuple(dato.upper() for dato in datos if dato not in vacios)
    valores_datos = tuple(cliente.__dict__[dato] for dato in datos if dato not in vacios)

    sql = f"""INSERT INTO CLIENTE {valores} VALUES {valores_datos}"""

    # sql = f"""INSERT INTO CLIENTE (NOMBRE, CIF, TLF, TLF2, PROVINCIA, POBLACION, DIRECCION, CP, BANCO) VALUES
    # ('{cliente.name}', '{cliente.cif}', '{cliente.tlf}', '{cliente.tlf2}', '{cliente.provincia}', '{cliente.poblacion}',
    # '{cliente.direccion}', '{cliente.cp}', '{cliente.banco}')"""

    try:
        conexion.cursor.execute(sql)
        sql = f"SELECT NOMBRE, CIF, TLF, TLF2, PROVINCIA, POBLACION, DIRECCION, CP, BANCO " \
              f"FROM cliente WHERE cif = '{cliente.cif}'"

        try:
            conexion.cursor.execute(sql)
            rows = conexion.cursor.fetchall()

            i = 0
            for row in rows:
                table.insert('', i, text='1', values=row)
                int(i) + 1
            conexion.close_db()
            title = 'Crear Cliente'
            message = f'Cliente con CIF {cliente.cif} se ha creado correctamente'
            messagebox.showinfo(title, message)
            logger.info(f'Cliente con CIF {cliente.cif} se ha creado correctamente')
            return True
        except Exception as e:
            print(e)
            title = 'Listar Cliente Nuevo'
            message = 'Error al listar el cliente'
            messagebox.showerror(title, message)
    except sqlite3.IntegrityError as e:
        fail = re.search(r'length\(([^)]+)\)', str(e))
        title = 'Crear Cliente'
        message = f'Error al crear el cliente, revise el campo {fail.group(1)}'
        messagebox.showerror(title, message)


def edit_client(client, id_client):
    conexion = ConexionDB()

    sql = f"""UPDATE CLIENTE 
                SET NOMBRE = '{client.name}', CIF= '{client.cif}', TLF= '{client.tlf}', TLF2= '{client.tlf2}', 
                PROVINCIA= '{client.provincia}', POBLACION= '{client.poblacion}',DIRECCION= '{client.direccion}', 
                CP= '{client.cp}', BANCO= '{client.banco}' WHERE ID_CLIENTE = '{id_client}'"""

    try:
        conexion.cursor.execute(sql)
        title = 'Actualizar Cliente'
        message = 'El cliente se actualizo correctamente'
        messagebox.showinfo(title, message)
        conexion.close_db()
    except Exception as e:
        print(e)
        title = 'Actualizar Cliente'
        message = 'Error al actualizar el cliente'
        messagebox.showerror(title, message)


def list_edit(table, id_cliente):
    conexion = ConexionDB()
    sql = f"SELECT NOMBRE, CIF, TLF, TLF2, PROVINCIA, POBLACION, DIRECCION, CP, BANCO " \
          f"FROM cliente WHERE id_cliente = '{id_cliente}'"

    try:
        conexion.cursor.execute(sql)
        rows = conexion.cursor.fetchall()

        i = 0
        for row in rows:
            table.delete(*table.get_children())
            table.insert('', i, text='1', values=row)
            int(i) + 1
        conexion.close_db()
    except Exception as e:
        print(e)
        title = 'Listar Cliente Actualizado'
        message = 'Error al listar el cliente'
        messagebox.showerror(title, message)


def search_client(client, table):
    conexion = ConexionDB()

    sql = f"""SELECT NOMBRE, CIF, TLF, TLF2, PROVINCIA, POBLACION, DIRECCION, CP, BANCO FROM cliente WHERE NOMBRE LIKE '{client.name}%'"""

    try:
        conexion.cursor.execute(sql)
        rows = conexion.cursor.fetchall()

        i = 0
        for row in rows:
            table.insert('', i, text='1', values=row)
            int(i) + 1
        conexion.close_db()
    except Exception as e:
        print(e)
        title = 'Buscar Cliente'
        message = 'Error al buscar el cliente'
        messagebox.showerror(title, message)
        logger.error(e)


def load_bank():
    conexion = ConexionDB()
    sql = f"SELECT nombre FROM banco"
    conexion.cursor.execute(sql)

    rows = conexion.cursor.fetchall()
    options = [f"{row[0]}" for row in rows]

    conexion.close_db()

    return options

