from pybaseball import batting_stats
import pandas
import csv
from functools import reduce

data = batting_stats(2024, qual=50)

ignore = ["IDfg", "Season", "Age", "Dol", "Age Rng", "G", "AB", "PA"]
data.drop(ignore, axis=1, inplace=True)

print(data)
