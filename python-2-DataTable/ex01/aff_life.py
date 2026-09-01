import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load

def main():
    """main function"""
    load("life_expectancy_years.csv")
    data  = pd.read_csv("life_expectancy_years.csv")
    years = data.columns[1:].astype(int)
    morocco = data[data["country"] == "Morocco"].iloc[0]
    plt.plot(years, morocco[1:])
    plt.title("Morocco Life Expectancy Projections")
    plt.xlabel("year")
    plt.ylabel("Life Expectancy")
    plt.show()

if __name__ == "__main__":
    main()