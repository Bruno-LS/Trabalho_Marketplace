from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Cliente import Cliente


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


