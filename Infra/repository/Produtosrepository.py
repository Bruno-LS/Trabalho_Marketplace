from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Produto import Produto
from sqlalchemy import delete, update
import pandas as pd


class ProdutosRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Produto).all()
            return data

    @staticmethod
    def select_id(id: int):
        with DBconnection() as db:
            data = db.session.query(Produto).filter(Produto.ID_Produto == id)
            return data

    @staticmethod
    def incluir(dados):
        with DBconnection() as db:
            tratados = tratarDados(dados)
            produto = Produto(tratados)
            db.session.add(produto)
            db.session.commit()

    @staticmethod
    def excluir(id: int):
        with DBconnection() as db:
            stmt = delete(Produto).where(Produto.ID_Produto == id)
            db.session.execute(stmt)

    @staticmethod
    def atualizar(id: int, dados: pd.DataFrame):
        with DBconnection() as db:
            stmt = (
                update(Produto).
                where(Produto.ID_Produto == id).
                values(
                    Estoque=10,
                    UPC=int(dados.iloc[0]['UPC']),
                    SKU=int(dados.iloc[0]['SKU']),
                    Nome_produto=dados.iloc[0]['Product_Name'],
                    Valor=float(dados.iloc[0]['Amount'])
                )
            )
            db.session.execute(stmt)


def tratarDados(dados):
    return dados
