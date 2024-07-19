import json

from Infra.repository.Pedidos_repository import PedidosRepository as ped_repo
from Infra.repository.Clientes_repository import ClientesRepository as cli_repo
from Infra.repository.Itens_Pedidos_repository import ItensPedidoRepository as it_Pe_repo
from Infra.repository.Movimentacao_repository import MovimentacaoRepository as movim_repo
from Infra.repository.Produtosrepository import ProdutosRepository as pr_repo
import pandas as pd


def listar_tabela(nome_tabela):  # Usar nome da tabela pra selecionar qual repository

    if nome_tabela == "Pedido":
        req = ped_repo.select()
    elif nome_tabela == "Cliente":
        req = cli_repo.select()
    elif nome_tabela == "Itens_Pedido":
        req = it_Pe_repo.select()
    elif nome_tabela == "Produto":
        req = pr_repo.select()
    else:
        req = movim_repo.select()

    data = req.__str__()
    linhas = [json.dumps(data, indent=4)]
    return linhas


def buscar_id(nome_tabela, id: int):  # Usar nome da tabela pra selecionar qual repository

    if nome_tabela == "Pedido":
        req = ped_repo.select_id(id)
    elif nome_tabela == "Cliente":
        req = cli_repo.select_id(id)
    else:
        req = pr_repo.select_id(id)

    linha = req.__str__()
    linha = json.dumps(linha, indent=4)
    return linha


def tratar_carga(df_carga: pd.DataFrame):
    cli_repo.incluir(df_carga)
    ped_repo.incluir(df_carga)
    pr_repo.incluir(df_carga)
    it_Pe_repo.incluir(df_carga)
    movim_repo.incluir(df_carga)


def incluir(nome_tabela, dados):
    if nome_tabela == "Pedido":
        ped_repo.incluir(dados)
    elif nome_tabela == "Cliente":
        cli_repo.incluir(dados)
    elif nome_tabela == "Itens_Pedido":
        it_Pe_repo.incluir(dados)
    elif nome_tabela == "Produto":
        pr_repo.incluir(dados)
    else:
        movim_repo.incluir(dados)


def excluir(nome_tabela, id):
    if nome_tabela == "Pedido":
        ped_repo.excluir(id)
    elif nome_tabela == "Cliente":
        cli_repo.excluir(id)
    elif nome_tabela == "Itens_Pedido":
        it_Pe_repo.excluir(id)
    elif nome_tabela == "Produto":
        pr_repo.excluir(id)
    else:
        movim_repo.excluir(id)


def atualizar(id: int, nome_tabela, dados):
    if nome_tabela == "Pedido":
        ped_repo.atualizar(id, dados)
    elif nome_tabela == "Cliente":
        cli_repo.atualizar(id, dados)
    elif nome_tabela == "Itens_Pedido":
        it_Pe_repo.atualizar(id, dados)
    elif nome_tabela == "Produto":
        pr_repo.atualizar(id, dados)
    else:
        movim_repo.atualizar(id)
