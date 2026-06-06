from dataset_loader import load_dataset
from collections import Counter

X, y = load_dataset()

print("Dataset Shape:", X.shape)
print("Total Samples:", len(y))
print("Class Distribution:")
print(Counter(y))