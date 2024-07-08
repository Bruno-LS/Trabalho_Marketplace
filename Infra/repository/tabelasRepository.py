from sqlalchemy import text
from Infra.Configs.connection_DB import DBconnection
from Infra.Entities.Pedido import Pedido
from Infra.Entities.Cliente import Cliente
from Infra.Entities.Movimentacao import Movimentacao
from Infra.Entities.Itens_Pedidos import ItensPedido
from Infra.Entities.Compras import Compras
from Infra.Entities.Produto import Produto


class TabelasRepository:
    db = DBconnection()
    session = DBconnection().session

    # Recebe dataframe e fazer o insert conforme a lógica de negócios
    def incluir(self, data_frame):
        with self.db as db:
            cliente = Cliente(data_frame)
            db.session.add(cliente)
            db.session.commit()
            id_cliente = cliente.ID_cliente
            pedido = Pedido(data_frame, id_cliente)
            db.session.add(pedido)
            db.session.commit()
            produto = Produto(data_frame)
            db.session.add(produto)
            db.session.commit()
            movimentacao = Movimentacao(data_frame)
            db.session.add(movimentacao)
            db.session.commit()
            itensPedido = ItensPedido(data_frame)
            db.session.add(itensPedido)
            db.session.commit()
            compras = Compras(data_frame)
            db.session.add(compras)
            db.session.commit()

