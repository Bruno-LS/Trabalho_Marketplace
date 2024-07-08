from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Movimentacao import Movimentacao



class MovimentacaoRepository:

    # Recebe dataframe e fazer o insert conforme a lógica de negócios
    @staticmethod
    def incluir(data_frame):
        with DBconnection() as db:
            data_insert = Movimentacao(data_frame)
            db.session.add(data_insert)
            db.session.commit()


    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Movimentacao).all()
            return data



