import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]


class Dense:
    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        self.output = None
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases


layer1 = Dense(4, 5)
layer2 = Dense(5, 2)

layer1.forward(X)
layer2.forward(layer1.output)
print(layer1.output)
print(layer2.output)