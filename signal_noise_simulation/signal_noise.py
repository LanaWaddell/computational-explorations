import random

def generate_signal(length=100):
    """Generate a clean signal"""
    return [1 for _ in range(length)]

def add_noise(signal, noise_level=0.5):
    """Add noise to the signal"""
    noisy_signal = []
    for value in signal:
        noise = random.uniform(-noise_level, noise_level)
        noisy_signal.append(value + noise)
    return noisy_signal

def moving_average(signal, window_size=5):
    """Simple filter to reduce noise"""
    filtered = []
    for i in range(len(signal)):
        window = signal[max(0, i - window_size):i + 1]
        filtered.append(sum(window) / len(window))
    return filtered

def measure_clarity(original, processed):
    """Measure how close processed signal is to original"""
    error = sum(abs(o - p) for o, p in zip(original, processed))
    return error / len(original)

def run_simulation():
    signal = generate_signal()
    noisy = add_noise(signal, noise_level=0.8)
    filtered = moving_average(noisy)

    clarity_before = measure_clarity(signal, noisy)
    clarity_after = measure_clarity(signal, filtered)

    print("Clarity (lower is better):")
    print(f"Before filtering: {clarity_before:.4f}")
    print(f"After filtering:  {clarity_after:.4f}")

if __name__ == "__main__":
    run_simulation()