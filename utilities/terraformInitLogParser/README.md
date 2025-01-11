# Terraform Init Log Parser
[`terraform init`]

This script parses a Terraform `init` log file, extracts module details, and generates a hierarchical tree structure representing the relationships between parent and child modules. The output is displayed in a structured tree format and saved as a text file (`terraform_tree_report.txt`).

---

## What This Script Does

1. **Parses Terraform `init` Logs**:
   - Extracts information about modules, including:
     - Module URL
     - Module version
     - Module name

2. **Builds a Tree Structure**:
   - Constructs a parent-child hierarchy for nested modules based on naming conventions.

3. **Generates Readable Output**:
   - Displays a clean and visually intuitive tree structure in the terminal.
   - Saves the output to a file (`terraform_tree_report.txt`).

4. **Custom Formatting**:
   - Displays the module name, URL, and version in the format:
     ```
     module_name - module_url (module_version)
     ```

---

## Prerequisites

Before using this script, ensure you have the following:

1. **Python**:
   - Install Python 3.6 or higher.

2. **Dependencies**:
   - Install the `anytree` Python library for rendering the tree structure:
     ```bash
     pip install anytree
     ```

3. **Terraform `init` Log File**:
   - Ensure you have a Terraform `init` log file (e.g., `tfinit.log`) that contains module information.

---

## Preparation and Run

1. **Save the Script**:
   - Save the script as `tfinit_parsing.py`.

2. **Prepare the Log File**:
   - Ensure the Terraform `init` log file (`tfinit.log`) is in the same directory as the script.

3. **Run the Script**:
   - Execute the script with the following command:
     ```bash
     python tfinit_parsing.py tfinit.log
     ```

4. **View the Output**:
   - The hierarchical tree structure will be displayed in the terminal.
   - A file named `terraform_tree_report.txt` will be created with the same tree structure.


---

## Expected Result

1. **Terminal Output**:
   - A hierarchical tree structure will be displayed in the terminal.

2. **Generated Report**:
   - A file named `terraform_tree_report.txt` will be created in the same directory, containing the same tree structure.

### Example Output
For the given input log:
```
Initializing the backend...

Successfully configured the backend "gcs"! Terraform will automatically
8use this backend unless the backend configuration changes.

Upgrading modules...
Downloading github.com/someproject/run_cloud_svc/gcp 1.0.13 for module-one...
- module-one in .terraform/modules/module-one

Downloading github.com/someproject/service-account/gcp 1.0.2 for module-one.module-two...
- module-one.module-two in .terraform/modules/module-one.module-two

Downloading registry.terraform.io/terraform-google-modules/service-accounts/google 4.4.3 for module-one.module-two.module-three...
- module-one.module-two.module-three in .terraform/modules/module-one.module-two/module-three

Downloading github.com/someproject/modules/module-one.module-four 2.0.0 for module-one.module-four...
- module-one.module-four in .terraform/modules/module-one.module-four

Downloading registry.terraform.io/terraform-google-modules/redis/memorystore 1.1.0 for module-five.module-six...
- module-five.module-six in .terraform/modules/module-five.module-six

Downloading github.com/someproject/shared-labels/gcp 1.0.0 for module-seven...
- module-seven in .terraform/modules/module-seven

Downloading registry.terraform.io/googlecloudplatform/secret-manager/google 0.2.0 for module-eight.module-nine...
- module-eight.module-nine in .terraform/modules/module-eight.module-nine

Terraform has been successfully initialized!

```

The output tree will be:
```
Terraform Modules
├── module-one
│   ├── module-two - github.com/someproject/service-account/gcp (1.0.2)
│   │   └── module-three - registry.terraform.io/terraform-google-modules/service-accounts/google (4.4.3)
│   └── module-four - github.com/someproject/modules/module-one.module-four (2.0.0)
├── module-five
│   └── module-six - registry.terraform.io/terraform-google-modules/redis/memorystore (1.1.0)
├── module-seven
│   └── module-seven - github.com/someproject/shared-labels/gcp (1.0.0)
└── module-eight
    └── module-nine - registry.terraform.io/googlecloudplatform/secret-manager/google (0.2.0)
```

---

## Benefits

1. **Enhanced Debugging**:
   - Helps DevOps teams quickly identify and visualize the dependency tree of Terraform modules, including nested and shared modules.

2. **Improved Collaboration**:
   - Provides a clear representation of module relationships, making it easier for teams to understand how infrastructure is structured.

3. **Simplifies Troubleshooting**:
   - Identifies missing or incorrectly referenced parent modules, reducing the time spent debugging complex Terraform configurations.

4. **Automation-Friendly**:
   - The script generates outputs that can be easily integrated into CI/CD pipelines for better monitoring of Terraform runs.

---

## Solving Real-Life Problems for DevOps Teams

1. **Dependency Management**:
   - Terraform configurations often involve multiple nested modules, which can be challenging to manage. This script provides a clear, hierarchical visualization of how modules are interconnected.

2. **Infrastructure Troubleshooting**:
   - When a Terraform run fails due to module issues, this script can help pinpoint the problem by showing the exact hierarchy and missing dependencies.

3. **Documentation and Auditing**:
   - Automatically generates a readable tree report, which can be used as documentation for the Terraform project or as an audit trail for compliance purposes.

4. **Simplifying Onboarding**:
   - New team members can quickly understand the structure of Terraform projects by referring to the generated report.

---
