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
    """
    Guarda los datos del cliente en la base de datos

    :param cliente: Cliente a guardar
    :param table: Tabla donde se guardarán los datos
    :return: True si se guardó correctamente
    """
    conexion = ConexionDB()
    datos = list(filter(lambda x: not x.startswith("__") and not callable(getattr(cliente, x)), dir(cliente)))
    vacios = [dato for dato in datos if cliente.__dict__[dato] == '' or cliente.__dict__[dato] is None or cliente.__dict__[dato] == 'None']

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


def edit_client(cliente, id_client, table):
    """
    Actualiza los datos del cliente en la base de datos y los muestra en la tabla

    :param cliente: Cliente a actualizar
    :param id_client: ID del cliente
    :param table: Tabla donde se mostrarán los datos
    :return: True si se actualizó correctamente

    """
    conexion = ConexionDB()
    datos = list(filter(lambda x: not x.startswith("__") and not callable(getattr(cliente, x)), dir(cliente)))
    vacios = [dato for dato in datos if cliente.__dict__[dato] == '' or cliente.__dict__[dato] is None or cliente.__dict__[dato] == 'None']

    valores = tuple(dato.upper() for dato in datos if dato not in vacios)
    valores_datos = tuple(cliente.__dict__[dato] for dato in datos if dato not in vacios)

    try:
        for nombre, valor in zip(valores, valores_datos):
            sql = f"""UPDATE CLIENTE SET {nombre} = '{valor}' WHERE ID_CLIENTE = '{id_client}'"""
            conexion.cursor.execute(sql)
        title = 'Actualizar Cliente'
        message = 'El cliente se actualizo correctamente'
        messagebox.showinfo(title, message)
        conexion.close_db()
        list_edit(table, id_client)
        return True
    except Exception as e:
        print(e)
        title = 'Actualizar Cliente'
        message = 'Error al actualizar el cliente'
        messagebox.showerror(title, message)


def list_edit(table, id_cliente):
    """
    Muestra los datos del cliente en la tabla

    :param table: Tabla donde se mostrarán los datos
    :param id_cliente: ID del cliente
    """
    conexion = ConexionDB()
    sql = f"SELECT NOMBRE, CIF, TLF, TLF2, PROVINCIA, POBLACION, DIRECCION, CP, BANCO FROM cliente WHERE id_cliente = '{id_cliente}'"

    try:
        conexion.cursor.execute(sql)
        rows = conexion.cursor.fetchall()

        i = 0
        for row in rows:
            table.delete(*table.get_children())
            dato = list(row)
            for r in dato:
                if r is None:
                    dato[dato.index(r)] = ''
            table.insert('', i, text='1', values=dato)
            int(i) + 1
        conexion.close_db()
    except Exception as e:
        print(e)
        title = 'Listar Cliente Actualizado'
        message = 'Error al listar el cliente'
        messagebox.showerror(title, message)


def search_client(client, table):
    """
    Busca el cliente en la base de datos

    :param client: Cliente a buscar
    :param table: Tabla donde se mostrarán los datos

    """
    conexion = ConexionDB()

    sql = f"""SELECT NOMBRE, CIF, TLF, TLF2, PROVINCIA, POBLACION, DIRECCION, CP, BANCO 
    FROM cliente WHERE NOMBRE LIKE '{client.nombre}%'"""

    try:
        conexion.cursor.execute(sql)
        rows = conexion.cursor.fetchall()
        i = 0
        for row in rows:
            dato = list(row)
            for r in dato:
                if r is None:
                    dato[dato.index(r)] = ''
            table.insert('', i, text='1', values=dato)
            int(i) + 1
        conexion.close_db()
    except Exception as e:
        print(e)
        title = 'Buscar Cliente'
        message = 'Error al buscar el cliente'
        messagebox.showerror(title, message)
        logger.error(e)


def delete_client(cif):
    """
    Elimina el cliente de la base de datos

    :param cif: CIF del cliente a eliminar
    """
    conexion = ConexionDB()
    sql = f"DELETE FROM cliente WHERE CIF = '{cif}'"
    try:
        conexion.cursor.execute(sql)
        title = 'Eliminar Cliente'
        message = 'El cliente se elimino correctamente'
        messagebox.showinfo(title, message)
        conexion.close_db()
    except Exception as e:
        print(e)
        title = 'Eliminar Cliente'
        message = 'Error al eliminar el cliente'
        messagebox.showerror(title, message)
        logger.error(e)


def load_bank(client=None):
    """
    Función para cargar los bancos segun el cliente

    :param client: Cliente a buscar
    :return: lista de bancos
    """
    conexion = ConexionDB()

    if client is not None and client != '':
        sql = f"SELECT IBAN FROM banco WHERE CIF_CLIENTE = '{client}'"
        conexion.cursor.execute(sql)

        rows = conexion.cursor.fetchall()
        options = [f"{row[0]}" for row in rows]

        conexion.close_db()

        return options
    elif client == '':
        return "None"
