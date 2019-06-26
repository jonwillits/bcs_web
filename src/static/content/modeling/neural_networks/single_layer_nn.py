import numpy as np

NUM_EPOCHS = 10
LEARNING_RATE = 1


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [1]])
num_examples = X.shape[0]
num_input_units = X.shape[1]

bias = np.random.normal(size=1)
weights = np.random.normal(size=2)

for e in range(NUM_EPOCHS):

    for i in range(num_examples):

        z = np.dot(X[i], weights) + bias
        y_hat = sigmoid(z)

        error = Y[i] - y_hat
        sigmoid_prime = y_hat * (1 - y_hat)

        for j in range(num_input_units):
            weights[j] += LEARNING_RATE * error * sigmoid_prime * X[i,j]
        bias += LEARNING_RATE * error * sigmoid_prime

    # accuracy
    num_correct = 0
    for i in range(num_examples):
        z = np.dot(X[i], weights) + bias
        y_hat = sigmoid(z)
        if y_hat > 0.5:
            if Y[i] == 1:
                num_correct += 1
        else:
            if Y[i] == 0:
                num_correct += 1
    print(e, num_correct / X.shape[0])


