import wfdb
import numpy as np
from collections import Counter
def load_dataset():
 records = ["100", "101", "102", "103"]
 beats = []
 binary_labels = []

 for rec in records:

     print(f"Processing {rec}")

     record = wfdb.rdrecord(f"data/{rec}")
     annotation = wfdb.rdann(f"data/{rec}", "atr")
     signal = record.p_signal[:,0]



     for peak, label in zip(annotation.sample, annotation.symbol):

       if peak < 100:
         continue

       if peak + 100 > len(signal):
         continue

       beat = signal[peak-100:peak+100]

       beats.append(beat)

       if label == 'N':
         binary_labels.append(0)
       else:
         binary_labels.append(1)

 beats = np.array(beats)

 print("Dataset Shape:", beats.shape)

 print("\nBinary Label Distribution:")
 print(Counter(binary_labels))
 binary_labels = np.array(binary_labels)

 print(type(beats))
 print(type(binary_labels))

 print(beats.shape)
 print(binary_labels.shape)
 return beats, binary_labels
def load_record(record_id):

    record = wfdb.rdrecord(f"data/{record_id}")
    annotation = wfdb.rdann(f"data/{record_id}", "atr")

    signal = record.p_signal[:,0]

    beats = []
    labels = []

    for peak, label in zip(annotation.sample, annotation.symbol):

        if peak < 100:
            continue

        if peak + 100 > len(signal):
            continue

        beat = signal[peak-100:peak+100]

        beats.append(beat)

        if label == "N":
            labels.append(0)
        else:
            labels.append(1)

    return np.array(beats), np.array(labels)