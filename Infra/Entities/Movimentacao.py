from sqlalchemy import String, Integer, Column, ForeignKey, PrimaryKeyConstraint
from Infra.Configs.Base import Base
import pandas as pd


class Movimentacao(Base):
    __tablename__ = "Movimentaçao_Estoque"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    ID_Pedido = Column(Integer, ForeignKey("Pedido.ID_Pedido"), nullable=False)
    STATUS_Pedido = Column(String(1), nullable=False, default='N')
    Estoque = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('ID_Produto', 'ID_Pedido', name='itens_pedido_pk'),
    )

    def __init__(self, data_frame: pd.DataFrame):
        self.ID_Pedido = data_frame.iloc[0]['ID_Order']
        self.ID_Produto = data_frame.iloc[0]['ID_Product']
        self.Estoque = 10

    def __repr__(self):
        return f"Movimentação do Estoque(ID_Pedido={self.ID_Pedido}, ID_Produto={self.ID_Produto}, Estoque={self.Estoque}, Status do Pedido={self.STATUS_Pedido})"

