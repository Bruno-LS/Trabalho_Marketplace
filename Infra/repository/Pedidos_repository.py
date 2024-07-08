from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Pedido import Pedido



class PedidosRepository:

    # Recebe dataframe e fazer o insert conforme a lógica de negócios
    @staticmethod
    def incluir(data_frame):
        with DBconnection() as db:
            id_cliente = 10
            data_insert = Pedido(data_frame, id_cliente)
            db.session.add(data_insert)
            db.session.commit()


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

