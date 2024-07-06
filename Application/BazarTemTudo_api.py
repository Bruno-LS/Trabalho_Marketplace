
from flask import Flask, jsonify, request
import Application.Endpoints as en
from Infrastructure.Conexao_Externa import iniciar_Transacao

app = Flask(__name__)

@app.route('/')
def oi():
    return (f"Nesta aplicação há as seguintes funcionalidades: "
            f"Select das tabelas no link '/nome_tabela'"
            f"Buscar Id no link '/nome_tabela/id'"
            f"Buscar pelo Nome do Item no link '/nome_tabela/nome'"
            f"Iniciar Extração de Pedidos no link '/iniciar'")

@app.route('/iniciar')
def inicar():
    return 'iniciar'
    iniciar_Transacao()

@app.route('/tabela/<String:nome_tabela>')
def Buscar_Tabela(nome_tabela):
    Tabela = en.Listar_tabela(nome_tabela)
    return jsonify(Tabela)

@app.route('/tabela/<String:nome_tabela>/<int:id>', methods=['GET'])
def Buscar_ID(nome_tabela, id):
    Linha = en.buscarP_id(nome_tabela, id)
    return jsonify(Linha)

@app.route('/tabela/<String:nome_tabela>/<String:nome>', methods=['GET'])
def Buscar_Nome(nome_tabela, nome):
    Linha = en.buscarP_nome(nome_tabela, nome)
    return jsonify(Linha)

@app.route('/tabela/<String:nome_tabela>/remover/<String:senha>/<int:id>', methods=['DELETE'])
def Remover(nome_tabela, senha, id):
    status_remo = en.remover(nome_tabela, senha, id)
    return 'Removido Com Sucesso' if status_remo==1 else 'Falha Na Remoção'

"""
Talvez colocar o resto do CRUD (inserir, alterar) - @app.route('/<nome_tabela>/operacao/') POST/PUT
"""

app.run(port=5000, host='localhost', debug=True)








