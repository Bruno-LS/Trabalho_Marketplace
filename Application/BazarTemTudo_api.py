
from flask import Flask, jsonify
import Domain.Funcoes_util as en
from Infra.Configs.Conexao_Externa import iniciar_Transacao

app = Flask(__name__)

@app.route('/')
def oi():
    return (f"Nesta aplicação há as seguintes funcionalidades: "
            f"Select das tabelas no link '/nome_tabela'"
            f"Buscar Id no link '/nome_tabela/id'"
            f"Iniciar Extração de Pedidos no link '/iniciar'"
            f"Remover Linha no link '/tabela/nome_tabela/remover/id'")

"""@app.route('/iniciar')
def inicar():
    return 'iniciar'
    iniciar_Transacao()
"""

@app.route('/tabela/<string:nome_tabela>', methods=['GET'])
def Buscar_Tabela(nome_tabela):
    print(nome_tabela)
    Tabela = en.listar_tabela(nome_tabela)
    return jsonify(Tabela)


@app.route('/tabela/<string:nome_tabela>/<int:id>', methods=['GET'])
def Buscar_ID(nome_tabela, id):
    Linha = en.buscar_id(nome_tabela, id)
    return jsonify(Linha)

#criar
"""@app.route('/tabela/<string:nome_tabela>/remover/<int:id>', methods=['DELETE'])
def Remover(nome_tabela, id):
    status_remo = en.remover(nome_tabela, id)
    return 'Removido Com Sucesso' if status_remo==1 else 'Falha Na Remoção'
"""

app.run(port=5000, host='localhost', debug=True)








