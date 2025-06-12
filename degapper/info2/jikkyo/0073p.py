import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklean import datasets
from PIL import Image, ImageOps, ImageEnhance
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

digits = datasets.load_digits()
filename = 'digit.jpg'
im = Image. open (filename)
im_width, im_height = im.size
square_len = min(im.size)
im = im. crop ((
    (im_width - square_len) // 2,
    (im_height - square_len) // 2,
    (im_width + square_len) // 2,
    (im_height + square_len) // 2
))
im = ImageEnhance.Brightness(im).enhance (2.0)
im = im.convert('L')
im = ImageOps.invert(im)
im = im.resize ((8, 8), Image.LANCZOS)
digit = np.asarray (im)
digit = np.round (16*(digit/255))

x = digits.data
y = digits.target
model = LogisticRegression(solver='liblinear')
model = model.fit(x, y)