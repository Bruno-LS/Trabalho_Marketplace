from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Movimentacao import Movimentacao
from sqlalchemy import delete, update
import pandas as pd


class MovimentacaoRepository:

    @staticmethod
    def select():
        with DBconnection() as db:
            data = db.session.query(Movimentacao).all()
            return data

    @staticmethod
    def incluir(dados):
        with DBconnection() as db:
            tratados = tratarDados(dados)
            movimentacao = Movimentacao(tratados)
            db.session.add(movimentacao)
            db.session.commit()

    @staticmethod
    def excluir(id: int):
        with DBconnection() as db:
            stmt = delete(Movimentacao).where(Movimentacao.ID_Movimentacao == id)
            db.session.execute(stmt)

    @staticmethod
    def atualizar(id: int):
        with DBconnection() as db:
            stmt = (
                update(Movimentacao).
                where(Movimentacao.ID_Produto == id).
                values(
                    Estoque=10,
                )
            )
            db.session.execute(stmt)


def tratarDados(dados):
    return dados
