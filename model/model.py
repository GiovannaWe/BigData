import pandas as pd

class SalesDataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.load_data()

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path, dtype={"ValorTotalVenda": str})
            self.df["ValorTotalVenda"] = self.df["ValorTotalVenda"].str.replace(',', '.')
            if 'DataVenda' in self.df.columns:
                self.df["DataVenda"] = pd.to_datetime(self.df["DataVenda"], errors="coerce")
                self.df = self.df.dropna(subset=["DataVenda"])
                self.df = self.df.sort_values("DataVenda")
                self.df["Mes"] = self.df["DataVenda"].dt.strftime("%Y-%m")
                self.df["ValorTotalVenda"] = pd.to_numeric(self.df["ValorTotalVenda"], errors='coerce')
                self.df = self.df.dropna(subset=["ValorTotalVenda"])
            else:
                print("Coluna 'DataVenda' não encontrada no DataFrame.")
        except Exception as e:
            print(f"Erro ao carregar os dados do arquivo CSV: {str(e)}")
