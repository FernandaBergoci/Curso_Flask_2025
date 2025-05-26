import os
os.system('cls')

# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")

# Rota Raiz
@app.route("/")
def ola_mundo():
    #Criar uma variável com meu nome
    nome = "Fernanda"
    produtos=[
        {"nome": "Ração", "preco": 261.00},
        {"nome": "Playstation", "preco": 2500.00}
    ]
    return render_template("alo.html", n=nome, aProdutos=produtos), 200

# Nova Rota Teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel=""):
    return "Nova rota teste<br>Variável: {}".format(variavel), 200
app.run()