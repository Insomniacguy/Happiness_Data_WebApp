import pandas as pd

df = pd.read_csv("happy.csv")


def get_data(options1, options2):
    x_data = None
    y_data = None
    if options1 == "Happiness":
        x_data = df['happiness']
    elif options1 == "GDP":
        x_data = df["gdp"]
    else:
        x_data = df['generosity']

    if options2 == "Happiness":
        y_data = df['happiness']
    elif options2 == "GDP":
        y_data = df["gdp"]
    else:
        y_data = df["generosity"]

    return x_data, y_data


if __name__ == "__main__":
    x1, y1 = get_data("happiness", "gdp")
