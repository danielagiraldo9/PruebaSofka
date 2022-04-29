import tkinter as tk
from tkinter import ttk, messagebox
from models.register import Register
from models.ventanaJuego import VentanaJuego
from .engine.fileStorage import FileStorage

storage = FileStorage()


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('300x130')
        self.title('Login')
        self.resizable(0,0)
        # configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # Creamos los componentes
        self.crearComponentes()

    # Definir el método crear_componentes
    def crearComponentes(self):
        # usuario
        usuario_etiqueta = ttk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.usuario_entrada = ttk.Entry(self)
        self.usuario_entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # password
        password_etiqueta = ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.password_entrada = ttk.Entry(self, show='*')
        self.password_entrada.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # boton Login
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)

        # boton register
        register_boton = ttk.Button(self, text='Register', command=self.register)
        register_boton.grid(row=4, column=0, columnspan=2)

        Login.mainloop(self)


    def _login(self):
        """
        Este metodo verifica si el usuario esta en la
        base de datos, y le permite el ingreso al juego
        """
        usuario = self.usuario_entrada.get()
        clave = self.password_entrada.get()
        dic = storage.all()
        if dic == None:
            messagebox.showinfo('Mensaje', 'usuario no existe, por favor registrese')
        else:
            for values in dic.values():
                if values['usuario'] == usuario and values['password'] == clave:
                    self.quit()
                    self.destroy()
                    ventana = VentanaJuego()
            else:
                messagebox.showinfo('Mensaje', 'usuario o clave incorrectas')

    
    def register(self):
        """me lleva a la ventana de registro"""
        self.quit()
        self.destroy()
        registrar = Register()

# Ejecutar la ventana
if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()