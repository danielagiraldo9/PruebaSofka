#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk, messagebox
from .ventanaJuego import VentanaJuego
from models.engine.fileStorage import FileStorage

storage = FileStorage()


class Register(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('400x170')
        self.title('Register')
        self.resizable(0,0)
        # configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self.crear_ventana()

    # Definir el método crear_componentes
    def crear_ventana(self):
        # nombre y apellido
        nombre_usuario = ttk.Label(self, text='Nombre:')
        nombre_usuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.nombre_entrada = ttk.Entry(self)
        self.nombre_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        apellido_usuario = ttk.Label(self, text='Apellido:')
        apellido_usuario.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.apellido_entrada = ttk.Entry(self)
        self.apellido_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        password_etiqueta = ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # boton register
        register_boton = ttk.Button(self, text='Register', command=self.register)
        register_boton.grid(row=4, column=0, columnspan=2)

        Register.mainloop(self)


    def register(self):
        """
        Este metodo registra los datos en el
        archivo json(base de datos)
        """
        # creo un objeto con los datos
        obj = {}
        obj['nombre'] = (self.nombre_entrada.get())
        obj['apellido'] = (self.apellido_entrada.get())
        obj['usuario'] = (self.usuario_entrada.get())
        obj['password'] = (self.password_entrada.get())

        storage.new(obj)
        storage.save()
        self.quit()
        self.destroy()
        juego = VentanaJuego()
