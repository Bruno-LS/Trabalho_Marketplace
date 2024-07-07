from sqlalchemy import String, Integer, Column, ForeignKey
from Infra.Configs.Base import Base


class Movimentacao(Base):
    __tablename__ = "Movimentaçao_Estoque"
    ID_Produto = Column(Integer, ForeignKey("Produto.ID_Produto"), nullable=False)
    ID_Pedido = Column(Integer, ForeignKey("Pedido.ID_Pedido"), nullable=False)
    STATUS_Pedido = Column(String(1), nullable=False, default='N')
    Estoque = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Movimentação do Estoque(ID_Pedido={self.ID_Pedido}, ID_Produto={self.ID_Produto}, Estoque={self.Estoque}, Status do Pedido={self.STATUS_Pedido})"

