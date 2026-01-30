import pandas as pd

class DataSummary:
    def __init__(self, df):
        self.df = df

    def basic_summary(self):
        """
        Resumen estadístico numérico
        """
        return self.df.describe()

    def missing_values(self):
        """
        Conteo de valores nulos por columna
        """
        return self.df.isna().sum()
