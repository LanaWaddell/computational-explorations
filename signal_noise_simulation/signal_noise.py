import random
import matplotlib.pyplot as plt

def generate_signal(length=100):
    return [1 for _ in range(length)]

def add_noise(signal, noise_level=0.5):
    return [value + random.uniform(-noise_level, noise_level) for value in signal]

def observer_effect(signal, strength=0.2):
    """Simulate observation altering the signal"""
    return [value + random.uniform(-strength, strength) for value in signal]

def moving_average(signal, window_size=5):
    filtered = []
    for i in range(len(signal)):
        window = signal[max(0, i - window_size):i + 1]
        filtered.append(sum(window) / len(window))
    return filtered

def measure_clarity(original, processed):
    error = sum(abs(o - p) for o, p in zip(original, processed))
    return error / len(original)

def plot_signals(original, noisy, observed, filtered):
    plt.figure(figsize=(10, 5))
    plt.plot(original, label="Original Signal", linestyle='dashed')
    plt.plot(noisy, label="Noisy Signal", alpha=0.6)
    plt.plot(observed, label="Observed Signal", alpha=0.6)
    plt.plot(filtered, label="Filtered Signal", linewidth=2)
    plt.legend()
    plt.title("Signal vs Noise Simulation")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()

def run_simulation():
    signal = generate_signal()
    noisy = add_noise(signal, noise_level=0.8)
    observed = observer_effect(noisy, strength=0.3)
    filtered = moving_average(observed)

    print("Clarity (lower is better):")
    print(f"Noisy:     {measure_clarity(signal, noisy):.4f}")
    print(f"Observed:  {measure_clarity(signal, observed):.4f}")
    print(f"Filtered:  {measure_clarity(signal, filtered):.4f}")

    plot_signals(signal, noisy, observed, filtered)

if __name__ == "__main__":
    run_simulation()