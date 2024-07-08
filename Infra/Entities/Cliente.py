from sqlalchemy import String, Integer, Column
from Infra.Configs.Base import Base
import pandas as pd


class Cliente(Base):
    __tablename__ = "Cliente"
    ID_cliente = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    Nome = Column(String(100), nullable=False)
    CPF = Column(String(11), nullable=False)
    Email = Column(String(100), nullable=False)
    Telefone = Column(String(15), nullable=False)

    def __init__(self, data_frame: pd.DataFrame):
        self.ID_Cliente = self.ID_cliente
        self.Nome = data_frame.iloc[0]['Buyer_Name']
        self.CPF = data_frame.iloc[0]['Tax_ID']
        self.Email = data_frame.iloc[0]['Email']
        self.Telefone = data_frame.iloc[0]['Phone']

    def __repr__(self):
        return (f"Cliente(ID_cliente={self.ID_cliente}, Nome={self.Nome}, CPF={self.CPF}, "
                f"Email={self.Email}, Telefone={self.Telefone})")


