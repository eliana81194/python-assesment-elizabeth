# Task 10: Machine Learning with Scikit-Learn - KNN & Naive Bayes
# File: task10_ml_knn_naive_bayes.py

# ---------------------------------------------------------
# a. Install scikit-learn and confirm the version (2 marks)
# ---------------------------------------------------------
# Installed from the terminal before running this script:
#
#     pip install scikit-learn pandas
#
# On some systems (e.g. Linux with an externally-managed Python):
#
#     pip install scikit-learn pandas --break-system-packages

import sklearn
print("a. Scikit-Learn Version Check")
print("sklearn version:", sklearn.__version__)
print()

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ---------------------------------------------------------
# b. Load a dataset using Pandas, display first 5 rows (3 marks)
# ---------------------------------------------------------
# The Iris dataset is used here (a common, built-in scikit-learn
# dataset for classification - it is small, clean, and well suited
# for demonstrating KNN and Naive Bayes).

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

print("b. Dataset - First 5 Rows")
print(df.head())
print()

# ---------------------------------------------------------
# c. Prepare features (X) and labels (y); train/test split (4 marks)
# ---------------------------------------------------------
X = df[iris.feature_names]  # features
y = df["target"]            # labels

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("c. Train/Test Split")
print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
print()

# ---------------------------------------------------------
# d. KNN: instantiate, fit, predict (5 marks)
# ---------------------------------------------------------
print("d. KNN - Fit and Predict")

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)
knn_predictions = knn_model.predict(X_test)

print("KNN Predictions:", knn_predictions)
print("Actual Labels:  ", y_test.values)
print()

# ---------------------------------------------------------
# e. KNN: accuracy_score and classification_report (4 marks)
# ---------------------------------------------------------
print("e. KNN - Evaluation")

knn_accuracy = accuracy_score(y_test, knn_predictions)
print("KNN Accuracy:", knn_accuracy)
print("KNN Classification Report:")
print(classification_report(y_test, knn_predictions))

# ---------------------------------------------------------
# f. Mathematics behind KNN (4 marks)
# ---------------------------------------------------------
"""
f. The Mathematics Behind KNN

K-Nearest Neighbours (KNN) is a distance-based classification algorithm.
It classifies a new data point by looking at the 'k' closest points to
it in the training data and assigning the majority class among them.

Euclidean Distance Formula:
For two points A(x1, y1, ..., xn) and B(x2, y2, ..., xn) in n-dimensional
feature space, the Euclidean distance is:

    distance(A, B) = sqrt( (x1 - x2)^2 + (y1 - y2)^2 + ... + (xn - xn)^2 )

In general, for n features:
    distance(A, B) = sqrt( sum_i=1_to_n (A_i - B_i)^2 )

How k is chosen:
- A small k (e.g. k=1) makes the model sensitive to noise/outliers,
  since a single nearby point can change the prediction (overfitting).
- A large k smooths out the decision boundary but may blur the
  distinction between classes, reducing accuracy on complex patterns
  (underfitting).
- k is commonly chosen as an odd number (to avoid ties in binary
  classification) and is often tuned using cross-validation, trying
  several values of k and picking the one with the best validation
  accuracy. In this script, k=3 was chosen as a small, commonly-used
  default that balances sensitivity to noise against oversmoothing.
"""
print()

# ---------------------------------------------------------
# g. Naive Bayes: instantiate, fit, predict (5 marks)
# ---------------------------------------------------------
print("g. Naive Bayes - Fit and Predict")

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
nb_predictions = nb_model.predict(X_test)

print("Naive Bayes Predictions:", nb_predictions)
print("Actual Labels:          ", y_test.values)
print()

# ---------------------------------------------------------
# h. Naive Bayes: accuracy_score and confusion matrix (4 marks)
# ---------------------------------------------------------
print("h. Naive Bayes - Evaluation")

nb_accuracy = accuracy_score(y_test, nb_predictions)
print("Naive Bayes Accuracy:", nb_accuracy)
print("Naive Bayes Confusion Matrix:")
print(confusion_matrix(y_test, nb_predictions))

# ---------------------------------------------------------
# i. Mathematics behind Naive Bayes (4 marks)
# ---------------------------------------------------------
"""
i. The Mathematics Behind Naive Bayes

Naive Bayes is a probabilistic classifier based on Bayes' Theorem,
which describes the probability of a class C given some observed
features X:

    P(C | X) = ( P(X | C) * P(C) ) / P(X)

Where:
    P(C | X) = posterior probability - probability of class C
               given the observed features X
    P(X | C) = likelihood - probability of observing features X
               given that the class is C
    P(C)     = prior probability - how common class C is overall,
               before seeing any features
    P(X)     = evidence - overall probability of observing X
               (acts as a normalizing constant)

The algorithm is called 'Naive' because it assumes that all features
are conditionally independent of each other given the class - i.e.
knowing the value of one feature tells you nothing extra about
another feature, once the class is known. This assumption rarely
holds perfectly in real data, but the algorithm still performs well
in practice.

For continuous features (as in this script, using GaussianNB), the
likelihood P(X | C) for each feature is modelled using a Gaussian
(normal) probability density function:

    P(x | C) = ( 1 / sqrt(2 * pi * variance_C) ) *
               exp( -((x - mean_C)^2) / (2 * variance_C) )

where mean_C and variance_C are the mean and variance of that feature
for class C, estimated from the training data. To classify a new
sample, Naive Bayes computes P(C | X) for every possible class and
selects the class with the highest resulting probability.
"""

