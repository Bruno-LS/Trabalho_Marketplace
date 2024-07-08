from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Movimentacao import Movimentacao



class MovimentacaoRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Movimentacao).all()
            return data



    