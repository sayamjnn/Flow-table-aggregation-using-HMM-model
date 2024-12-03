import re
import sys

# Function to parse a single flow entry
def parse_flow_entry(flow_rule):
    # Match MAC address pattern (6 groups of 2 hexadecimal digits)
    mac_regex = r'([0-9a-fA-F]{2}):([0-9a-fA-F]{2}):([0-9a-fA-F]{2}):([0-9a-fA-F]{2}):([0-9a-fA-F]{2}):([0-9a-fA-F]{2})'
    
    dl_src_match = re.search(f'dl_src={mac_regex}', flow_rule)
    dl_dst_match = re.search(f'dl_dst={mac_regex}', flow_rule)
    action_match = re.search(r'actions=([^,]+)', flow_rule)

    # Extract full MAC address if matches are found
    dl_src = ':'.join(dl_src_match.groups()) if dl_src_match else None
    dl_dst = ':'.join(dl_dst_match.groups()) if dl_dst_match else None
    action = action_match.group(1) if action_match else None

    # If any of the essential parts are missing, skip this rule
    if not dl_src or not dl_dst or not action:
        print(f"Warning: Invalid rule, missing dl_src, dl_dst, or action in flow rule: {flow_rule}")
        return None

    return (dl_src, dl_dst, action)

# Function to convert flow_rules2 to flow_rules
def convert_flow_rules(flow_rules2):
    flow_rules = []
    
    for rule in flow_rules2:
        parsed_rule = parse_flow_entry(rule)
        if parsed_rule:
            flow_rules.append(parsed_rule)
    
    return flow_rules

# Main function to handle file reading and writing
def process_flow_rules(input_file, output_file=None):
    # Read flow rules from input file
    flow_rules2 = []
    with open(input_file, 'r') as infile:
        flow_rules2 = [line.strip() for line in infile if line.strip()]

    # Convert the flow rules
    converted_flow_rules = convert_flow_rules(flow_rules2)

    # Write output to file or print to console
    if output_file:
        with open(output_file, 'w') as outfile:
            for rule in converted_flow_rules:
                outfile.write(f"{rule}\n")
        print(f"Converted flow rules have been written to {output_file}")
    else:
        for rule in converted_flow_rules:
            print(rule)

# Entry point of the script
if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <input_file> [output_file]")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) == 3 else None

    process_flow_rules(input_filename, output_filename)

