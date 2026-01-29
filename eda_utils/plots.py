import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.figure()
    plt.hist(df[column].dropna(), bins=20)
    plt.title(f"Distribución de {column}")
    plt.xlabel(column)
    plt.ylabel("Frecuencia")
    plt.show()
