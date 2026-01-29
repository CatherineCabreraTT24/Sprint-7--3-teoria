import seaborn as sns
from eda_utils.stats import basic_summary, missing_values
from eda_utils.plots import plot_histogram


def main():
    df = sns.load_dataset("penguins")

    print("Resumen estadístico:")
    print(basic_summary(df))

    print("\nValores faltantes:")
    print(missing_values(df))

    plot_histogram(df, "bill_length_mm")


if __name__ == "__main__":
    main()
