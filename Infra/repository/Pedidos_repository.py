from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Pedido import Pedido
from sqlalchemy import delete, update
import pandas as pd


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

    @staticmethod
    def incluir(dados):
        with DBconnection() as db:
            tratados = tratarDados(dados)
            pedido = Pedido(tratados, dados.id_cliente)
            db.session.add(pedido)
            db.session.commit()

    @staticmethod
    def excluir(id: int):
        with DBconnection() as db:
            stmt = delete(Pedido).where(Pedido.ID_Pedido == id)
            db.session.execute(stmt)

    @staticmethod
    def atualizar(id: int, dados: pd.DataFrame):
        with DBconnection() as db:
            stmt = (
                update(Pedido).
                where(Pedido.ID_Pedido == id).
                values(
                    Data_Pedido=dados.iloc[0]['Order_Date'],
                    Pagamento_data=dados.iloc[0]['Payment_Date'],
                    Valor_Total=dados.iloc[0]['Amount'],
                    Tipo_Entrega=dados.iloc[0]['Delivery_Type'],
                    Moeda=dados.iloc[0]['Currency'],
                    Endereco1=dados.iloc[0]['Address1'],
                    Endereco2=dados.iloc[0]['Address2'],
                    Endereco3=dados.iloc[0]['Address3'],
                    CEP=int(dados.iloc[0]['Postal_Code']),
                    Cidade=dados.iloc[0]['City'],
                    UF=dados.iloc[0]['State'],
                    PAIS=dados.iloc[0]['Country'],
                )
            )
            db.session.execute(stmt)


def tratarDados(dados):
    return dados
