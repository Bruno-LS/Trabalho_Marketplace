from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Cliente import Cliente


class ClientesRepository:

    # Recebe dataframe e fazer o insert conforme a lógica de negócios
    @staticmethod
    def incluir(data_frame):
        with DBconnection() as db:
            data_insert = Cliente(data_frame)
            db.session.add(data_insert)
            db.session.commit()

    # Retira de todas as tabelas onde possui chave estrangeira
    @staticmethod
    def excluir(id):
        with DBconnection() as db:
            db.session.query(Cliente).filter(Cliente.ID_cliente == id) \
                .delete()
            db.session.commit()

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
