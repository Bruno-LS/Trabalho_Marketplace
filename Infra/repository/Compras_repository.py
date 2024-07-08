from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Compras import Compras



class ComprasRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Compras).all()
            return data


    @staticmethod
    def select_id(self, id):
        with DBconnection() as db:
            data = db.session.query(Compras).filter(Compras.ID_Produto == id)
            return data

