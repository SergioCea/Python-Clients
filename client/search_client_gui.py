import tkinter as tk
from tkinter import ttk
from model.conexion_db import ConexionDB
from model.client import Cliente, edit_client, list_edit, search_client


class Frame_Search(tk.Frame):
    def __init__(self, root=None, pes=None):
        super().__init__(root)
        self.root = root
        self.id_cliente = None
        self.pes2 = pes
        self.search_client()
        self.disable_fields()

        self.table_client_search()

    def search_client(self):
        # Labels datos del cliente
        self.label_nombre_bus = tk.Label(self.pes2, text='Nombre:')
        self.label_nombre_bus.grid(row=0, column=0, padx=10, pady=10)

        self.label_direccion_bus = tk.Label(self.pes2, text='Dirección:')
        self.label_direccion_bus.grid(row=1, column=0, pady=10)

        self.label_poblacion_bus = tk.Label(self.pes2, text='Población:')
        self.label_poblacion_bus.grid(row=1, column=2, pady=10)

        self.label_cp_bus = tk.Label(self.pes2, text='CP:')
        self.label_cp_bus.grid(row=1, column=6, pady=10)

        self.label_provincia_bus = tk.Label(self.pes2, text='Provincia:')
        self.label_provincia_bus.grid(row=1, column=4, pady=10)

        self.label_cif_bus = tk.Label(self.pes2, text='CIF:')
        self.label_cif_bus.grid(row=0, column=2, pady=10)

        self.label_tlf_bus = tk.Label(self.pes2, text='Telefono/Movil:')
        self.label_tlf_bus.grid(row=0, column=4, pady=10)

        self.label_tlf2_bus = tk.Label(self.pes2, text='Otro telefono:')
        self.label_tlf2_bus.grid(row=0, column=6, pady=10)

        """
        self.label_fax = tk.Label(self, text='Fax:')
        self.label_fax.grid(row=0, column=8, pady=10)
        """

        self.label_banco_bus = tk.Label(self.pes2, text='Banco:')
        self.label_banco_bus.grid(row=1, column=8, pady=10)

        # Entrys de los datos
        self.nombre_bus = tk.StringVar()
        self.entry_nombre_bus = tk.Entry(self.pes2, textvariable=self.nombre_bus)
        self.entry_nombre_bus.config(width=30)
        self.entry_nombre_bus.grid(row=0, column=1)

        self.cif_bus = tk.StringVar()
        self.entry_cif_bus = tk.Entry(self.pes2, textvariable=self.cif_bus)
        self.entry_cif_bus.config()
        self.entry_cif_bus.grid(row=0, column=3)

        self.tlf_bus = tk.StringVar()
        self.entry_tlf_bus = tk.Entry(self.pes2, textvariable=self.tlf_bus)
        self.entry_tlf_bus.config()
        self.entry_tlf_bus.grid(row=0, column=5)

        self.tlf2_bus = tk.StringVar()
        self.entry_tlf2_bus = tk.Entry(self.pes2, textvariable=self.tlf2_bus)
        self.entry_tlf2_bus.config()
        self.entry_tlf2_bus.grid(row=0, column=7)

        """
        self.fax = tk.StringVar()
        self.entry_fax = tk.Entry(self, textvariable=self.fax)
        self.entry_fax.config()
        self.entry_fax.grid(row=0, column=9)
        """

        self.banco_bus = tk.StringVar()
        self.entry_banco_bus = tk.Entry(self.pes2, textvariable=self.banco_bus)
        self.entry_banco_bus.config()
        self.entry_banco_bus.grid(row=1, column=9, pady=10, padx=10)

        self.direcion_bus = tk.StringVar()
        self.entry_direccion_bus = tk.Entry(self.pes2, textvariable=self.direcion_bus)
        self.entry_direccion_bus.config(width=30)
        self.entry_direccion_bus.grid(row=1, column=1, pady=10)

        self.poblacion_bus = tk.StringVar()
        self.entry_poblacion_bus = tk.Entry(self.pes2, textvariable=self.poblacion_bus)
        self.entry_poblacion_bus.config()
        self.entry_poblacion_bus.grid(row=1, column=3, pady=10)

        self.provincia_bus = tk.StringVar()
        self.entry_provincia_bus= tk.Entry(self.pes2, textvariable=self.provincia_bus)
        self.entry_provincia_bus.config()
        self.entry_provincia_bus.grid(row=1, column=5, pady=10)

        self.cp_bus = tk.StringVar()
        self.entry_cp_bus = tk.Entry(self.pes2, textvariable=self.cp_bus)
        self.entry_cp_bus.config()
        self.entry_cp_bus.grid(row=1, column=7, pady=10)

        # Botones
        self.boton_cli_bus = tk.Button(self.pes2, text='Buscar Cliente', command=self.enable_fields_search)
        self.boton_cli_bus.config(width=15, cursor='hand2')
        self.boton_cli_bus.grid(row=2, column=3, pady=10)

        self.boton_buscar_bus = tk.Button(self.pes2, text='Buscar', command=self.search_data)
        self.boton_buscar_bus.config(width=10, cursor='hand2')
        self.boton_buscar_bus.grid(row=2, column=4, pady=10)

        self.boton_guardar_bus = tk.Button(self.pes2, text='Guardar', command=self.save_data_search)
        self.boton_guardar_bus.config(width=10, cursor='hand2')
        self.boton_guardar_bus.grid(row=2, column=5, pady=10)

        self.boton_clean_bus = tk.Button(self.pes2, text='Limpiar', command=self.clean)
        self.boton_clean_bus.config(width=10, cursor='hand2')
        self.boton_clean_bus.grid(row=2, column=6, pady=10)

    def enable_fields_search(self):
        self.entry_nombre_bus.config(state='normal')
        self.entry_cif_bus.config(state='normal')
        self.entry_tlf_bus.config(state='normal')
        self.entry_provincia_bus.config(state='normal')
        self.entry_poblacion_bus.config(state='normal')

        self.boton_clean_bus.config(state='normal')
        self.boton_buscar_bus.config(state='normal')

        if self.id_cliente is not None:
            self.entry_tlf2_bus.config(state='normal')
            self.entry_direccion_bus.config(state='normal')
            self.entry_banco_bus.config(state='normal')
            self.entry_cp_bus.config(state='normal')
            self.boton_guardar_bus.config(state='normal')

    def clean_fields_search(self):
        # Busqueda cliente
        self.nombre_bus.set('')
        self.cif_bus.set('')
        self.tlf_bus.set('')
        self.provincia_bus.set('')
        self.poblacion_bus.set('')

        if self.id_cliente is not None:
            self.tlf2_bus.set('')
            self.cp_bus.set('')
            self.direcion_bus.set('')
            self.banco_bus.set('')

    def disable_fields(self):
        self.clean_fields_search()

        # Busqueda cliente
        self.entry_nombre_bus.config(state='disabled')
        self.entry_cif_bus.config(state='disabled')
        self.entry_tlf_bus.config(state='disabled')
        self.entry_provincia_bus.config(state='disabled')
        self.entry_poblacion_bus.config(state='disabled')

        self.entry_tlf2_bus.config(state='disabled')
        self.entry_direccion_bus.config(state='disabled')
        self.entry_banco_bus.config(state='disabled')
        self.entry_cp_bus.config(state='disabled')

        self.boton_clean_bus.config(state='disabled')
        self.boton_buscar_bus.config(state='disabled')
        self.boton_guardar_bus.config(state='disabled')

    def disable_fields_search(self):
        # Busqueda cliente
        self.entry_tlf2_bus.config(state='disabled')
        self.entry_direccion_bus.config(state='disabled')
        self.entry_banco_bus.config(state='disabled')
        self.entry_cp_bus.config(state='disabled')

        self.boton_guardar_bus.config(state='disabled')

    def delete_table_bus(self):
        self.tabla_bus.delete(*self.tabla_bus.get_children())

    def clean(self):
        self.clean_fields_search()
        self.disable_fields_search()
        self.tabla_bus.delete(*self.tabla_bus.get_children())
        self.id_cliente = None

    def save_data_search(self):
        client = Cliente(
            self.nombre_bus.get(),
            self.cif_bus.get(),
            self.tlf_bus.get(),
            self.tlf2_bus.get(),
            # self.fax.get(),
            self.provincia_bus.get(),
            self.poblacion_bus.get(),
            self.direcion_bus.get(),
            self.cp_bus.get(),
            self.banco_bus.get(),
        )

        edit_client(client, self.id_cliente)
        list_edit(self.tabla_bus, self.id_cliente)

        # Limpiar campos
        self.clean_fields_search()
        self.disable_fields_search()

    def search_data(self):
        self.delete_table_bus()
        client = Cliente(
            self.nombre_bus.get(),
            self.cif_bus.get(),
            self.tlf_bus.get(),
            self.tlf2_bus.get(),
            self.provincia_bus.get(),
            self.poblacion_bus.get(),
            self.direcion_bus.get(),
            self.cp_bus.get(),
            self.banco_bus.get(),
        )

        search_client(client, self.tabla_bus)

    def table_client_search(self):
        self.tabla_bus = ttk.Treeview(self.pes2, columns=('Nombre', 'CIF', 'Telefono', 'Otro telefono', 'Provincia',
                                                 'Población', 'Dirección', 'CP', 'Banco'), show='headings')
        self.tabla_bus.grid(row=4, column=0, columnspan=10, padx=(10, 0), sticky='nse')
        self.scroll_bus = ttk.Scrollbar(self.pes2,
                                    orient='vertical', command=self.tabla_bus.yview)
        self.scroll_bus.grid(row=4, column=10, sticky='nse')
        self.tabla_bus.configure(yscrollcommand=self.scroll_bus.set)
        # self.list_client = list_save()

        self.tabla_bus.heading('#1', text='Nombre', anchor='center')
        self.tabla_bus.column('Nombre', width=100, anchor='center')
        self.tabla_bus.heading('#2', text='CIF')
        self.tabla_bus.column('CIF', width=80, anchor='center')
        self.tabla_bus.heading('#3', text='Telefono')
        self.tabla_bus.column('Telefono', width=150, anchor='center')
        self.tabla_bus.heading('#4', text='Otro telefono')
        self.tabla_bus.column('Otro telefono', width=150, anchor='center')
        self.tabla_bus.heading('#5', text='Provincia')
        self.tabla_bus.column('Provincia', width=125, anchor='center')
        self.tabla_bus.heading('#6', text='Población')
        self.tabla_bus.column('Población', width=125, anchor='center')
        self.tabla_bus.heading('#7', text='Dirección')
        self.tabla_bus.column('Dirección', width=200, anchor='center')
        self.tabla_bus.heading('#8', text='CP')
        self.tabla_bus.column('CP', width=50, anchor='center')
        self.tabla_bus.heading('#9', text='Banco')
        self.tabla_bus.column('Banco', width=100, anchor='center')

        self.boton_editar_bus = tk.Button(self.pes2, text='Editar Cliente', command=self.edit_table_search)
        self.boton_editar_bus.config(width=15, cursor='hand2')
        self.boton_editar_bus.grid(row=5, column=0, pady=10, padx=10, columnspan=2)

        self.boton_borrar_bus = tk.Button(self.pes2, text='Eliminar Cliente')
        self.boton_borrar_bus.config(width=15, cursor='hand2')
        self.boton_borrar_bus.grid(row=5, column=1, pady=10, padx=10, columnspan=3)

    def edit_table_search(self):
        conexion = ConexionDB()
        try:
            self.bus_nombre = self.tabla_bus.item(self.tabla_bus.selection())['values'][0]
            self.bus_cif = self.tabla_bus.item(self.tabla_bus.selection())['values'][1]
            self.bus_tlf = self.tabla_bus.item(self.tabla_bus.selection())['values'][2]
            self.bus_tlf2 = self.tabla_bus.item(self.tabla_bus.selection())['values'][3]
            self.bus_provincia = self.tabla_bus.item(self.tabla_bus.selection())['values'][4]
            self.bus_poblacion = self.tabla_bus.item(self.tabla_bus.selection())['values'][5]
            self.bus_direcion = self.tabla_bus.item(self.tabla_bus.selection())['values'][6]
            self.bus_cp = self.tabla_bus.item(self.tabla_bus.selection())['values'][7]
            self.bus_banco = self.tabla_bus.item(self.tabla_bus.selection())['values'][8]
            sql = f"""SELECT ID_CLIENTE FROM CLIENTE WHERE CIF = '{self.bus_cif}'"""
            conexion.cursor.execute(sql)
            id = conexion.cursor.fetchone()
            self.id_cliente = id[0]

            self.enable_fields_search()
            self.clean_fields_search()

            self.entry_nombre_bus.insert(0, self.bus_nombre)
            self.entry_cif_bus.insert(0, self.bus_cif)
            self.entry_tlf_bus.insert(0, self.bus_tlf)
            self.entry_provincia_bus.insert(0, self.bus_provincia)
            self.entry_poblacion_bus.insert(0, self.bus_poblacion)

            self.entry_tlf2_bus.insert(0, self.bus_tlf2)
            self.entry_direccion_bus.insert(0, self.bus_direcion)
            self.entry_banco_bus.insert(0, self.bus_banco)
            self.entry_cp_bus.insert(0, self.bus_cp)

        except Exception as e:
            print(e)
