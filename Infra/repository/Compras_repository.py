from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Compras import Compras
from Infra.Entities.Produto import Produto
from Infra.Entities.Itens_Pedidos import ItensPedido
from Infra.Entities.Movimentacao import Movimentacao

from sqlalchemy import delete, update
import pandas as pd


class ComprasRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Compras).all()
            return data


    @staticmethod
    def select_id(id):
        with DBconnection() as db:
            data = db.session.query(Compras).filter(Compras.ID_Produto == id)
            return data

    @staticmethod
    def incluir(dados):
        with DBconnection() as db:
            tratados = tratarDados(db)
            compras = Compras(tratados)
            db.session.add(compras)
            db.session.commit()

    @staticmethod
    def excluir(id: int):
        with DBconnection() as db:
            stmt = delete(Compras).where(Compras.ID_Compras == id)
            db.session.execute(stmt)

    @staticmethod
    def atualizar(id: int, dados: pd.DataFrame):
        with DBconnection() as db:
            stmt = (
                update(Compras).
                where(Compras.ID_Produto == id).
                values(
                    Nome_produto=dados.iloc[0]['Product_Name'],
                    Quant=dados.iloc[0]['Quantity']
                )
            )
            db.session.execute(stmt)


def tratarDados(db):
    pr = Produto.__table__
    mo = Movimentacao.__table__
    it = ItensPedido.__table__

    # consulta
    query = db.session.query(
        pr.c.ID_Produto,
        pr.c.Nome_produto,
        it.c.Quant
    ).join(
        mo, pr.c.ID_Produto == mo.c.ID_Produto
    ).join(
        it, mo.c.ID_Produto == it.c.ID_Produto
    ).filter(
        mo.c.STATUS_Pedido == 'N'
    ).distinct()

    results = query.all()

    data = [
        {
            'ID_Produto': result.ID_Produto,
            'Nome_produto': result.Nome_produto,
            'Quant': result.Quant
        }
        for result in results
    ]
    df = pd.DataFrame(data)

    return df

