import pandas as pd
from model.model import SalesDataLoader
from view.view import VisualizationData

class SalesDataController:
    def __init__(self, file_path):
        self.data_loader = SalesDataLoader(file_path)
        self.view = VisualizationData()

    def process_data(self):
        data = self.data_loader.df
        print("DataFrame após processamento inicial:")
        print(data.head())
        print("Colunas no DataFrame:")
        print(data.columns)

        if not data.empty and 'ValorTotalVenda' in data.columns:
            print("Tipos de dados na coluna 'ValorTotalVenda':")
            print(data['ValorTotalVenda'].apply(type).value_counts())
            total_monthly = data['ValorTotalVenda'].sum()
            print("Valores na coluna 'ValorTotalVenda':")
            print(data['ValorTotalVenda'])
            print("Soma total das vendas:", total_monthly)
            if not pd.isna(total_monthly) and isinstance(total_monthly, (int, float)):
                total_monthly = float(total_monthly)
                self.view.display_page(data, total_monthly)
            else:
                print("O valor total das vendas não é um número.")
        else:
            print("DataFrame vazio ou coluna 'ValorTotalVenda' não encontrada.")

