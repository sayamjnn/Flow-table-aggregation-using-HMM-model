import matplotlib.pyplot as plt
import numpy as np

def generate_accuracy_plot():
    # Data
    flow_entries = [25, 50, 75, 100, 125, 150, 175, 200]
    accuracy_50 = [0.62, 0.66, 0.70, 0.74, 0.78, 0.82, 0.86, 0.88]
    accuracy_70 = [0.61, 0.65, 0.69, 0.73, 0.77, 0.81, 0.85, 0.87]
    accuracy_90 = [0.60, 0.64, 0.68, 0.72, 0.76, 0.80, 0.84, 0.86]

    # Plot
    bar_width = 0.25
    x = np.arange(len(flow_entries))

    plt.bar(x - bar_width, accuracy_50, bar_width, label='50', hatch='//', edgecolor='black')
    plt.bar(x, accuracy_70, bar_width, label='70', hatch='x', edgecolor='black')
    plt.bar(x + bar_width, accuracy_90, bar_width, label='90', hatch='\\', edgecolor='black')

    # Labels and legend
    plt.xlabel('Number of flow entries')
    plt.ylabel('Accuracy')
    plt.xticks(x, flow_entries)
    plt.ylim(0.60, 0.90)
    plt.legend()
    plt.title('Prediction accuracy vs size of flow table')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    generate_accuracy_plot()

