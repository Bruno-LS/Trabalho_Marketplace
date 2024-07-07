from sqlalchemy import String, Integer, Column
from Infra.Configs.Base import Base

class Cliente(Base):
    __tablename__ = "Cliente"
    ID = Column(Integer, primary_key=True, nullable=False)
    Nome = Column(String(100), nullable=False)
    CPF = Column(String(11), nullable=False)
    Email = Column(String(100), nullable=False)
    Telefone = Column(String(15), nullable=False)

    def __repr__(self):
        return (f"Cliente(ID_cliente={self.ID}, Nome={self.Nome}, CPF={self.CPF}, "
                f"Email={self.Email}, Telefone={self.Telefone})")


