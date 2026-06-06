import wfdb
from collections import Counter

records = ["100", "101", "102", "103"]

for rec in records:
    annotation = wfdb.rdann(f"data/{rec}", "atr")

    print(f"\nRecord {rec}")
    print(Counter(annotation.symbol))