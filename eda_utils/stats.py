import pandas as pd

def basic_summary(df):
    """
    Resumen estadístico numérico
    """
    return df.describe()


def missing_values(df):
    """
    Conteo de valores nulos por columna
    """
    return df.isna().sum()
