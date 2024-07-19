from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Cliente import Cliente
from sqlalchemy import delete, update
import pandas as pd



class ClientesRepository:


    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Cliente).all()
            return data

    @staticmethod
    def select_id(id: int):
        with DBconnection() as db:
            data = db.session.query(Cliente).filter(Cliente.ID_cliente == id)
            return data

    @staticmethod
    def incluir(dados:pd.DataFrame):
        with DBconnection() as db:
            tratados = tratarDados(dados, db)
            if tratados != 0:
                cliente = Cliente(tratados)
                db.session.add(cliente)
                db.session.commit()

    @staticmethod
    def excluir(id: int):
        with DBconnection() as db:
            stmt = delete(Cliente).where(Cliente.ID_Cliente == id)
            db.session.execute(stmt)

    @staticmethod
    def atualizar(id: int, dados: pd.DataFrame):
        with DBconnection() as db:
            stmt = (
                update(Cliente).
                where(Cliente.ID_Cliente == id).
                values(
                    Nome=dados.iloc[0]['Buyer_Name'],
                    CPF=dados.iloc[0]['Tax_ID'],
                    Email=dados.iloc[0]['Email'],
                    Telefone=dados.iloc[0]['Phone']
                )
            )
            db.session.execute(stmt)


def tratarDados(dados, db):
    cliente = db.session.query(Cliente).where(dados.iloc[0]['Buyer_Name'])
    if cliente:
        return 0
    else:
        return dados

