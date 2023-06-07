import numpy as np

def calculate_std_deviation(splicing_pattern_frequencies):
    frequencies = list(splicing_pattern_frequencies.values())
    std_deviation = np.std(frequencies)
    return std_deviation

