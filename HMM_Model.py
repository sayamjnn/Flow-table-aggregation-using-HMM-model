import numpy as np
from hmmlearn import hmm

# Example flow entries with their match counts (in a real-world scenario, this data would come from the network)
# Each entry is represented by a tuple: (flow_entry, counter)
flow_entries = [
    ('flow1', 50),
    ('flow2', 120),
    ('flow3', 200),
    ('flow4', 80),
    ('flow5', 150),
    ('flow6', 60),
    ('flow7', 220),
    ('flow8', 180),
    ('flow9', 130),
    ('flow10', 90),
    ('flow11', 75),
    ('flow12', 160),
    ('flow13', 95),
    ('flow14', 50),
]

# Step 1: Prepare the data (flow entries and counters)
# For the sake of simplicity, we consider the "counter" as the observation and treat it as a continuous variable
# Convert the flow entry counters to a numpy array of shape (n_samples, n_features)
X = np.array([entry[1] for entry in flow_entries]).reshape(-1, 1)

# Step 2: Define the HMM model
# We need to define the number of states. For simplicity, we will use 3 states (low, medium, high popularity).
model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=1000)

# Step 3: Train the HMM with the flow entry counters
model.fit(X)

# Step 4: Predict the popularity state for each flow entry based on its counter
states = model.predict(X)

# Step 5: Assign states back to the flow entries
flow_state_data = [(flow_entries[i][0], flow_entries[i][1], states[i]) for i in range(len(flow_entries))]

# Step 6: Sort entries by their match count (the most popular ones) and cache top 10
# Sort by counter (descending order) and then pick the top 10
top_10_entries = sorted(flow_state_data, key=lambda x: x[1], reverse=True)[:10]

# Display the top 10 popular entries and their predicted states
print("Top 10 Popular Flow Entries in Cache:")
for entry in top_10_entries:
    flow_entry, counter, state = entry
    print(f"Flow Entry: {flow_entry}, Counter: {counter}, Predicted State: {state}")

# Step 7: If you want to predict the future popularity, you can also use the model for forecasting.
# For example, predict the next state of a new flow entry with a specific counter:
new_flow_counter = np.array([[160]])  # New flow entry with counter 160
predicted_state = model.predict(new_flow_counter)
print(f"\nPredicted state for a new flow entry with counter {new_flow_counter[0][0]}: {predicted_state[0]}")

