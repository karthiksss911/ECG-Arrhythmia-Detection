import wfdb
import numpy as np

record = wfdb.rdrecord("data/100")
annotation = wfdb.rdann("data/100", "atr")

signal = record.p_signal[:, 0]

beats = []
labels = []

for peak, label in zip(annotation.sample, annotation.symbol):

    if peak < 100:
        continue

    if peak + 100 > len(signal):
        continue

    beat = signal[peak-100 : peak+100]

    beats.append(beat)
    labels.append(label)

beats = np.array(beats)

print("Beats shape:", beats.shape)
print("Labels:", len(labels))