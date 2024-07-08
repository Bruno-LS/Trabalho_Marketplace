import pandas as pd
from datetime import date
from Infra.repository.Pedidos_repository import PedidosRepository as tab_repo
from Infra.Entities.Pedido import Pedido


data = [[1, 101, date(2024, 7, 1), date(2024, 7, 2), "123456789012", "001", "Product A", 2, "USD", "Standard", 50.0, "buyer1@example.com", "John Doe", "123 Main St", "", "", "12345", "CityA", "StateA", "CountryA", "123-456-7890", "TAX123"]]
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

# novo_pedido = Pedido(df_carga, 84)


# tab_repo.incluir(df_carga)

linha = tab_repo.select()
print(linha)
