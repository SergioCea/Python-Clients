import tkinter as tk
from tkinter import ttk
from model.client import Cliente, save_data_client, load_bank
from model.conexion_db import ConexionDB


class Frame_Client(tk.Frame):
    def __init__(self, root=None, pes=None):
        super().__init__(root)
        self.root = root
        self.id_cliente = None
        self.pes1 = pes
        self.properties_client()

        self.disable_fields()

        self.table_client()

    def properties_client(self):
        # Labels datos del cliente
        self.label_nombre = tk.Label(self.pes1, text='Nombre:')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_direccion = tk.Label(self.pes1, text='Dirección:')
        self.label_direccion.grid(row=1, column=0, pady=10)

        self.label_poblacion = tk.Label(self.pes1, text='Población:')
        self.label_poblacion.grid(row=1, column=2, pady=10)

        self.label_cp = tk.Label(self.pes1, text='CP:')
        self.label_cp.grid(row=1, column=6, pady=10)

        self.label_provincia = tk.Label(self.pes1, text='Provincia:')
        self.label_provincia.grid(row=1, column=4, pady=10)

        self.label_cif = tk.Label(self.pes1, text='CIF:')
        self.label_cif.grid(row=0, column=2, pady=10)

        self.label_tlf = tk.Label(self.pes1, text='Telefono/Movil:')
        self.label_tlf.grid(row=0, column=4, pady=10)

        self.label_tlf2 = tk.Label(self.pes1, text='Otro telefono:')
        self.label_tlf2.grid(row=0, column=6, pady=10)

        """
        self.label_fax = tk.Label(self, text='Fax:')
        self.label_fax.grid(row=0, column=8, pady=10)
        """

        self.label_banco = tk.Label(self.pes1, text='Banco:')
        self.label_banco.grid(row=1, column=8, pady=10)

        # Entrys de los datos
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self.pes1, textvariable=self.nombre)
        self.entry_nombre.config(width=30)
        self.entry_nombre.grid(row=0, column=1)

        self.cif = tk.StringVar()
        self.entry_cif = tk.Entry(self.pes1, textvariable=self.cif)
        self.entry_cif.config()
        self.entry_cif.grid(row=0, column=3)

        self.tlf = tk.StringVar()
        self.entry_tlf = tk.Entry(self.pes1, textvariable=self.tlf)
        self.entry_tlf.config()
        self.entry_tlf.grid(row=0, column=5)

        self.tlf2 = tk.StringVar()
        self.entry_tlf2 = tk.Entry(self.pes1, textvariable=self.tlf2)
        self.entry_tlf2.config()
        self.entry_tlf2.grid(row=0, column=7)

        """
        self.fax = tk.StringVar()
        self.entry_fax = tk.Entry(self, textvariable=self.fax)
        self.entry_fax.config()
        self.entry_fax.grid(row=0, column=9)
        """

        self.banco = tk.StringVar()
        self.options = load_bank()
        self.entry_banco = tk.OptionMenu(self.pes1, self.banco, '', *self.options)
        self.entry_banco.grid(row=1, column=9, pady=10, padx=10)
        # Agregar un rastreador de cambios en la variable del campo select
        self.banco.trace('w', self.actualizar_opciones)

        self.direcion = tk.StringVar()
        self.entry_direccion = tk.Entry(self.pes1, textvariable=self.direcion)
        self.entry_direccion.config(width=30)
        self.entry_direccion.grid(row=1, column=1, pady=10)

        self.poblacion = tk.StringVar()
        self.entry_poblacion = tk.Entry(self.pes1, textvariable=self.poblacion)
        self.entry_poblacion.config()
        self.entry_poblacion.grid(row=1, column=3, pady=10)

        self.provincia = tk.StringVar()
        self.entry_provincia = tk.Entry(self.pes1, textvariable=self.provincia)
        self.entry_provincia.config()
        self.entry_provincia.grid(row=1, column=5, pady=10)

        self.cp = tk.StringVar()
        self.entry_cp = tk.Entry(self.pes1, textvariable=self.cp)
        self.entry_cp.config()
        self.entry_cp.grid(row=1, column=7, pady=10)

        # Botones
        self.boton_nuevo = tk.Button(self.pes1, text='Nuevo Cliente', command=self.enable_fields)
        self.boton_nuevo.config(width=15, cursor='hand2')
        self.boton_nuevo.grid(row=2, column=3, pady=10, columnspan=1)

        self.boton_guardar = tk.Button(self.pes1, text='Guardar', command=self.save_data)
        self.boton_guardar.config(width=10, cursor='hand2')
        self.boton_guardar.grid(row=2, column=4, pady=10, columnspan=2)

        self.boton_cancelar = tk.Button(self.pes1, text='Cancelar', command=self.clean_fields)
        self.boton_cancelar.config(width=10, cursor='hand2')
        self.boton_cancelar.grid(row=2, column=6, pady=10, columnspan=1)

    def enable_fields(self):
        self.entry_nombre.config(state='normal')
        self.entry_cif.config(state='normal')
        self.entry_tlf.config(state='normal')
        self.entry_tlf2.config(state='normal')
        self.entry_provincia.config(state='normal')
        self.entry_banco.config(state='normal')
        # self.entry_fax.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_poblacion.config(state='normal')
        self.entry_cp.config(state='normal')

        self.boton_cancelar.config(state='normal')
        self.boton_guardar.config(state='normal')

    def clean_fields(self):
        # Cliente nuevo
        self.nombre.set('')
        self.cif.set('')
        self.tlf.set('')
        self.tlf2.set('')
        self.direcion.set('')
        # self.fax.set('')
        self.banco.set('')
        self.provincia.set('')
        self.cp.set('')
        self.poblacion.set('')

    def disable_fields(self):
        self.clean_fields()

        # Nuevo cliente
        self.entry_nombre.config(state='disabled')
        self.entry_cif.config(state='disabled')
        self.entry_tlf.config(state='disabled')
        self.entry_tlf2.config(state='disabled')
        self.entry_provincia.config(state='disabled')
        self.entry_banco.config(state='disabled')
        # self.entry_fax.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.entry_poblacion.config(state='disabled')
        self.entry_cp.config(state='disabled')

        self.boton_cancelar.config(state='disabled')
        self.boton_guardar.config(state='disabled')

    def save_data(self):
        client = Cliente(
            self.nombre.get(),
            self.cif.get(),
            self.tlf.get(),
            self.tlf2.get(),
            # self.fax.get(),
            self.provincia.get(),
            self.poblacion.get(),
            self.direcion.get(),
            self.cp.get(),
            self.banco.get(),
        )

        save_data_client(client, self.tabla)

        # Limpiar campos
        self.clean_fields()

    def table_client(self):
        self.tabla = ttk.Treeview(self.pes1, columns=('Nombre', 'CIF', 'Telefono', 'Otro telefono', 'Provincia',
                                                      'Población', 'Dirección', 'CP', 'Banco'), show='headings')
        self.tabla.grid(row=4, column=0, columnspan=10, padx=(10, 0), sticky='nse')
        self.scroll = ttk.Scrollbar(self.pes1,
                                    orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=10, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
        # self.list_client = list_save()

        self.tabla.heading('#1', text='Nombre', anchor='center')
        self.tabla.column('Nombre', width=100, anchor='center')
        self.tabla.heading('#2', text='CIF')
        self.tabla.column('CIF', width=80, anchor='center')
        self.tabla.heading('#3', text='Telefono')
        self.tabla.column('Telefono', width=150, anchor='center')
        self.tabla.heading('#4', text='Otro telefono')
        self.tabla.column('Otro telefono', width=150, anchor='center')
        self.tabla.heading('#5', text='Provincia')
        self.tabla.column('Provincia', width=125, anchor='center')
        self.tabla.heading('#6', text='Población')
        self.tabla.column('Población', width=125, anchor='center')
        self.tabla.heading('#7', text='Dirección')
        self.tabla.column('Dirección', width=200, anchor='center')
        self.tabla.heading('#8', text='CP')
        self.tabla.column('CP', width=50, anchor='center')
        self.tabla.heading('#9', text='Banco')
        self.tabla.column('Banco', width=100, anchor='center')

    def actualizar_opciones(self, *args):
        options = load_bank()
        # Obtener el valor actual del campo de entrada
        valor = self.banco.get().lower()

        # Obtener todas las opciones que contienen el valor actual
        opciones_filtradas = [opcion for opcion in options if valor in opcion.lower()]

        # Actualizar las opciones del campo select
        self.entry_banco['menu'].delete(0, 'end')
        for opcion in opciones_filtradas:
            self.entry_banco['menu'].add_command(label=opcion, command=tk._setit(self.banco, opcion))
