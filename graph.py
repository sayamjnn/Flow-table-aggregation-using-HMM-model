import matplotlib.pyplot as plt

def generate_compression_ratio_plot():
    # Data for the plot
    number_of_flow_entries = [100, 200, 300, 400, 500, 600, 700, 800]
    ffta = [0.85, 0.86, 0.87, 0.86, 0.87, 0.87, 0.88, 0.88]
    pruning = [0.75, 0.78, 0.77, 0.76, 0.75, 0.76, 0.75, 0.76]
    proposed = [0.55, 0.57, 0.56, 0.55, 0.56, 0.56, 0.57, 0.57]
    pruning_espresso = [0.60, 0.62, 0.61, 0.60, 0.61, 0.62, 0.63, 0.64]

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(number_of_flow_entries, ffta, label='FFTA', marker='o', linestyle='-', color='black')
    plt.plot(number_of_flow_entries, pruning, label='Pruning', marker='x', linestyle='-', color='blue')
    plt.plot(number_of_flow_entries, pruning_espresso, label='Pruning + Espresso-II', marker='o', linestyle='--', color='red')
    plt.plot(number_of_flow_entries, proposed, label='Proposed', marker='o', linestyle='-', color='green')

    # Customize the plot
    plt.xlabel('Number of flow entries')
    plt.ylabel('Compression ratio')
    plt.title('The compression ratios of four different schemes')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the plot as an image
    plt.savefig('compression_ratio_graph.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    generate_compression_ratio_plot()

