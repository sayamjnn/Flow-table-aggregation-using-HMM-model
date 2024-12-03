from itertools import groupby
from operator import itemgetter

# Convert MAC address to binary string
def mac_to_binary(mac):
    mac_parts = mac.split(":")
    binary_str = ''.join(f'{int(part, 16):08b}' for part in mac_parts)
    return binary_str

# Convert binary string back to MAC address
def binary_to_mac(binary):
    mac_parts = [f'{int(binary[i:i+8], 2):02x}' for i in range(0, 48, 8)]
    return ':'.join(mac_parts)

# Function to find common prefix and create a masked MAC address
def create_masked_mac(mac_list):
    if not mac_list:
        return ""
    
    # Determine the common prefix length
    prefix_length = 0
    for i in range(48):
        bit_values = {mac[i] for mac in mac_list}
        if len(bit_values) > 1:  # More than one distinct bit value
            break
        prefix_length += 1

    # Generate masked MAC address
    common_prefix = mac_list[0][:prefix_length]
    masked_mac_binary = common_prefix.ljust(48, '0')
    return binary_to_mac(masked_mac_binary)

# Perform MAC address minimization and aggregation
def minimize_mac_addresses(entries):
    # Extract unique binary source MAC addresses
    src_macs = list(set(mac_to_binary(src) for src, _, _ in entries))
    dst_mac = entries[0][1]  # Destination MAC is same for this group
    action = entries[0][2]   # Action is same for this group

    # Create a single entry with a masked MAC address for similar source MACs
    masked_mac = create_masked_mac(src_macs)
    
    # Return the minimized entry
    return [(masked_mac, dst_mac, action)]

# Function to aggregate entries with mask extension
def entry_aggregation_with_mask_extension(flow_entries):
    # Sort by destination MAC and action
    flow_entries.sort(key=itemgetter(1, 2))
    grouped_entries = []
    
    # Group by destination MAC and action
    for key, group in groupby(flow_entries, key=itemgetter(1, 2)):
        group_list = list(group)
        minimized_mac_entries = minimize_mac_addresses(group_list)
        grouped_entries.extend(minimized_mac_entries)

    return grouped_entries

# Function to read flow rules from a file
def read_flow_rules_from_file(file_name):
    flow_rules = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Remove leading/trailing whitespace and handle tuple format
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                
                # Check for tuple-like format
                if line.startswith("(") and line.endswith(")"):
                    line = line[1:-1]  # Remove parentheses
                    parts = line.split(", ")
                    if len(parts) == 3:
                        src_mac = parts[0].strip("'")
                        dst_mac = parts[1].strip("'")
                        action = parts[2].strip("'")
                        flow_rules.append((src_mac, dst_mac, action))
                    else:
                        print(f"Invalid tuple format in line: {line}")
                else:
                    print(f"Invalid format in line: {line}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    return flow_rules

# Main function
def main():
    # Check if the file name is provided in command line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <flow_rules_file>")
        sys.exit(1)
    
    file_name = sys.argv[1]

    # Read flow rules from the specified file
    flow_rules = read_flow_rules_from_file(file_name)

    # Apply the aggregation and minimization
    minimized_flow_entries = entry_aggregation_with_mask_extension(flow_rules)

    # Output the minimized flow entries
    print("Minimized Flow Entries:")
    for src, dst, action in minimized_flow_entries:
        print(f"dl_src: {src}, dl_dst: {dst}, action: {action}")

# Run the main function
if __name__ == "__main__":
    import sys
    main()

