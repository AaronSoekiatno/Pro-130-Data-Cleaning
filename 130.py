import csv
import pandas as pd

df = pd.read_csv("totalPlanetData.csv")
del df["mass"]
del df["Distance data"]
del df["radius"]
print(df)