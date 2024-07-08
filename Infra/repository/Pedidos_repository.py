from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Pedido import Pedido



class PedidosRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Pedido).all()
            return data

    @staticmethod
    def select_id(id: int):
        with DBconnection() as db:
            data = db.session.query(Pedido).filter(Pedido.ID_Pedido == id)
            return data

