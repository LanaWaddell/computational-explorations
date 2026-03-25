import random

class Qubit:
    def __init__(self, alpha=1.0, beta=0.0):
        """
        alpha = amplitude for |0>
        beta = amplitude for |1>
        Must satisfy: |alpha|^2 + |beta|^2 = 1
        """
        self.alpha = alpha
        self.beta = beta

    def state(self):
        return f"{self.alpha:.2f}|0> + {self.beta:.2f}|1>"

    def measure(self):
        """Simulate measurement collapse"""
        prob_0 = self.alpha ** 2
        rand = random.random()

        if rand < prob_0:
            self.alpha, self.beta = 1.0, 0.0
            return 0
        else:
            self.alpha, self.beta = 0.0, 1.0
            return 1

    def apply_hadamard(self):
        """Create superposition"""
        new_alpha = (self.alpha + self.beta) / (2 ** 0.5)
        new_beta = (self.alpha - self.beta) / (2 ** 0.5)
        self.alpha, self.beta = new_alpha, new_beta


def run_experiment(trials=1000):
    results = {0: 0, 1: 0}

    for _ in range(trials):
        q = Qubit(1.0, 0.0)  # Start in |0>
        q.apply_hadamard()   # Put into superposition
        outcome = q.measure()
        results[outcome] += 1

    print("Measurement Results:")
    print(f"0: {results[0]}")
    print(f"1: {results[1]}")
    print(f"Ratio 0: {results[0]/trials:.2f}")
    print(f"Ratio 1: {results[1]/trials:.2f}")


if __name__ == "__main__":
    print("Initial Qubit:")
    q = Qubit(1.0, 0.0)
    print(q.state())

    print("\nAfter Hadamard (superposition):")
    q.apply_hadamard()
    print(q.state())

    print("\nMeasurement outcome:")
    result = q.measure()
    print(f"Collapsed to: |{result}>")

    print("\nRunning repeated experiment...")
    run_experiment()