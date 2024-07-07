from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Pedido import Pedido


class PedidosRepository:

    # ajeitar
    def incluir(self, data_frame):
        with DBconnection() as db:
            data_insert = Pedido(data_frame)
            #Logica de insert
            db.session.add(data_insert)
            db.session.commit()

    # ajeitar
    def excluir(self, id):
        with DBconnection() as db:
            db.session.query(Pedido).filter(Pedido.ID_Pedido==id)\
                .delete()
            db.session.commit()


    def select(self):
        with DBconnection() as db:
            data = db.session.query(Pedido).all()
            return data