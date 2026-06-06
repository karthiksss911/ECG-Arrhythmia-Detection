import wfdb
import matplotlib.pyplot as plt

record = wfdb.rdrecord("data/100")

signal = record.p_signal[:, 0]

print("Signal shape:", signal.shape)

plt.figure(figsize=(12,4))
plt.plot(signal[:2000])
plt.show()