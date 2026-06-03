import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=10)

class Perceptron:
    def __init__(self, input_size, activation_function):

        self.weight = rng.normal(size=(input_size,1))
        self.bias = 0.
        self.activation = activation_function

    def forward(self, X):
        """
        Berechnet die Ausgabe des Perzeptrons für ein Feauture X.

        Args:
            X: Eingabedaten, Shape (n_samples, n_features)
        Returns:
            Ausgabe des Perzeptrons nach Aktiverung, Shape (n_samples, 1)
        """

        z = X @ self.weight + self.bias
        a = self.activation(z)
        return a

    def train(self, X, y , lr=0.1, epochs=1000, error_prints=True ):
        """
        Trains the perceptron using the perceptron (error-count) learning rule.

        Args:
            X (np.ndarray): Input data of shape (n_samples, n_features).
            y (np.ndarray): Target labels of shape (n_samples, 1) 
            lr (float): Learning rate
            epochs (int): Maximum number of training epochs.
            error_prints (bool) : Printing error rates -> set False for timelapse

        Returns:
            list[float]: List of error_rate per epoch
            list[float]: List of update_rate per epoch
        """
    
        error_history, update_history = [], []

        for epoch in range(epochs):
            update_count  = 0
            for xi, yi in zip(X,y):
                xi = np.reshape(xi, (1,-1)) # (1, n_features)
                yi = np.reshape(yi, (-1,1)) # (1, 1) 
                #Forward pass 
                y_hat = self.forward(xi)

                #Calc delta
                delta = (yi - y_hat)
                delta = np.squeeze(delta)
                delta = float(delta)

                #Update weights and bias
                if delta != 0:
                    self.weight += lr * delta * xi.T
                    self.bias += lr * delta
                    update_count  += 1

            update_rate = update_count /len(y)
            y_hat = self.forward(X)
            y_class_pred = (y_hat >= 0.5).astype(int)
            error_rate = float(np.mean(y != y_class_pred))
            error_history.append(error_rate)            
            update_history.append(update_rate)

            if error_prints:
                if epoch % 10 == 0:
                    print(f'Epoch {epoch}: Error Rate = {error_rate:.4f}')

            if error_rate == 0:
                print(f"Solution in Epoch {epoch}")
                return error_history, update_history
        
        return error_history, update_history

def visualize_training(error_history):
    epochs = np.arange(1, len(error_history) + 1)
    fig, ax = plt.subplots(figsize=(7, 4))

    ax.plot(epochs,error_history, label="Error rate", c="r")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Error rate")
    ax.set_title("Error rate progress")
    ax.legend()
    return fig, ax

def visualize_loss(loss_history, y_label, x_label, ax=None, title="Training Loss"):
    """ 
    Visualizes the loss history.

    Args:
        loss_history:
            List of loss values.
        y_label:
            Label for the y-axis.
        x_label:
            Label for the x-axis.
        ax:
            Optional matplotlib axes object. If None, a new figure and axes are created.
        title:
            Plot title.

    Returns:
        fig, ax:
            Matplotlib figure and axes.
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(7, 4))
    else:
        fig = ax.figure

    ax.plot(loss_history)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(ls=":", linewidth=0.6)

    return fig, ax


def ex_boundary_helper(ax: plt.Axes, intercept: float, x: np.ndarray | None = None) -> np.ndarray:
    if x is None:
        x = np.linspace(-1, 1, 100)
    y = -x + intercept
    ax.plot(x,y, ls="--", lw=2, label="example decision boundary")
    ax.legend()

def step_function(x: np.ndarray):
  return np.where(x >= 0, 1, 0)

def sigmoid(x: np.ndarray):
  return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x: np.ndarray):
  ds = (np.exp(-x))/(1+np.exp(-x))**2
  return ds