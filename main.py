# -*- coding: utf-8 -*-
"""DL Lab assignment 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v7venM6mR3jA4hXWaCVshzfuB2gNVsEp

Initializaton
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/content/drive/MyDrive/Lab Assignment 1/archive/train.csv')

X=data[['blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory',
       'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram',
       'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi']]
y = data['price_range']

"""Problem 1"""

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, stratify=y,train_size=0.80,test_size=0.20)

def normalize(X_train,X_test):
  stdsc = StandardScaler()
  stdsc.fit(X_train)
  X_train_std = stdsc.transform(X_train)
  X_test_std = stdsc.transform(X_test)
  return X_train_std, X_test_std

# Evaluation metrics
def evaluate(mlp,test,y_test):
  y_predicted = mlp.predict(test)
  print(metrics.classification_report(y_test, y_predicted))
  return y_predicted

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, train_size=0.80,test_size=0.20)
X_train_std, X_test_std = normalize(X_train, X_test)
mlp = MLPClassifier(max_iter = 500,hidden_layer_sizes=(100,100,100,100), learning_rate_init=0.001, activation='tanh',random_state = 1)
mlp.fit(X_train_std, y_train)
pred_score = mlp.score(X_test_std, y_test)

y_predicted=evaluate(mlp, X_test_std, y_test)

#7. Confusion Matrix
mat = confusion_matrix(y_test, y_predicted)
sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False)
plt.xlabel("True Label")
plt.ylabel("Predicted Label")

"""Problem 2"""

X_t, X_test, y_t, y_test = train_test_split(X, y, random_state=1, stratify=y,train_size=0.80,test_size=0.20)

def normalize(X_train,X_test):
  stdsc = StandardScaler()
  stdsc.fit(X_train)
  X_train_std = stdsc.transform(X_train)
  X_test_std = stdsc.transform(X_test)
  return X_train_std, X_test_std

# Commented out IPython magic to ensure Python compatibility.
#8. Accuracy vs epoch

# %matplotlib inline
def calc_score(X_train_std, X_test_std, y_train):
  start_num_epochs = 10
  finish_num_epochs = 500
  inc_amt = 10

  pred_scores = []
  num_epochs = []

  for epoch_count in range(start_num_epochs, finish_num_epochs, inc_amt):
    my_classifier = MLPClassifier(random_state=1,hidden_layer_sizes=(50,), max_iter= epoch_count)
    my_classifier.fit(X_train_std, y_train)
    score = my_classifier.score(X_test_std, y_test)
    pred_scores.append(score)
    num_epochs.append(epoch_count)
  return pred_scores,num_epochs

X_train_std, X_test_std = normalize(X_t, X_test)
pred_scores_1,num_of_epochs_1=calc_score(X_train_std,X_test_std,y_t)

X_train, X_val, y_train, y_val = train_test_split(X_t, y_t, random_state=1,stratify=y_t, train_size=0.75,test_size=0.25)
X_train_std, X_test_std = normalize(X_train, X_test)
pred_scores_2,num_of_epochs_2=calc_score(X_train_std,X_test_std,y_train)

X_train, X_val, y_train, y_val = train_test_split(X_t, y_t, random_state=1,stratify=y_t, train_size=0.50,test_size=0.50)
X_train_std, X_test_std = normalize(X_train, X_test)
pred_scores_3,num_of_epochs_3=calc_score(X_train_std,X_test_std,y_train)

X_train, X_val, y_train, y_val = train_test_split(X_t, y_t, random_state=1,stratify=y_t, train_size=0.25,test_size=0.75)
X_train_std, X_test_std = normalize(X_train, X_test)
pred_scores_4,num_of_epochs_4=calc_score(X_train_std,X_test_std,y_train)

plt.plot(num_of_epochs_1, pred_scores_1, "r-+", linewidth = 2,label='100% Train')
plt.plot(num_of_epochs_2, pred_scores_2, "b-+", linewidth = 2,label='75% Train')
plt.plot(num_of_epochs_3, pred_scores_3, "g-+", linewidth = 2,label='50% Train')
plt.plot(num_of_epochs_4, pred_scores_4, "y-+", linewidth = 2,label='25% Train')
plt.xlabel("Number of epochs")
plt.ylabel("Acc")
plt.title("Impact of number of training epochs")
plt.legend()
plt.show()