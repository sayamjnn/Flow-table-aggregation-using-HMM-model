import matplotlib.pyplot as plt
import numpy as np

def generate_comparison_plot():
    # Data
    flow_entries = [25, 50, 75, 100, 125, 150, 175, 200]
    accuracy_match_freq = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.88]
    accuracy_proposed = [0.60, 0.64, 0.70, 0.75, 0.78, 0.83, 0.87, 0.90]

    # Plot
    bar_width = 0.35
    x = np.arange(len(flow_entries))

    plt.bar(x - bar_width/2, accuracy_match_freq, bar_width, label='Match frequency', hatch='//', edgecolor='black',color='skyblue')
    plt.bar(x + bar_width/2, accuracy_proposed, bar_width, label='Proposed', hatch='\\', edgecolor='black',color='purple')

    # Labels and legend
    plt.xlabel('Number of flow entries')
    plt.ylabel('Accuracy')
    plt.xticks(x, flow_entries)
    plt.ylim(0.50, 0.90)
    plt.legend()
    plt.title('Comparison of prediction accuracies')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    generate_comparison_plot()

