from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Itens_Pedidos import ItensPedido






class ItensPedidoRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(ItensPedido).all()
            return data

