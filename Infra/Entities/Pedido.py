import json
from dataclasses import dataclass, asdict
from sqlalchemy import String, Integer, Float, DATE, Column, ForeignKey
from Infra.Configs.Base import Base
import pandas as pd


@dataclass
class Pedido(Base):
    __tablename__ = "Pedido"
    ID_Pedido = Column(Integer, primary_key=True, nullable=False)
    Data_Pedido = Column(DATE, nullable=False)
    Pagamento_data = Column(DATE, nullable=False)
    Valor_Total = Column(Float, nullable=False)
    Tipo_Entrega = Column(String(20), nullable=False)
    Moeda = Column(String(15), nullable=False)
    Endereco1 = Column(String(50), nullable=False)
    Endereco2 = Column(String(50), nullable=False)
    Endereco3 = Column(String(50), nullable=False)
    CEP = Column(Integer, nullable=False)
    Cidade = Column(String(100), nullable=False)
    UF = Column(String(50), nullable=False)
    PAIS = Column(String(30), nullable=False)
    ID_Cliente = Column(Integer, ForeignKey("Cliente.ID_cliente"), nullable=False)


    def __init__(self, data_frame: pd.DataFrame, ID_Cliente):
        self.ID_Pedido = int(data_frame.iloc[0]['ID_Order'])
        self.Data_Pedido = data_frame.iloc[0]['Order_Date']
        self.Pagamento_data = data_frame.iloc[0]['Payment_Date']
        self.Valor_Total = data_frame.iloc[0]['Amount']
        self.Tipo_Entrega = data_frame.iloc[0]['Delivery_Type']
        self.Moeda = data_frame.iloc[0]['Currency']
        self.Endereco1 = data_frame.iloc[0]['Address1']
        self.Endereco2 = data_frame.iloc[0]['Address2']
        self.Endereco3 = data_frame.iloc[0]['Address3']
        self.CEP = int(data_frame.iloc[0]['Postal_Code'])
        self.Cidade = data_frame.iloc[0]['City']
        self.UF = data_frame.iloc[0]['State']
        self.PAIS = data_frame.iloc[0]['Country']
        self.ID_Cliente = ID_Cliente


    def __repr__(self):
        return (f"ID_Pedido:{self.ID_Pedido}, Data_Pedido:{self.Data_Pedido}, "
                f"Pagamento_data:{self.Pagamento_data}, Valor_Total:{self.Valor_Total}, "
                f"Tipo_Entrega:{self.Tipo_Entrega}, Moeda:{self.Moeda}, Enderecol:{self.Endereco1}, "
                f"Enderec02:{self.Endereco2}, Enderec03:{self.Endereco3}, CEP:{self.CEP}, "
                f"Cidade:{self.Cidade}, UF:{self.UF}, PAIS:{self.PAIS}, ID_Cliente:{self.ID_Cliente}")


