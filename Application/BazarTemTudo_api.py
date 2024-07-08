from flask import Flask, jsonify
import Domain.Funcoes_util as en
from Infra.Configs.Conexao_Externa import iniciar_Transacao

app = Flask(__name__)

@app.route('/')
def oi():
    return (f"Routes: "
            f" /iniciar "
            f" /tabela/<nome_tabela> "
            f" /tabela/<nome_tabela>/<id>")

@app.route('/iniciar')
def inicar():
    iniciar_Transacao()
    return 'Iniciado'



@app.route('/tabela/<string:nome_tabela>', methods=['GET'])
def Buscar_Tabela(nome_tabela):
    tabela = en.listar_tabela(nome_tabela)
    return tabela


@app.route('/tabela/<string:nome_tabela>/<int:id>', methods=['GET'])
def Buscar_ID(nome_tabela, id):
    linha = en.buscar_id(nome_tabela, id)
    return linha



app.run(port=5000, host='localhost', debug=True)








