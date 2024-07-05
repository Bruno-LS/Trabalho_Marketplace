"""
1.Iniciar o app
2.Tratar as entradas e saidas
3.Chamar as funções corretas para as funcionalidades desejadas
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def oi():
    return "Oi"


"""
1.Criar uma clase CRUD, com os metodos como endpoints
2.Criar endpoint que da select nas tabelas 
3.Criar endpoint de buscar pelo id na respectiva tabela
4.Talvez colocar o resto do CRUD (inserir, remover, alterar)
5.Criar uma que ativa a api externa e inicia o processo de jogar no banco
"""

app.run(port=5000, host='localhost', debug=True)

