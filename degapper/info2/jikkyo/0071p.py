import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklean import datasets
from PIL import Image, ImageOps, ImageEnhance
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

digits = datasets.load_digits()
n = 500
print(digits.images[n])
print(digits.data[n])
print(digits.target[n])
plt. imshow(digits.images[n], cmap='gray_r')
plt.show()