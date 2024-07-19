from flask import Flask, request
import Domain.Funcoes_util as en
from Infra.Configs.Conexao_Externa import iniciar_Transacao
import pandas as pd

app = Flask(__name__)
"""
colocar um request pra pegar os dados

"""


@app.route('/iniciar')
def inicar():
    iniciar_Transacao()
    return 'Iniciado'


@app.route('/tabela/Pedido/<string:operacao>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tbpedido(operacao):
    if operacao == 'incluir':
        dados = request.json
        df = pd.DataFrame(dados)
        en.incluir('Pedidos', df)
    elif operacao == 'excluir':
        id = request
        en.excluir('Pedido', id)
    elif operacao == 'atualizar':
        dados = request.json
        df = pd.DataFrame(dados)
        en.atualizar(dados.id, 'Pedido', df)
    else:
        return en.listar_tabela('Pedido')


@app.route('/tabela/Produto/<string:operacao>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tbproduto(operacao):
    if operacao == 'incluir':
        dados = request.json
        df = pd.DataFrame(dados)
        en.incluir('Produtos', df)
    elif operacao == 'excluir':
        id = request
        en.excluir('Produto', id)
    elif operacao == 'atualizar':
        dados = request.json
        df = pd.DataFrame(dados)
        en.atualizar(dados.id, 'Produto', df)
    else:
        return en.listar_tabela('Produto')


@app.route('/tabela/Cliente/<string:operacao>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tbcliente(operacao):
    if operacao == 'incluir':
        dados = request.json
        df = pd.DataFrame(dados)
        en.incluir('Clientes', df)
    elif operacao == 'excluir':
        id = request
        en.excluir('Cliente', id)
    elif operacao == 'atualizar':
        dados = request.json
        df = pd.DataFrame(dados)
        en.atualizar(dados.id, 'Cliente', df)
    else:
        return en.listar_tabela('Cliente')


@app.route('/tabela/Itens_Pedidos/<string:operacao>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tbitens(operacao):
    if operacao == 'incluir':
        dados = request.json
        df = pd.DataFrame(dados)
        en.incluir('Itens_Pedidos', df)
    elif operacao == 'excluir':
        id = request
        en.excluir('Itens_Pedidos', id)
    elif operacao == 'atualizar':
        dados = request.json
        df = pd.DataFrame(dados)
        en.atualizar(dados.id, 'Itens_Pedidos', df)
    else:
        return en.listar_tabela('Itens_Pedidos')


@app.route('/tabela/Movimentacao/<string:operacao>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tbmovimentacao(operacao):
    if operacao == 'incluir':
        dados = request.json
        df = pd.DataFrame(dados)
        en.incluir('Movimentacao', df)
    elif operacao == 'excluir':
        id = request
        en.excluir('Movimentacao', id)
    elif operacao == 'atualizar':
        dados = request.json
        df = pd.DataFrame(dados)
        en.atualizar(dados.id, 'Movimentacao', df)
    else:
        return en.listar_tabela('Movimentacao')


@app.route('/tabela/Compras/<string:operacao>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def tbcompras(operacao):
    if operacao == 'incluir':
        dados = request.json
        df = pd.DataFrame(dados)
        en.incluir('Compras', df)
    elif operacao == 'excluir':
        id = request
        en.excluir('Compras', id)
    elif operacao == 'atualizar':
        dados = request.json
        df = pd.DataFrame(dados)
        en.atualizar(dados.id, 'Compras', df)
    else:
        return en.listar_tabela('Compras')


app.run(port=5000, host='localhost', debug=True)
