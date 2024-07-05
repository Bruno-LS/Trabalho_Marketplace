"""
1.Criar a conexão com a api externa
2.Puxar o json da api externa e jogar em um dataframe, q será puxado depois em Tratar_Cargas
"""
import requests

df = []

lista_requisicao = []
lista_Pedidos = []

for requisicao in lista_requisicao:
    url = '{}'.format(requisicao)
    req = requests.get(url, timeout=3)
    pedido = req.json()
    lista_Pedidos.append([['Order_ID'], pedido['Order_Date'], pedido['Payment_Date'],
                          ['Total_Amount'], pedido['Delivery_Type'], pedido['Currency'],
                          ['Address1'], pedido['Address2'], pedido['Address3'], ['ZIP_Code'],
                          pedido['City'], pedido['State'], pedido['Country'], pedido['Customer_ID']]
                         )

