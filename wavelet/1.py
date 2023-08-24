import pandas as pd
import os


csv_files = [f for f in os.listdir("synthetic") if f.endswith(".csv")]


os.mkdir("new_folder")


for file in csv_files:

    df = pd.read_csv(os.path.join("synthetic", file), sep=",")


    result = df["Result"].tolist()
    file_new = file[:-4] + "_new.csv"
    with open(os.path.join("new_folder", file_new), "w") as f:
        for r in result:
            f.write(str(r) + "\n")
