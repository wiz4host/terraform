###########################################################################
#This script parses a Terraform init log file, extracts module details, 
#and generates a hierarchical tree structure representing the
#relationships between parent and child modules. The output is displayed 
#in a structured tree format and saved as a text file 
#(terraform_tree_report.txt).

Date: 11/01/2025
###########################################################################
#USAGE:  python tfInit_moduleMap_Parser.py tfinit.log
###########################################################################

import re
from anytree import Node, RenderTree, ContStyle
import os

def parse_terraform_init_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Use the specified pattern
    module_pattern = r"Downloading (.+?) (\d\.\d.\d).for(.+?)(.+)..."

    # Initialize dictionaries to store nodes and roots
    nodes = {}
    root_nodes = {}

    for line in lines:
        match = re.search(module_pattern, line)
        if match:
            url = match.group(1).strip()       # URL
            version = match.group(2).strip()  # Version
            module_name = match.group(4).strip()  # Module Name fetched from group(4)

            # Extract the top-level parent module
            top_level_name = module_name.split('.')[0]

            # Create the node for the module with the version at the end
            current_node = Node(f"{module_name.split('.')[-1]} - {url} ({version})")

            # If it's a top-level module, ensure it's marked as root
            if top_level_name not in root_nodes:
                root_nodes[top_level_name] = Node(top_level_name)

            # Attach the module to its parent in the hierarchy
            if '.' in module_name:
                parent_name = '.'.join(module_name.split('.')[:-1])
                parent_node = nodes.get(parent_name)
                if parent_node:
                    current_node.parent = parent_node
                else:
                    # If the parent doesn't exist, attach it directly to the top-level root
                    current_node.parent = root_nodes[top_level_name]
            else:
                # Directly attach top-level modules to the root node
                current_node.parent = root_nodes[top_level_name]

            # Store the current node in the dictionary
            nodes[module_name] = current_node

    # Create a virtual root to group all top-level modules
    virtual_root = Node("Terraform Modules")
    for root in root_nodes.values():
        root.parent = virtual_root

    return virtual_root

def generate_tree_report(tree_root):
    report = []
    for pre, _, node in RenderTree(tree_root, style=ContStyle()):
        report.append(f"{pre}{node.name}")
    return report

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python tfinit_parsing.py <tfinit.log>")
        sys.exit(1)

    # Input file containing the Terraform init logs
    input_file = sys.argv[1]

    # Validate if the file exists
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        sys.exit(1)

    # Parse the log and generate the tree structure
    tree_root = parse_terraform_init_log(input_file)

    # Generate the report
    if tree_root:
        tree_report = generate_tree_report(tree_root)

        # Save the report to a text file (use utf-8 encoding)
        output_file = "terraform_tree_report.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(tree_report))

        # Display the report to the user
        for line in tree_report:
            print(line)
    else:
        print("No modules found in the log.")
