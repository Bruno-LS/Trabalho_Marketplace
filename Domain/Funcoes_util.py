from Infra.repository.Pedidos_repository import PedidosRepository as ped_repo
from Infra.repository.Clientes_repository import ClientesRepository as cli_repo
from Infra.repository.Itens_Pedidos_repository import ItensPedidoRepository as it_Pe_repo
from Infra.repository.Movimentacao_repository import MovimentacaoRepository as movim_repo
import pandas as pd


def listar_tabela(nome_tabela): #Usar nome da tabela pra selecionar qual repository

    if nome_tabela == "Pedido":
        req = ped_repo.select()
    elif nome_tabela == "Cliente":
        req = cli_repo.select()
    elif nome_tabela == "Itens_Pedido":
        req = it_Pe_repo.select()
    else:
        req = movim_repo.select()

    linhas = req.__repr__()
    return linhas

#ajeitar
def buscar_id(nome_tabela, id: int): #Usar nome da tabela pra selecionar qual repository

    if nome_tabela == "Pedido":
        req = ped_repo.select_id(id)
    else: # nome_tabela == "Cliente":
        req = cli_repo.select_id(id)

    linha = req.__repr__()
    return linha




#ajeitar
def tratar_carga(df_carga: pd.DataFrame):
    """
    - incluir vindo de repository mais logica das procedures - """
    cli_repo.incluir(df_carga) # - Incluir_Cliente
    ped_repo.incluir(df_carga) # - Incluir_Pedido

    it_Pe_repo.incluir(df_carga) # - Incluir_Itens_Pedido
    movim_repo.incluir(df_carga) # - Incluir_Movimetacao




