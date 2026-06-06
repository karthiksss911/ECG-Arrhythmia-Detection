import wfdb
from collections import Counter

annotation = wfdb.rdann("data/100", "atr")

print(Counter(annotation.symbol))