import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self):
        self.w = None
        self.b = None

    def model(self, x):
        return 1 if (np.dot(self.w, x).all() >= self.b) else 0

    def predict(self, X):
        Y = []
        for x in X:
            result = self.model(x)
            Y.append(result)
        return np.asarray(Y)

    def fit(self, X, Y, epochs=1, lr=1):
        self.w = np.ones(np.asarray(X).shape[1])
        self.b = 0
        accuracy = {}
        max_accuracy = 0
        wt_matrix = []

        for i in range(epochs):
            for x, y in zip(X, Y):
                y_pred = self.model(x)
                if y == 1 and y_pred == 0:
                    self.w = self.w + lr * np.asarray(x)
                    self.b = self.b - lr * 1
                elif y == 0 and y_pred == 1:
                    self.w = self.w - lr * np.asarray(x)
                    self.b = self.b + lr * 1

            wt_matrix.append(self.w)
            accuracy[i] = accuracy_score(self.predict(X), Y)
            if (accuracy[i] > max_accuracy):
                max_accuracy = accuracy[i]
                checkpouint_w = self.w
                checkpouint_b = self.b
        self.w = checkpouint_w
        self.b = checkpouint_b
        print(max_accuracy)
        plt.plot(accuracy.values())
        plt.xlabel('Epoch #')
        plt.ylabel('Accuracy')
        plt.ylim([0, 1])
        plt.show()
        return np.asarray(wt_matrix)
