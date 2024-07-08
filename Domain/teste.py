import pandas as pd
from datetime import date
from Infra.repository.Pedidos_repository import PedidosRepository as tab_repo
from Infra.repository.Clientes_repository import ClientesRepository as cl
from Infra.repository.tabelasRepository import TabelasRepository as tbr
from Infra.Entities.Pedido import Pedido


data = {
    "ID_Order": [1],
    "ID_Product": [101],
    "Order_Date": ["2024-07-01"],
    "Payment_Date": ["2024-07-03"],
    "UPC": [123456],
    "SKU": [1111],
    "Product_Name": ["Produto A"],
    "Quantity": [10],
    "Currency": ["BRL"],
    "Delivery_Type": ["Correios"],
    "Amount": [100.50],
    "Email": ["comprador1@example.com"],
    "Buyer_Name": ["João Silva"],
    "Address1": ["Rua A, 123"],
    "Address2": ["Apto 101"],
    "Address3": [None],
    "Postal_Code": [12345678],
    "City": ["São Paulo"],
    "State": ["SP"],
    "Country": ["Brasil"],
    "Phone": ["11999999999"],
    "Tax_ID": ["12345678901"]
}
df_carga = pd.DataFrame(data, columns=[
        "ID_Order",
        "ID_Product",
        "Order_Date",
        "Payment_Date",
        "UPC",
        "SKU",
        "Product_Name",
        "Quantity",
        "Currency",
        "Delivery_Type",
        "Amount",
        "Email",
        "Buyer_Name",
        "Address1",
        "Address2",
        "Address3",
        "Postal_Code",
        "City",
        "State",
        "Country",
        "Phone",
        "Tax_ID"
    ])

print(df_carga)
# novo_pedido = Pedido(df_carga, 84)


# tab_repo.incluir(df_carga)

# cl.incluir(df_carga)
tb = tbr()
tb.incluir(df_carga)
