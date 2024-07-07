from sqlalchemy import Integer, Column, ForeignKey
from Infra.Configs.Base import Base


class ItensPedido(Base):
    __tablename__ = "Itens_Pedidos"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    ID_Pedido = Column(Integer, ForeignKey("Pedido.ID_Pedido"), nullable=False)
    Quant = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Itens_Pedido(ID_Pedido={self.ID_Pedido}, ID_Produto={self.ID_Produto}, Quantidade={self.Quant})"

