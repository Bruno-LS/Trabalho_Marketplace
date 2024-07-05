"""
1.Iniciar o app
2.Tratar as entradas e saidas
3.Chamar as funções corretas para as funcionalidades desejadas
"""
from flask import Flask
#import Application.Endpoints

app = Flask(__name__)

@app.route('/')
def oi():
    return (f"Nesta aplicação há as seguintes funcionalidades: "
            f"Select das tabelas no link '/nome_tabela'"
            f"Buscar Id no link '/nome_tabela/id'"
            f"Buscar pelo Nome do Item no link '/nome_tabela/nome'"
            f"Iniciar Extração de Pedidos no link '/iniciar'")


"""
Criar endpoint que da select nas tabelas - @app.route('/<nome_tabela>')
Criar endpoint de buscar pelo id na respectiva tabela - @app.route('/<nome_tabela>/id')
Criar endpoint de buscar pelo nome na respectiva tabela - @app.route('/<nome_tabela>/nome')
Talvez colocar o resto do CRUD (inserir, remover, alterar) - @app.route('/<nome_tabela>') POST/PUT
Criar uma que ativa a api externa e inicia o processo de jogar no banco - @app.route('/iniciar')
"""

app.run(port=5000, host='localhost', debug=True)








