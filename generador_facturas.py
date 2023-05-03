import tkinter as tk
from tkinter import ttk
from client.interfaz_gui import Frame_Client
from client.search_client_gui import Frame_Search
from client.banco_gui import Frame_Banco
from model.conexion_db import ConexionDB
import os
import sys

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Generador de Facturas")
        path = resource_path("images/logo.ico")
        self.iconbitmap(path)

        self.nav_bar = tk.Menu(self)
        self.item_cliente = tk.Menu(self.nav_bar, tearoff=0)
        self.nav_bar.add_cascade(label="Cliente", menu=self.item_cliente)
        self.item_cliente.add_command(label="Nuevo Cliente", command=self.new_client)
        self.item_cliente.add_command(label="Editar/Buscar Clientes", command=self.search_client)

        self.item_banco = tk.Menu(self.nav_bar, tearoff=0)
        self.nav_bar.add_cascade(label="Banco", menu=self.item_banco)
        self.item_banco.add_command(label="Nuevo Banco", command=self.new_bank)

        self.nuevo_cliente = ttk.Frame(self)
        self.buscar_cliente = ttk.Frame(self)
        self.crear_banco = ttk.Frame(self)

        #current_size = tk.StringVar(value=self.geometry())
        Frame_Client(root=self, pes=self.nuevo_cliente)
        Frame_Search(root=self, pes=self.buscar_cliente)
        Frame_Banco(root=self, pes=self.crear_banco)

        self.config(menu=self.nav_bar)
        self.show_frame("Frame_Client")
    def show_frame(self, frame_name):
        if frame_name == "Frame_Client":
            self.geometry("1120x420")
            frame = self.nuevo_cliente
        elif frame_name == "Frame_Search":
            self.geometry("1120x420")
            frame = self.buscar_cliente
        elif frame_name == "Frame_Banco":
            self.geometry("570x370")
            frame = self.crear_banco
        else:
            return

        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def search_client(self):
        self.show_frame("Frame_Search")

    def new_client(self):
        self.show_frame("Frame_Client")

    def new_bank(self):
        self.show_frame("Frame_Banco")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception as e:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = App()
    app.mainloop()
    ConexionDB()

