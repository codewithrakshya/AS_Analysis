import matplotlib.pyplot as plt

def plot_splicing_patterns(splicing_pattern_frequencies):
    patterns = list(splicing_pattern_frequencies.keys())
    frequencies = list(splicing_pattern_frequencies.values())

    plt.bar(patterns, frequencies)
    plt.xlabel('Splicing Pattern')
    plt.ylabel('Frequency')
    plt.title('Splicing Pattern Frequencies')
    plt.xticks(rotation=90)
    plt.show()
