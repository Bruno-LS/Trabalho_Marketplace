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


class Itens_Pedido(Base):
    __tablename__ = "Itens_Pedidos"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    ID_Pedido = Column(Integer, ForeignKey("Pedido.ID_Pedido"), nullable=False)
    Quant = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"Itens_Pedido(ID_Pedido={self.ID_Pedido}, ID_Produto={self.ID_Produto}, Quantidade={self.Quant})")


class Movimentacao(Base):
    __tablename__ = "Movimentaçao_Estoque"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    ID_Pedido = Column(Integer, ForeignKey("Pedido.ID_Pedido"), nullable=False)
    STATUS_Pedido = Column(String(1), nullable=False, default='N')
    Estoque = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"Movimentação do Estoque(ID_Pedido={self.ID_Pedido}, ID_Produto={self.ID_Produto}, Estoque={self.Estoque}, Status do Pedido={self.STATUS_Pedido})")



class Compras(Base):
    __tablename__ ="Compras"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    Nome_produto = Column(String(30), nullable=False)
    Quant = Column(Integer, nullable=False)

    def __repr__(self):
        return (f"Produtos à Comprar(ID_Produto={self.ID_Produto}, Nome do Produto={self.Nome_produto}, Quantidade={self.Quant})")

