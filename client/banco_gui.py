import tkinter as tk
from tkinter import ttk
from model.bank import Banco, save_data_bank


class Frame_Banco(tk.Frame):
    def __init__(self, root=None, pes=None):
        super().__init__(root)
        self.root = root
        self.id_cliente = None
        self.pes3 = pes
        self.properties_bank()

        self.disable_fields()

        self.table_bank()

    def properties_bank(self):
        # Labels datos del banco
        self.label_nombre_bnk = tk.Label(self.pes3, text='Nombre:')
        self.label_nombre_bnk.grid(row=0, column=0, padx=10, pady=10)

        self.label_direccion_bnk = tk.Label(self.pes3, text='Dirección:')
        self.label_direccion_bnk.grid(row=1, column=0, pady=10)

        self.label_cif_bnk = tk.Label(self.pes3, text='CIF:')
        self.label_cif_bnk.grid(row=0, column=2, pady=10)

        self.label_tlf_bnk = tk.Label(self.pes3, text='Telefono/Movil:')
        self.label_tlf_bnk.grid(row=1, column=2, pady=10)

        # Entrys de los datos
        self.nombre_bnk = tk.StringVar()
        self.entry_nombre_bnk = tk.Entry(self.pes3, textvariable=self.nombre_bnk)
        self.entry_nombre_bnk.config(width=30)
        self.entry_nombre_bnk.grid(row=0, column=1)

        self.cif_bnk = tk.StringVar()
        self.entry_cif_bnk = tk.Entry(self.pes3, textvariable=self.cif_bnk)
        self.entry_cif_bnk.config()
        self.entry_cif_bnk.grid(row=0, column=3)

        self.tlf_bnk = tk.StringVar()
        self.entry_tlf_bnk = tk.Entry(self.pes3, textvariable=self.tlf_bnk)
        self.entry_tlf_bnk.config()
        self.entry_tlf_bnk.grid(row=1, column=3)

        self.direcion_bnk = tk.StringVar()
        self.entry_direccion_bnk = tk.Entry(self.pes3, textvariable=self.direcion_bnk)
        self.entry_direccion_bnk.config(width=30)
        self.entry_direccion_bnk.grid(row=1, column=1, pady=10)

        # Botones
        self.boton_nuevo_bnk = tk.Button(self.pes3, text='Crear Banco', command=self.enable_fields)
        self.boton_nuevo_bnk.config(width=15, cursor='hand2')
        self.boton_nuevo_bnk.grid(row=2, column=0, pady=10, padx=10)

        self.boton_guardar_bnk = tk.Button(self.pes3, text='Guardar', command=self.save_data_bank)
        self.boton_guardar_bnk.config(width=10, cursor='hand2')
        self.boton_guardar_bnk.grid(row=2, column=1, pady=10)

        self.boton_cancelar_bnk = tk.Button(self.pes3, text='Cancelar', command=self.clean_fields)
        self.boton_cancelar_bnk.config(width=10, cursor='hand2')
        self.boton_cancelar_bnk.grid(row=2, column=2, pady=10)

    def enable_fields(self):
        self.entry_nombre_bnk.config(state='normal')
        self.entry_cif_bnk.config(state='normal')
        self.entry_tlf_bnk.config(state='normal')
        self.entry_direccion_bnk.config(state='normal')
        self.boton_cancelar_bnk.config(state='normal')
        self.boton_guardar_bnk.config(state='normal')

    def clean_fields(self):
        # Banco nuevo
        self.nombre_bnk.set('')
        self.cif_bnk.set('')
        self.tlf_bnk.set('')
        self.direcion_bnk.set('')

    def disable_fields(self):
        self.clean_fields()

        # Banco cliente
        self.entry_nombre_bnk.config(state='disabled')
        self.entry_cif_bnk.config(state='disabled')
        self.entry_tlf_bnk.config(state='disabled')
        self.entry_direccion_bnk.config(state='disabled')

        self.boton_cancelar_bnk.config(state='disabled')
        self.boton_guardar_bnk.config(state='disabled')

    def save_data_bank(self):
        banco = Banco(
            self.nombre_bnk.get(),
            self.cif_bnk.get(),
            self.tlf_bnk.get(),
            self.direcion_bnk.get()
        )

        save_data_bank(banco, self.tabla)

        # Limpiar campos
        self.clean_fields()

    def table_bank(self):
        self.tabla = ttk.Treeview(self.pes3, columns=('Nombre', 'CIF', 'Telefono', 'Dirección'), show='headings')
        self.tabla.grid(row=4, column=0, columnspan=4, padx=(10, 0), sticky='nse')
        self.scroll = ttk.Scrollbar(self.pes3, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=10, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)
        # self.list_client = list_save()

        self.tabla.heading('#1', text='Nombre', anchor='center')
        self.tabla.column('Nombre', width=100, anchor='center')
        self.tabla.heading('#2', text='CIF')
        self.tabla.column('CIF', width=80, anchor='center')
        self.tabla.heading('#3', text='Telefono')
        self.tabla.column('Telefono', width=150, anchor='center')
        self.tabla.heading('#4', text='Dirección')
        self.tabla.column('Dirección', width=200, anchor='center')
