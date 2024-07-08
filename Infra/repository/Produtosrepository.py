from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Produto import Produto



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

