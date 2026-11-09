from tkinter import *
from tkinter import ttk, messagebox

import numpy as np
import pandas as pd
import openpyxl as xl

# interface


class Calculadora_lucro:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculadora de Lucro")
        self.root.geometry("1100x650")
        self.root.resizable(False, False)

        # variaveis

        self.color_green = "#176B58"
        self.color_yellow = "#D9A441"
        self.color_branco = "#F8FAF9"
        self.color_text = "#25342F"

        # executa a criacao dos containers

        self.containers()
        self.intens_container01()
        self.root.mainloop()

    def containers(self):
        self.fr_container01 = Frame(self.root, width=1050, height=30)
        self.fr_container02 = Frame(self.root, width=1050, height=250)
        self.fr_container03 = Frame(
            self.root, width=1050, height=370, bg=self.color_green
        )

        # Posicionar os elementos

        self.fr_container01.pack_propagate(False)
        self.fr_container02.pack_propagate(False)
        self.fr_container03.pack_propagate(False)
        self.fr_container01.pack()
        self.fr_container02.pack()
        self.fr_container03.pack()

        # Itens do container 01

    def intens_container01(self):
        self.lb_title = Label(
            self.fr_container01,
            text="Calculadora de Lucro",
            font="Verdana 20",
            bg=self.fr_container01.cget("bg"),
        )
        self.lb_title.pack()


Calculadora_lucro()
