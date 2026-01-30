import matplotlib.pyplot as plt

class HistogramPlotter:
    def __init__(self, df):
        self.df = df

    def plot(self, column, bins=20):
        plt.figure()
        plt.hist(self.df[column].dropna(), bins=bins)
        plt.title(f"Distribución de {column}")
        plt.xlabel(column)
        plt.ylabel("Frecuencia")
        plt.show()
