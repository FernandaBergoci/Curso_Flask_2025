import os
os.system('cls')

# coding: utf-8
from flask import Flask, render_template, request
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

# Rota formulário
@app.route("/form")
def form():
    return render_template("form.html"), 200

# Rota tratamento do formulário
@app.route("/form_recebe", methods = ["GET","POST"])
def form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamar direto no GET",200


app.run()