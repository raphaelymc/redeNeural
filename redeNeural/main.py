import numpy as np
import matplotlib.pyplot as plt

# Função sigmoide e sua derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Dados de entrada (inputs)
input_layer = np.array([[0, 0, 1],
                        [1, 1, 1],
                        [1, 0, 1],
                        [0, 1, 1]])

# Saídas esperadas (outputs)
y = np.array([[0], [1], [1], [0]])

# Pesos iniciais aleatórios
np.random.seed(1)
synaptic_weights = 2 * np.random.random((3, 1)) - 1

# Número de iterações (épocas)
epochs = 10000
errors = []  # NOVO: lista para armazenar o erro em cada época

# Treinamento
for iteration in range(epochs):
    # Propagação para frente
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    # Cálculo do erro
    error = y - outputs
    errors.append(np.mean(np.abs(error)))  # NOVO: registra o erro médio

    # Ajuste dos pesos (Backpropagation)
    adjustments = np.dot(input_layer.T, error * sigmoid_derivative(outputs))
    synaptic_weights += adjustments

# Resultados finais
print("\nPesos finais após o treinamento:")
print(synaptic_weights)

print("\nSaída após o treinamento:")
print(outputs)

# --- NOVO: gráfico do erro ---
plt.plot(errors)
plt.title("Evolução do Erro Durante o Treinamento")
plt.xlabel("Época")
plt.ylabel("Erro médio")
plt.grid(True)
plt.show()
