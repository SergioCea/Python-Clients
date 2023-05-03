from model.conexion_db import ConexionDB
from tkinter import messagebox
from model.logger import Logger


class Banco:
    def __init__(self, name, cif, tlf, direccion):
        self.id_banco = None
        self.name = name
        self.cif = cif
        self.tlf = tlf
        self.direccion = direccion

    def __str__(self):
        return f'Banco[{self.name}, {self.cif}, {self.tlf}, {self.direccion}]'

logger = Logger("settings.yaml").logger
def save_data_bank(banco, table):
    conexion = ConexionDB()

    sql = f"""INSERT INTO BANCO (NOMBRE, CIF, TLF, DIRECCION) VALUES 
    ('{banco.name}', '{banco.cif}', '{banco.tlf}', '{banco.direccion}')"""

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
            title = 'Crear Cliente'
            message = f'Cliente con CIF {banco.cif} se ha creado correctamente'
            messagebox.showinfo(title, message)
            logger.info(f'Banco con CIF {banco.cif} se ha creado correctamente')

        except Exception as e:
            print(e)
            title = 'Listar Cliente Nuevo'
            message = 'Error al listar el cliente'
            messagebox.showerror(title, message)
    except Exception as e:
        print(e)
        title = 'Crear Cliente'
        message = 'Error al crear el cliente'
        messagebox.showerror(title, message)
