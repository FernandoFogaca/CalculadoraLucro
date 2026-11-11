
from tkinter import *
from tkinter import ttk, messagebox
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
        self.fr_container01 = Frame(
            self.root, width=1050, height=40
        )

        self.fr_container02 = Frame(
            self.root, width=1050, height=400
        )

        self.fr_container03 = Frame(
            self.root,
            width=1050,
            height=210,
            bg=self.color_green
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
            bg=self.fr_container01.cget("bg")
        )

        self.lb_title.pack()

    def itens_container02(self):
        # Três subcontainers
        self.fr_subcontainer01 = Frame(
            self.fr_container02,
            bg="white",
            highlightthickness=1,
            highlightbackground=self.color_text
        )

        self.fr_subcontainer02 = Frame(
            self.fr_container02,
            bg="white",
            highlightthickness=1,
            highlightbackground=self.color_text
        )

        self.fr_subcontainer03 = Frame(
            self.fr_container02,
            bg="white",
            highlightthickness=1,
            highlightbackground=self.color_text
        )

        # Container dos botões
        self.fr_container_btn = Frame(
            self.fr_subcontainer01,
            bg="white"
        )

        # Título do cadastro
        self.lb_title_section01 = Label(
            self.fr_subcontainer01,
            text="Cadastro de Produtos",
            font="Verdana 15",
            bg="white"
        )

        # Nome do produto
        self.lb_nome_produto = Label(
            self.fr_subcontainer01,
            text="Produto *",
            font="Verdana",
            bg="white"
        )

        self.en_nome_produto = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            width=18,
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg="white"
        )

        # Quantidade
        self.lb_qtd_produto = Label(
            self.fr_subcontainer01,
            text="Quantidade do Produto *",
            font="Verdana",
            bg="white"
        )

        self.en_qtd_produto = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            width=18,
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg="white"
        )

        # Preço de compra
        self.lb_preco_compra = Label(
            self.fr_subcontainer01,
            text="Preço de Compra *",
            font="Verdana",
            bg="white"
        )

        self.en_preco_compra = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            width=18,
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg="white"
        )

        # Preço de venda
        self.lb_preco_venda = Label(
            self.fr_subcontainer01,
            text="Preço de Venda *",
            font="Verdana",
            bg="white"
        )

        self.en_preco_venda = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            width=18,
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg="white"
        )

        # Custo de frete
        self.lb_custo_frete = Label(
            self.fr_subcontainer01,
            text="Custo de Frete *",
            font="Verdana",
            bg="white"
        )

        self.en_custo_frete = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            width=18,
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg="white"
        )

        # Custo adicional
        self.lb_custo_adicional = Label(
            self.fr_subcontainer01,
            text="Custo Adicional *",
            font="Verdana",
            bg="white"
        )

        self.en_custo_adicional = Entry(
            self.fr_subcontainer01,
            font="Verdana",
            width=18,
            highlightthickness=1,
            highlightbackground=self.color_text,
            highlightcolor=self.color_green,
            bg="white"
        )

        # Botão Calcular
        self.btn_calcular = ctk.CTkButton(
            self.fr_container_btn,
            text="Calcular",
            width=90,
            height=30,
            fg_color="#0097b2",
            text_color="white",
            command=None
        )

        # Botão Salvar
        self.btn_salvar = ctk.CTkButton(
            self.fr_container_btn,
            text="Salvar",
            width=90,
            height=30,
            fg_color=self.color_green,
            text_color="white",
            command=None
        )

        # Botão Delete
        self.btn_deletar = ctk.CTkButton(
            self.fr_container_btn,
            text="Delete",
            width=90,
            height=30,
            fg_color="red",
            text_color="white",
            command=None
        )

        # Título da operação
        self.lb_title_section02 = Label(
            self.fr_subcontainer02,
            text="Operação:",
            font="Verdana 15",
            bg="white"
        )

        # Texto explicativo
        self.lb_text_resultado_operacao = Label(
            self.fr_subcontainer02,
            text="O resultado aparecerá aqui assim que calcular um produto",
            font="Verdana",
            wraplength=250,
            justify=LEFT,
            bg="white"
        )

        # Título lucro líquido
        self.lb_title_lucro_liquido = Label(
            self.fr_subcontainer02,
            text="Lucro líquido",
            font=("Verdana", 12,'bold'),
            bg="white"
        )

        # Resultado lucro líquido
        self.lb_title_resultado_liquido = Label(
            self.fr_subcontainer02,
            text="R$ 00,00",
            font="Verdana",
            width=25,
            padx=5,
            relief="solid",
            borderwidth=1,
            bg="white"
        )

        # Título margem de lucro
        self.lb_title_margem_lucro = Label(
            self.fr_subcontainer02,
            text="Margem de Lucro",
            font="Verdana",
            bg="white"
        )

        # Resultado margem de lucro
        self.lb_resultado_margem_lucro = Label(
            self.fr_subcontainer02,
            text="0,00%",
            font="Verdana",
            width=25,
            padx=5,
            relief="solid",
            borderwidth=1,
            bg="white"
        )

        # Posicionar os subcontainers
        self.fr_subcontainer01.grid(
            row=0, column=0, padx=10, pady=7, sticky=N
        )

        self.fr_subcontainer02.grid(
            row=0, column=1, padx=10, pady=7, sticky=N
        )

        self.fr_subcontainer03.grid(
            row=0, column=2, padx=10, pady=7, sticky=N
        )

        # Posicionar campos do cadastro
        self.lb_title_section01.grid(
            row=0, columnspan=2, pady=10
        )

        self.lb_nome_produto.grid(
            row=1, column=0, pady=5, padx=5, sticky=W
        )
        self.en_nome_produto.grid(
            row=1, column=1, padx=5, sticky=E
        )

        self.lb_qtd_produto.grid(
            row=2, column=0, pady=5, padx=5, sticky=W
        )
        self.en_qtd_produto.grid(
            row=2, column=1, padx=5, sticky=E
        )

        self.lb_preco_compra.grid(
            row=3, column=0, pady=5, padx=5, sticky=W
        )
        self.en_preco_compra.grid(
            row=3, column=1, padx=5, sticky=E
        )

        self.lb_preco_venda.grid(
            row=4, column=0, pady=5, padx=5, sticky=W
        )
        self.en_preco_venda.grid(
            row=4, column=1, padx=5, sticky=E
        )

        self.lb_custo_frete.grid(
            row=5, column=0, pady=5, padx=5, sticky=W
        )
        self.en_custo_frete.grid(
            row=5, column=1, padx=5, sticky=E
        )

        self.lb_custo_adicional.grid(
            row=6, column=0, pady=5, padx=5, sticky=W
        )
        self.en_custo_adicional.grid(
            row=6, column=1, padx=5, sticky=E
        )

        # Container dos botões
        self.fr_container_btn.grid(
            row=7, column=0, columnspan=2, pady=10
        )

        # Botões lado a lado
        self.btn_salvar.grid(row=0, column=0, padx=5)
        self.btn_calcular.grid(row=0, column=1, padx=5)
        self.btn_deletar.grid(row=0, column=2, padx=5)

        # Posicionamento do subcontainer 02
        self.lb_title_section02.grid(
            row=0, column=0,  pady=10
        )

        self.lb_text_resultado_operacao.grid(
            row=1, column=0, padx=10, pady=30
        )

        self.lb_title_lucro_liquido.grid(
            row=2, column=0
        )

        self.lb_title_resultado_liquido.grid(
            row=3, column=0, padx=5, pady=5
        )

        self.lb_title_margem_lucro.grid(
            row=4, column=0
        )

        self.lb_resultado_margem_lucro.grid(
            row=5, column=0, padx=5, pady=(0, 60)
        )


# Iniciar o programa
Calculadora_lucro()
