#!/bin/bash

# Path to the get_Script.sh file
get_script_path="/home/onos/dynamic_routing/mininet/SDN-Project/ryu/getflows.sh"

# Path to the HMM_model.py script
hmm_model_path="/home/onos/dynamic_routing/mininet/SDN-Project/HMM_Model_scripts/HMM_model_script.py"

# Paths to the four Python scripts
python_script_1="/home/onos/dynamic_routing/mininet/SDN-Project/HMM_Model_scripts/flow.py"
python_script_2="/home/onos/dynamic_routing/mininet/SDN-Project/HMM_Model_scripts/extableMatch.py"
python_script_3="/home/onos/dynamic_routing/mininet/SDN-Project/HMM_Model_scripts/proposed.py"
python_script_4="/home/onos/dynamic_routing/mininet/SDN-Project/HMM_Model_scripts/graph.py"


# Step 2: Execute HMM_model.py and display the output
echo "Executing HMM_model.py..."
python3 $hmm_model_path
if [ $? -ne 0 ]; then
    echo "Error: HMM_model.py execution failed!"
    exit 1
fi

# Step 3: Execute the first Python script and display the output
echo "Executing python_script_1.py..."
python3 $python_script_1
if [ $? -ne 0 ]; then
    echo "Error: python_script_1.py execution failed!"
    exit 1
fi

# Step 4: Execute the second Python script and display the output
echo "Executing python_script_2.py..."
python3 $python_script_2
if [ $? -ne 0 ]; then
    echo "Error: python_script_2.py execution failed!"
    exit 1
fi

# Step 5: Execute the third Python script and display the output
echo "Executing python_script_3.py..."
python3 $python_script_3
if [ $? -ne 0 ]; then
    echo "Error: python_script_3.py execution failed!"
    exit 1
fi

# Step 6: Execute the fourth Python script and display the output
echo "Executing python_script_4.py..."
python3 $python_script_4
if [ $? -ne 0 ]; then
    echo "Error: python_script_4.py execution failed!"
    exit 1
fi

echo "All scripts executed successfully!"
