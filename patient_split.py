from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from hello import load_record

X100, y100 = load_record("100")
X101, y101 = load_record("101")
X102, y102 = load_record("102")
X103, y103 = load_record("103")

# TRAIN
import numpy as np

X_train = np.vstack([X100, X101, X102])
y_train = np.hstack([y100, y101, y102])

# TEST
X_test = X103
y_test = y103

print("Train:", X_train.shape)
print("Test:", X_test.shape)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(classification_report(y_test, pred))