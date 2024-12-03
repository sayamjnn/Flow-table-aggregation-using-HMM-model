import numpy as np
from hmmlearn import hmm
from collections import defaultdict

# Function to read flow entries from a file and return them as a list of dictionaries
def read_flow_entries(file_path):
    flow_entries = defaultdict(int)  # Dictionary to store the counter for each flow entry
    with open(file_path, 'r') as f:
        for line in f:
            # Parse each line to extract dl_src, dl_dst, and action
            parts = line.strip().split(', ')
            flow_entry = {}
            for part in parts:
                key, value = part.split(': ')
                flow_entry[key] = value
            
            # Create a unique key for the flow entry (combination of dl_src and dl_dst)
            entry_key = (flow_entry['dl_src'], flow_entry['dl_dst'])
            
            # Update the flow entry counter
            flow_entries[entry_key] += 1
    
    return flow_entries

# Function to process the flow entries and prepare them for HMM
def prepare_data_for_hmm(flow_entries):
    # Prepare the data: we will use the match count (counter) as the observation
    flow_data = [(entry, count) for entry, count in flow_entries.items()]
    return flow_data

# Function to train the HMM model
def train_hmm_model(flow_data):
    # Convert the flow data into a format that the HMM can use
    X = np.array([count for entry, count in flow_data]).reshape(-1, 1)

    # Define and train the HMM
    model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=1000)
    model.fit(X)

    return model

# Function to predict and cache top 10 most popular flow entries
def predict_popularity_and_cache(flow_data, model):
    # Predict the state for each flow entry
    X = np.array([count for entry, count in flow_data]).reshape(-1, 1)
    states = model.predict(X)

    # Create a list of flow entries with their states
    flow_state_data = [(entry, count, state) for (entry, count), state in zip(flow_data, states)]

    # Sort the flow entries by their counter (in descending order) and get the top 10
    top_10_entries = sorted(flow_state_data, key=lambda x: x[1], reverse=True)[:10]

    return top_10_entries

# Function to display top 10 flow entries in cache
def display_top_10_entries(top_10_entries):
    print("Top 10 Popular Flow Entries in Cache:")
    for entry, count, state in top_10_entries:
        print(f"Flow Entry: {entry}, Counter: {count}, Predicted State: {state}")

# Main function to run the model
def main():
    file_path = '/home/onos/dynamic_routing/mininet/SDN-Project/ryu/flows_output/compressedfile.txt'  # Path to the file containing flow entries
    
    # Step 1: Read flow entries from the file
    flow_entries = read_flow_entries(file_path)
    
    # Step 2: Prepare data for HMM
    flow_data = prepare_data_for_hmm(flow_entries)
    
    # Step 3: Train the HMM model
    model = train_hmm_model(flow_data)
    
    # Step 4: Predict the popularity and cache top 10 flow entries
    top_10_entries = predict_popularity_and_cache(flow_data, model)
    
    # Step 5: Display the top 10 entries in cache
    display_top_10_entries(top_10_entries)

# Run the main function
if __name__ == '__main__':
    main()
