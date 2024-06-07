import pandas as pd

# Simulando os dados de vendas
data = {
    'venda_id': [1, 2, 3, 4, 5],
    'data_venda': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04', '2024-06-05'],
    'produto_id': [101, 102, 103, 104, 105],
    'quantidade': [5, 10, 2, 8, 3],
    'preco_unitario': [20.0, 15.0, 40.0, 10.0, 25.0],
    'valor_total': [100.0, 150.0, 80.0, 80.0, 75.0]
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Convertendo a coluna data_venda para o tipo datetime
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Salvando o DataFrame como um arquivo Parquet
df.to_parquet('vendas.parquet', index=False)
