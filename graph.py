import matplotlib.pyplot as plt
import pandas as pd
import datetime

def parse_date(x):
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')

def make_graph(outfile = "graph.png"):

    # options
    figsize = (12,6)

    # load data
    df = pd.read_csv("election_data_SG_GA.csv", converters = {"time": parse_date, "Perdue": int, "Ossoff": int})
    df["VoteDifference"] = df["Perdue"] - df["Ossoff"]

    ax = df.plot(
        x = "time", 
        y = "VoteDifference",
        title = "Senator candidates Perdue vs Ossof",
        xlabel = "Time",
        ylabel = "Vote difference",
        figsize = figsize
    )

    ax.figure.savefig(outfile)

if __name__ == "__main__":
    make_graph()