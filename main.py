from tkinter import *
from tkinter import ttk, messagebox

import numpy as np
import pandas as pd
import openpyxl as xl
import customtkinter as ctk


class Calculadora_lucro:
    def __init__(self):
        # Janela principal
        self.root = Tk()
        self.root.title("Calculadora de Lucro")
        self.root.geometry("1100x650")
        self.root.resizable(False, False)

        # Cores
        self.color_green = "#176B58"
        self.color_yellow = "#D9A441"
        self.color_branco = "#F8FAF9"
        self.color_text = "#25342F"

        # Criar containers e elementos
        self.containers()
        self.intens_container01()
        self.itens_container02()

        # Manter a janela aberta
        self.root.mainloop()

    def containers(self):
        # Três containers principais
        self.fr_container01 = Frame(self.root, width=1050, height=40)

        self.fr_container02 = Frame(self.root, width=1050, height=400)

        self.fr_container03 = Frame(
            self.root, width=1050, height=210, bg=self.color_green
        )

        # Manter as dimensões
        self.fr_container01.pack_propagate(False)
        self.fr_container02.pack_propagate(False)
        self.fr_container03.pack_propagate(False)

        # Posicionar os containers
        self.fr_container01.pack()
        self.fr_container02.pack()
        self.fr_container03.pack()

    def intens_container01(self):
        # Título principal
        self.lb_title = Label(
            self.fr_container01,
            text="Calculadora de Lucro",
            font="Verdana 20",
            bg=self.fr_container01.cget("bg"),
        )

        self.lb_title.pack()

    def itens_container02(self):
        # Três subcontainers
        self.fr_subcontainer01 = Frame(
            self.fr_container02,
            bg="white",
            highlightthickness=1,
            highlightbackground=self.color_text,
        )

        self.fr_subcontainer02 = Frame(
            self.fr_container02,
            bg="white",
            highlightthickness=1,
            highlightbackground=self.color_text,
        )

        self.fr_subcontainer03 = Frame(
            self.fr_container02,
            bg="white",
            highlightthickness=1,
            highlightbackground=self.color_text,
        )

        # Container dos botões
        self.fr_container_btn = Frame(
            self.fr_subcontainer01, bg=self.fr_subcontainer01.cget("bg")
        )

        # Título do cadastro
        self.lb_title_section01 = Label(
            self.fr_subcontainer01,
            text="Cadastro de Produtos",
            font="Verdana 15",
            bg=self.fr_subcontainer01.cget("bg"),
        )

        # Nome do produto
        self.lb_nome_produto = Label(
            self.fr_subcontainer01,
            text="Produto *",
            font="Verdana",
            bg=self.fr_subcontainer01.cget("bg"),
        )

        self.en_nome_produto = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg=self.fr_container01.cget("bg"),
        )

        # Quantidade
        self.lb_qtd_produto = Label(
            self.fr_subcontainer01,
            text="Quantidade do Produto *",
            font="Verdana",
            bg=self.fr_subcontainer01.cget("bg"),
        )

        self.en_qtd_produto = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg=self.fr_container01.cget("bg"),
        )

        # Preço de compra
        self.lb_preco_compra = Label(
            self.fr_subcontainer01,
            text="Preço de Compra *",
            font="Verdana",
            bg=self.fr_subcontainer01.cget("bg"),
        )

        self.en_preco_compra = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg=self.fr_container01.cget("bg"),
        )

        # Preço de venda
        self.lb_preco_venda = Label(
            self.fr_subcontainer01,
            text="Preço de Venda *",
            font="Verdana",
            bg=self.fr_subcontainer01.cget("bg"),
        )

        self.en_preco_venda = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg=self.fr_container01.cget("bg"),
        )

        # Custo de frete
        self.lb_custo_frete = Label(
            self.fr_subcontainer01,
            text="Custo de Frete *",
            font="Verdana",
            bg=self.fr_subcontainer01.cget("bg"),
        )

        self.en_custo_frete = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg=self.fr_container01.cget("bg"),
        )

        # Custo adicional
        self.lb_custo_adicional = Label(
            self.fr_subcontainer01,
            text="Custo Adicional *",
            font="Verdana",
            bg=self.fr_subcontainer01.cget("bg"),
        )

        self.en_custo_adicional = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg=self.fr_container01.cget("bg"),
        )

        # Botão Calcular - azul
        self.btn_calcular = ctk.CTkButton(
            self.fr_container_btn,
            text="Calcular",
            fg_color="#0097b2",
            text_color="white",
            command=None,
        )

        # Botão Salvar - verde
        self.btn_salvar = ctk.CTkButton(
            self.fr_container_btn,
            text="Salvar",
            fg_color=self.color_green,
            text_color="white",
            command=None,
        )

        # Botão Delete - vermelho
        self.btn_deletar = ctk.CTkButton(
            self.fr_container_btn,
            text="Delete",
            fg_color="red",
            text_color="white",
            command=None,
        )

        # Posicionar os subcontainers
        self.fr_subcontainer01.grid(row=0, column=0, padx=10, pady=7, sticky=N)

        self.fr_subcontainer02.grid(row=0, column=1, padx=10, pady=7, sticky=N)

        self.fr_subcontainer03.grid(row=0, column=2, padx=10, pady=7, sticky=N)

        # Posicionar campos do cadastro
        self.lb_title_section01.grid(row=0, columnspan=2, pady=10)

        self.lb_nome_produto.grid(row=1, column=0, pady=5, padx=5, sticky=W)
        self.en_nome_produto.grid(row=1, column=1, padx=5, sticky=W)

        self.lb_qtd_produto.grid(row=2, column=0, pady=5, padx=5, sticky=W)
        self.en_qtd_produto.grid(row=2, column=1, padx=5, sticky=W)

        self.lb_preco_compra.grid(row=3, column=0, pady=5, padx=5, sticky=W)
        self.en_preco_compra.grid(row=3, column=1, padx=5, sticky=W)

        self.lb_preco_venda.grid(row=4, column=0, pady=5, padx=5, sticky=W)
        self.en_preco_venda.grid(row=4, column=1, padx=5, sticky=W)

        self.lb_custo_frete.grid(row=5, column=0, pady=5, padx=5, sticky=W)
        self.en_custo_frete.grid(row=5, column=1, padx=5, sticky=W)

        self.lb_custo_adicional.grid(row=6, column=0, pady=5, padx=5, sticky=W)
        self.en_custo_adicional.grid(row=6, column=1, padx=5, sticky=W)

        # Posicionar o container dos botões
        self.fr_container_btn.grid(row=7, column=0, columnspan=2, pady=10)

        # Posicionar os botões lado a lado
        self.btn_salvar.grid(row=0, column=0, padx=5)

        self.btn_calcular.grid(row=0, column=1, padx=5)

        self.btn_deletar.grid(row=0, column=2, padx=5)


# Iniciar o programa
Calculadora_lucro()
