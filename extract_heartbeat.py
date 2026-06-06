import wfdb
import matplotlib.pyplot as plt

record = wfdb.rdrecord("data/100")
annotation = wfdb.rdann("data/100", "atr")

signal = record.p_signal[:,0]

peak = annotation.sample[2]


beat = signal[peak-100:peak+100]

print("Peak location:", peak)
print("Beat shape:", beat.shape)

plt.figure(figsize=(8,4))
plt.plot(beat)
plt.title("Single Heartbeat")
plt.grid()
plt.show()
