from sqlalchemy import String, Integer, Column, ForeignKey, PrimaryKeyConstraint, Float
from Infra.Configs.Base import Base
import pandas as pd
import json
from dataclasses import dataclass, asdict




@dataclass
class Produto(Base):
    __tablename__ = "Produto"
    ID_Produto = Column(Integer, primary_key=True, nullable=False)
    Valor = Column(Float, nullable=False)
    Nome_produto = Column(String(30), nullable=False)
    UPC = Column(Integer, nullable=False)
    SKU = Column(Integer, nullable=False)
    Estoque = Column(Integer, nullable=False)

    def __init__(self, data_frame: pd.DataFrame):

        self.ID_Produto = int(data_frame.iloc[0]['ID_Product'])
        self.Estoque = 10
        self.UPC = int(data_frame.iloc[0]['UPC'])
        self.SKU = int(data_frame.iloc[0]['SKU'])
        self.Nome_produto = data_frame.iloc[0]['Product_Name']
        self.Valor = float(data_frame.iloc[0]['Amount'])

    def __repr__(self):
        return f"ID_Produto:{self.ID_Produto}, Estoque:{self.Estoque}, Nome_Produto:{self.Nome_produto}, Valor:{self.Valor}, Valor:{self.UPC}, Valor:{self.SKU}"
