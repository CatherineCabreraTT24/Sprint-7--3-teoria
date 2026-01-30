import seaborn as sns
from eda_utils.stats import DataSummary
from eda_utils.plots import HistogramPlotter


def main():
    df = sns.load_dataset("penguins")

    # Resúmenes
    summary = DataSummary(df)

    print("Resumen estadístico:")
    print(summary.basic_summary())

    print("\nValores faltantes:")
    print(summary.missing_values())

    # Gráficas
    plotter = HistogramPlotter(df)
    plotter.plot("bill_length_mm")


if __name__ == "__main__":
    main()
