import wfdb

annotation = wfdb.rdann("data/100", "atr")

print("First 20 beat locations:")
print(annotation.sample[:20])

print("\nFirst 20 beat labels:")
print(annotation.symbol[:20])