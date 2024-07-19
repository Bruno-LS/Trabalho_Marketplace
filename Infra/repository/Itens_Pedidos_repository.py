from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Itens_Pedidos import ItensPedido
from sqlalchemy import delete, update
from sqlalchemy.orm import aliased
import pandas as pd





class ItensPedidoRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(ItensPedido).all()
            return data

    @staticmethod
    def incluir(dados):
        with DBconnection() as db:
            tratados = tratarDados(dados, db)
            itensPedido = ItensPedido(tratados)
            db.session.add(itensPedido)
            db.session.commit()

    @staticmethod
    def excluir(id: int):
        with DBconnection() as db:
            stmt = delete(ItensPedido).where(ItensPedido.ID_ItensPedido == id)
            db.session.execute(stmt)

    @staticmethod
    def atualizar(id: int, dados: pd.DataFrame):
        with DBconnection() as db:
            stmt = (
                update(ItensPedido).
                where(ItensPedido.ID_Pedido == id).
                values(
                    Quant=int(dados.iloc[0]['Quantity'])
                )
            )
            db.session.execute(stmt)


def tratarDados(dados, db):
    itens_pedidos_alias = aliased(ItensPedido)
    query = (
        db.session.query(dados.iloc[0]['ID_Order'], dados.iloc[0]['ID_Product'], dados.iloc[0]['Quantity'])
        .outerjoin(itens_pedidos_alias, int(dados.iloc[0]['ID_Product']) == itens_pedidos_alias.ID_Produto)
        .filter(itens_pedidos_alias.ID_Produto is None)
        .distinct()
    )

    result = query.all()
    df = pd.DataFrame(result)
    return df

