"""
Criar/Referenciar tabelas
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, Float, DATE, Column, ForeignKey

Base = declarative_base()

class Pedido(Base):
    __tablename__ = "Pedido"
    ID_Pedido = Column(Integer, primary_key=True, nullable=False)
    Data_Pedido = Column(DATE, nullable=False)
    Pagamento_data = Column(DATE, nullable=False)
    Valor_Total = Column(Float, nullable=False)
    Tipo_Entrega = Column(String(20), nullable=False)
    Moeda = Column(String(15), nullable=False)
    Enderecol = Column(String(50), nullable=False)
    Enderec02 = Column(String(50), nullable=False)
    Enderec03 = Column(String(50), nullable=False)
    CEP = Column(Integer, nullable=False)
    Cidade = Column(String(100), nullable=False)
    UF = Column(String(50), nullable=False)
    PAIS = Column(String(30), nullable=False)
    ID_Cliente = Column(Integer, ForeignKey("Cliente.ID_cliente"), nullable=False)

    def __repr__(self):
        return (f"Pedido(ID_Pedido={self.ID_Pedido}, Data_Pedido={self.Data_Pedido}, "
                f"Pagamento_data={self.Pagamento_data}, Valor_Total={self.Valor_Total}, "
                f"Tipo_Entrega={self.Tipo_Entrega}, Moeda={self.Moeda}, Enderecol={self.Enderecol}, "
                f"Enderec02={self.Enderec02}, Enderec03={self.Enderec03}, CEP={self.CEP}, "
                f"Cidade={self.Cidade}, UF={self.UF}, PAIS={self.PAIS}, ID_Cliente={self.ID_Cliente})")



class Cliente(Base):
    __tablename__ = "Cliente"
    ID_cliente = Column(Integer, primary_key=True, nullable=False)
    Nome = Column(String(100), nullable=False)
    CPF = Column(String(11), nullable=False)
    Email = Column(String(100), nullable=False)
    Telefone = Column(String(15), nullable=False)

    def __repr__(self):
        return (f"Cliente(ID_cliente={self.ID_cliente}, Nome={self.Nome}, CPF={self.CPF}, "
                f"Email={self.Email}, Telefone={self.Telefone})")



