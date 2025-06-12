import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklean import datasets
from PIL import Image, ImageOps, ImageEnhance
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

digits = datasets.load_digits()

x = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, stratify=y)
model = LogisticRegression (solver='liblinear')
model. fit(X_train, y_train)
y_pred = model. predict(X_test)
print (classification_report(y_test, y_pred))