import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Loading split from our split_data.py
df_train: pd.DataFrame = pd.read_csv("data/process/BINNING_train.csv").astype({"LABEL": "int32"})
df_test: pd.DataFrame = pd.read_csv("data/process/BINNING_test.csv").astype({"LABEL": "int32"})
print(df_train.head())
print(df_test.head())

# Training and validation of the model
target = df_train.pop("LABEL")
x_train, x_val, y_train, y_val = train_test_split(df_train, target, train_size=0.80)
classifier = LogisticRegression(penalty="l1", solver="liblinear", max_iter=1000)

breakpoint()
classifier.fit(x_train, y_train)
y_predicted = classifier.predict(x_val).astype(np.int32)

# metrics on validation set
accuracy = metrics.accuracy_score(y_true=y_val, y_pred=y_predicted)
classif_report = metrics.classification_report(y_val, y_predicted)
tn, fp, fn, tp = metrics.confusion_matrix(y_val, y_predicted).ravel()
disp = metrics.plot_confusion_matrix(classifier, x_val, y_val)

print("metrics on the validation set")
print(f"Accuracy: {accuracy}")
print(f"Classification report for classifier {classifier}:\n")
print(f"{classif_report}")
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

# metrics on the test set
y_test = df_test.pop("LABEL")
x_test = df_test.to_numpy()
y_predicted = classifier.predict(x_test).astype(np.int32)

# metrics on validation set
accuracy = metrics.accuracy_score(y_true=y_test, y_pred=y_predicted)
classif_report = metrics.classification_report(y_true=y_test, y_pred=y_predicted)
tn, fp, fn, tp = metrics.confusion_matrix(y_test, y_predicted).ravel()
disp = metrics.plot_confusion_matrix(classifier, x_test, y_test)

print("\nmetrics on the test set")
print(f"Accuracy: {accuracy}")
print(f"Classification report for classifier {classifier}:\n")
print(f"{classif_report}")
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")
plt.show()
