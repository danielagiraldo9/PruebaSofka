#!/usr/bin/env python3
"""Importaciones"""
import csv
import sys
import json
import tkinter as tk
from tkinter import ttk, messagebox


class VentanaJuego(tk.Tk):
    """
    Esta clase contiene los atrubutos y metodos
    Para crear la interfaz gráfica del juego
    """

    # atributos de clase
    respuestas = [('1', 'c'), ('2', 'b'), ('3', 'a'), ('4', 'd'), ('5', 'd')]

    def __init__(self):
        super().__init__()
        # ventana principal
        self.geometry('600x400')
        self.title('DIVIERTETE Y GANA!')
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=3)
        self.rowconfigure(3, weight=3)
        self.rowconfigure(4, weight=3)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self._crear_componentes()

    # Definir el método crear_componentes
    def _crear_componentes(self):
        """
        Crea la tabla para interactuar
        """

        level = 0
        # abrimos el archivo con las preguntas
        with open('files/preguntas.csv') as f:
            reader = csv.reader(f)
            for i in reader:
                # declaramos variables de nivel
                level += 1
                # Etiqueta Nivel y acumulado
                if (level == 1):
                    nivel = ttk.Label(self, text="NIVEL 1")
                    nivel.grid(row=0, column=0, sticky='NSEW')
                    acumulado = ttk.Label(self, text="PREMIO ACUMULADO: 0 USD")
                    acumulado.grid(row=0, column=1, sticky='NSEW')
                elif (level == 2):
                    nivel = ttk.Label(self, text="Nivel 2")
                    nivel.grid(row=0, column=0, sticky='NSEW')
                    premio = ttk.Label(self, text="PREMIO ACUMULADO: 300 USD")
                    premio.grid(row=0, column=1, sticky='NSEW')
                elif (level == 3):
                    nivel = ttk.Label(self, text="Nivel 3")
                    nivel.grid(row=0, column=0, sticky='NSEW')
                    prmio = ttk.Label(self, text="PREMIO ACUMULADO: 1.000 USD")
                    prmio.grid(row=0, column=1, sticky='NSEW')
                elif (level == 4):
                    nivel = ttk.Label(self, text="Nivel 4")
                    nivel.grid(row=0, column=0, sticky='NSEW')
                    prmio = ttk.Label(self, text="PREMIO ACUMULADO: 5.000 USD")
                    prmio.grid(row=0, column=1, sticky='NSEW')
                elif (level == 5):
                    nivel = ttk.Label(self, text="Nivel 5")
                    nivel.grid(row=0, column=0, sticky='NSEW')
                    pmio = ttk.Label(self, text="PREMIO ACUMULADO: 20.000 USD")
                    pmio.grid(row=0, column=1, sticky='NSEW')

                # Etiqueta Pregunta
                pregunta = ttk.Label(self, text=i[1], width=50)
                pregunta.grid(row=1, column=0, columnspan=2, sticky='NS')

                # Botones respuesta
                a = ttk.Button(self, text='A. ' + i[2],
                               command=lambda n=i[0],
                               m="a": self.which_button(n, m))
                a.grid(row=2, column=0, sticky='NSEW')
                b = ttk.Button(self, text='B. ' + i[3],
                               command=lambda n=i[0],
                               m="b": self.which_button(n, m))
                b.grid(row=2, column=1, sticky='NSEW')
                c = ttk.Button(self, text='C. ' + i[4],
                               command=lambda n=i[0],
                               m="c": self.which_button(n, m))
                c.grid(row=3, column=0, sticky='NSEW')
                d = ttk.Button(self, text='D. ' + i[5],
                               command=lambda n=i[0],
                               m="d": self.which_button(n, m))
                d.grid(row=3, column=1, sticky='NSEW')

                # Botón de retirada
                sale = ttk.Button(self, text='Retirarse', command=self.salir)
                sale.grid(row=4, column=1, sticky='NSEW')

                VentanaJuego.mainloop(self)

    def salir(self):
        """
        Programa el boton para retirarse del juego
        """
        self.quit()
        messagebox.showinfo('Mensaje informativo', "te vas con el acumulado")
        self.destroy()
        sys.exit()

    def which_button(self, arg1, arg2):
        tupla1 = tuple(arg1)
        tupla2 = tuple(arg2)
        tupla = tupla1 + tupla2
        if tupla in VentanaJuego.respuestas:
            messagebox.showinfo('Mensaje informativo', "Acertaste")
            VentanaJuego.quit(self)
        else:
            messagebox.showinfo('Mensaje informativo', "Lo siento :( Perdiste")
            self.quit()
            self.destroy()
            sys.exit()
