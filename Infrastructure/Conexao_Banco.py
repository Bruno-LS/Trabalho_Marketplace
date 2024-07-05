"""
1.Criar a conexao com o banco
2.Iniciar sessão
3.Definir como as demais funções vão interagir com o Banco
4.Exportar conexao
"""
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()
USER_NAME=os.getenv('USER_NAME')
BD_NAME=os.getenv('BD_NAME')
DRIVER_NAME=os.getenv('DRIVER_NAME')


# Conexao Por host
engine = create_engine("mssql+pyodbc://{}/{}?driver={}".format(USER_NAME, BD_NAME, DRIVER_NAME), echo=True)
conexao = engine.connect() #Iniciando conexao
conexao.close()

