from Infra.repository.Pedidos_repository import PedidosRepository as tab_repo


def listar_tabela(nome_tabela):
    req = tab_repo.select(nome_tabela)
    linhas = req.__repr__()
    return linhas

#ajeitar
def buscar_id(nome_tabela, id):
    req = tab_repo.select(nome_tabela).filter(nome_tabela.ID == id)
    linha = req.__repr__()
    return linha


"""#ajeitar
def remover(nome_tabela, id):
    return status_r
    
def alterar(nome_tabela, data_frame):
"""

#ajeitar e criar
def tratar_carga(df_carga):
    """
    - incluir vindo de repository mais logica das procedures -
    Incluir_Pedido()
    Incluir_Cliente()
    Incluir_Itens_Pedido()
    Incluir_Movimetacao()
    """


"""rep = tab_repo()
linha = rep.select()
print(linha)"""
