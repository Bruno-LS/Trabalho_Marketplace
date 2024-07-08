from sqlalchemy import String, Integer, Column, ForeignKey, PrimaryKeyConstraint
from Infra.Configs.Base import Base
import pandas as pd
import json
from dataclasses import dataclass, asdict


@dataclass
class Compras(Base):
    __tablename__ ="Compras"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    Nome_produto = Column(String(30), nullable=False)
    Quant = Column(Integer, nullable=False)

    def __init__(self, data_frame: pd.DataFrame):
        self.Nome_produto = data_frame.iloc[0]['Product_Name']
        self.ID_Produto = int(data_frame.iloc[0]['ID_Product'])
        self.Quant = int(data_frame.iloc[0]['Quantity'])

    __table_args__ = (
        PrimaryKeyConstraint('ID_Produto', name='Compras_pk'),
    )

    def __repr__(self):
        return f"Compras(ID_Produto={self.ID_Produto}, Nome_Produto={self.Nome_produto}, Quantidade={self.Quant})"

