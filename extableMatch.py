import matplotlib.pyplot as plt
import numpy as np

def generate_comparison_plot():
    # Data
    num_flows = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    match_rate_20 = [0.68, 0.67, 0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.60, 0.59]
    match_rate_40 = [0.66, 0.65, 0.64, 0.63, 0.62, 0.61, 0.60, 0.59, 0.58, 0.57]
    match_rate_60 = [0.64, 0.63, 0.62, 0.61, 0.60, 0.59, 0.58, 0.57, 0.56, 0.55]

    # Plot configuration
    bar_width = 0.25
    x = np.arange(len(num_flows))

    # Create the bar plots for different ΔT values
    plt.bar(x - bar_width, match_rate_20, bar_width, label='ΔT = 20', hatch='//', edgecolor='black', color='skyblue')
    plt.bar(x, match_rate_40, bar_width, label='ΔT = 40', hatch='x', edgecolor='black', color='salmon')
    plt.bar(x + bar_width, match_rate_60, bar_width, label='ΔT = 60', hatch='\\', edgecolor='black', color='lightgreen')

    # Customize the plot with labels, legend, and title
    plt.xlabel('Number of flows')
    plt.ylabel('Match Rate')
    plt.xticks(x, num_flows)
    plt.ylim(0.55, 0.70)
    plt.legend(title='ΔT')
    plt.title('Match rates of ExTable with different ΔT')

    # Show the plot
    plt.show()

def main():
    # Generate the comparison plot
    generate_comparison_plot()

# Ensure the main function runs when the script is executed directly
if __name__ == "__main__":
    main()

