#!/bin/bash

# List of switches (adjust this list as per your topology)
SWITCHES=("s1" "s2" "s3" "s4" "s5")

# Directory for storing temporary and final output files
OUTPUT_DIR="./flows_output"
mkdir -p $OUTPUT_DIR

# Function to process flows with process.py
process_with_process_py() {
    local input_file=$1
    local output_file=$2
    echo "Running process.py on $input_file..."
    python3 FlowProcessing.py "$input_file" "$output_file"
}

# Function to run algorithm.py on the processed file
process_with_algorithm_py() {
    local input_file=$1
    local output_file=$2
    echo "Running algorithm.py on $input_file..."
    python3 EntryAggregstion.py "$input_file" > "$output_file"
}

# Loop through each switch
for SWITCH in "${SWITCHES[@]}"; do
    echo "Processing switch $SWITCH..."

    # Step 1: Dump the flows for the current switch
    FLOW_FILE="$OUTPUT_DIR/flows_$SWITCH.txt"
    echo "Fetching flows for $SWITCH..."
    sudo ovs-ofctl -O OpenFlow13 dump-flows $SWITCH > "$FLOW_FILE"

    # Step 2: Process flows with process.py
    STEP1_FILE="$OUTPUT_DIR/step1.txt"
    process_with_process_py "$FLOW_FILE" "$STEP1_FILE"
    
    # Step 3: Process the step1.txt with algorithm.py
    COMPRESSED_FILE="$OUTPUT_DIR/compressedfile.txt"
    process_with_algorithm_py "$STEP1_FILE" "$COMPRESSED_FILE"
    
    # Clean up the temporary files for the next switch
    #echo "Cleaning up temporary files for $SWITCH..."
    #rm "$FLOW_FILE" "$STEP1_FILE"

    echo "Finished processing switch $SWITCH."
done

echo "Flow processing complete for all switches!"

