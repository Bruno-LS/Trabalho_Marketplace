"""
1.Criar a conexão com a api externa
2.Puxar o json da api externa e jogar em um dataframe, q será puxado depois em Tratar_Cargas
"""
import requests
import pandas as pd
from Domain.Funcoes_util import tratar_carga

#ajeitar
def iniciar_Transacao(lista_requisicao):

    lista_Carga = []

    for requisicao in lista_requisicao:
        url = '/{}'.format(requisicao)
        req = requests.get(url, timeout=3)
        pedido = req.json()
        lista_Carga.append([pedido["ID_Order"], pedido["ID_Product"], pedido["Order_Date"],
                            pedido["Payment_Date"], pedido["UPC"], pedido["SKU"],
                            pedido["Product_Name"], pedido["Quantity"], pedido["Currency"],
                            pedido["Delivery_Type"], pedido["Amount"], pedido["Email"],
                            pedido["Buyer_Name"], pedido["Address1"], pedido["Address2"],
                            pedido["Address3"], pedido["Postal_Code"], pedido["City"],
                            pedido["State"], pedido["Country"], pedido["Phone"], pedido["Tax_ID"]]
                           )


    df_carga = pd.DataFrame(lista_Carga, columns=[
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

    tratar_carga(df_carga)