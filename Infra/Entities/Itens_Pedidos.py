from sqlalchemy import Integer, Column, ForeignKey, PrimaryKeyConstraint
from Infra.Configs.Base import Base
import pandas as pd
import json
from dataclasses import dataclass, asdict



@dataclass
class ItensPedido(Base):
    __tablename__ = "Itens_Pedidos"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    ID_Pedido = Column(Integer, ForeignKey("Pedido.ID_Pedido"), nullable=False)
    Quant = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('ID_Produto', 'ID_Pedido', name='itens_pedido_pk'),
    )

    def __init__(self, data_frame: pd.DataFrame):
        self.ID_Pedido = int(data_frame.iloc[0]['ID_Order'])
        self.ID_Produto = int(data_frame.iloc[0]['ID_Product'])
        self.Quant = int(data_frame.iloc[0]['Quantity'])


    def __repr__(self):
        return f"Itens_Pedido(ID_Pedido={self.ID_Pedido}, ID_Produto={self.ID_Produto}, Quantidade={self.Quant})"


