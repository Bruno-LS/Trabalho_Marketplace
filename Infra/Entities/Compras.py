from sqlalchemy import String, Integer, Column, ForeignKey
from Infra.Configs.Base import Base

class Compras(Base):
    __tablename__ ="Compras"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    Nome_produto = Column(String(30), nullable=False)
    Quant = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Produtos à Comprar(ID_Produto={self.ID_Produto}, Nome do Produto={self.Nome_produto}, Quantidade={self.Quant})"

