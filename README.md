# Infrastructure Simulator

A Python-based virtual machine provisioning and management simulator that allows users to create, configure, and manage virtual machine instances with automated service installation capabilities.

## 🚀 Features

- **Interactive VM Creation**: Create virtual machines with custom specifications through an intuitive command-line interface
- **Input Validation**: Comprehensive validation for VM parameters including CPU, memory, disk, and operating system
- **Configuration Management**: Persistent storage of VM configurations in JSON format
- **Automated Service Installation**: Install nginx on all created VM instances with a single command
- **Comprehensive Logging**: Detailed logging system for tracking operations and troubleshooting
- **Cross-Platform Support**: Supports both Windows and Linux virtual machines
- **Duplicate Prevention**: Prevents creation of VMs with duplicate names

## 📁 Project Structure

```
project_new_version/
├── configs/
│   └── instances.json          # VM configuration storage
├── logs/
│   └── provisioning.log        # Application logs
├── scripts/
│   └── install_nginx.sh        # Nginx installation script
├── src/
│   ├── infra_simulator.py      # Main application entry point
│   ├── functions.py            # Core utility functions
│   ├── machine.py              # VirtualMachine data model
│   └── __pycache__/           # Python bytecode cache
├── venv/                       # Python virtual environment
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

## 🛠️ Prerequisites

- **Python 3.7+** (Recommended: Python 3.8 or higher)
- **pydantic** library for data validation
- **bash** (for nginx installation script execution)

## 📦 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MaorIdi/final_project_new_version.git
   cd project_new_version
   ```

2. **Create and activate a virtual environment:**

   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\Activate.ps1

   # Windows (Command Prompt)
   python -m venv venv
   venv\Scripts\activate.bat

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install pydantic
   ```

## 🎯 Usage

### Running the Application

Navigate to the project directory and run the main simulator:

```bash
cd src
python infra_simulator.py
```

### Interactive Workflow

1. **VM Creation Process:**

   - The application will prompt you to create a new virtual machine
   - Enter the required specifications:
     - VM Name (unique identifier)
     - CPU count (positive integer)
     - Memory amount (positive integer, in GB)
     - Disk size (positive integer, in GB)
     - Operating System (windows/linux or abbreviated forms)

2. **Input Validation:**

   - All inputs are validated for correctness
   - Invalid inputs will display warnings and prompt for re-entry
   - Duplicate VM names are prevented

3. **Multiple VM Creation:**

   - After creating a VM, you can choose to create additional machines
   - Each VM is stored in the configuration file

4. **Service Installation:**
   - Option to automatically install nginx on all created VM instances
   - Uses the included bash script for installation

### Example Usage Session

```
Do you want to create a new virtual machine? (y/n): y
Enter the name of the virtual machine: web-server-01
Enter the number of CPUs: 2
Enter the amount of memory: 4
Enter the size of the disk: 20
Enter the operating system (windows/linux): linux

2025-08-04 10:30:15 - INFO - infra_simulator.py - created vm: name='web-server-01' ram=4.0 cpu=2.0 storage=20.0 os='linux' successfully

Do you want to create another virtual machine? (y/n): n
Would you like to install nginx on all machine instances? (y/n): y

2025-08-04 10:30:20 - INFO - infra_simulator.py - Successfully installed nginx on web-server-01
```

## 📊 Data Models

### VirtualMachine Class

The `VirtualMachine` class uses Pydantic for data validation:

```python
class VirtualMachine(BaseModel):
    name: str        # Unique VM identifier
    ram: float       # Memory in GB
    cpu: float       # Number of CPU cores
    storage: float   # Disk size in GB
    os: str         # Operating system (windows/linux)
```

### Configuration Storage

VM configurations are stored in `configs/instances.json`:

```json
[
  {
    "name": "web-server-01",
    "ram": 4.0,
    "cpu": 2.0,
    "storage": 20.0,
    "os": "linux"
  },
  {
    "name": "db-server",
    "ram": 8.0,
    "cpu": 4.0,
    "storage": 100.0,
    "os": "windows"
  }
]
```

## 🔧 Core Functions

### `get_vm_details()`

Collects VM specifications from user input through interactive prompts.

### `validate_vm_details(vm_name, cpu, memory, disk, os)`

Validates all VM parameters and returns a list of validation errors if any exist.

### `create_virtual_machine(vm_name, cpu, memory, disk, os, config_file)`

Creates a new VirtualMachine instance and persists it to the configuration file.

### `ask_user_for_flag(message)`

Utility function for yes/no user prompts, returns boolean based on user input.

## 📝 Logging

The application implements comprehensive logging with:

- **File Logging**: All operations logged to `logs/provisioning.log`
- **Console Output**: Real-time logging to terminal
- **Structured Format**: Timestamp, log level, module name, and message
- **Log Levels**: INFO for successful operations, WARNING for validation issues, ERROR for failures

### Log Format

```
2025-08-04 10:30:15 - INFO - infra_simulator.py - created vm: web-server-01 successfully
2025-08-04 10:30:20 - ERROR - infra_simulator.py - Failed to install nginx on web-server-01: Command failed
```

## 🖥️ Supported Operating Systems

The simulator supports the following OS inputs (case-insensitive):

- **Windows**: `windows`, `win`, `w`
- **Linux**: `linux`, `lin`, `l`

All abbreviated forms are automatically expanded to full names during processing.

## 🔨 Scripts

### `install_nginx.sh`

Bash script for automated nginx installation on VM instances:

```bash
#!/bin/bash
# This script installs nginx on a machine instance based on its name.

vm_name=$1

if [[ ! -z $vm_name ]]; then
    sleep 2  # Simulated installation process
else
    echo "Please pass vm_name as an argument."
    exit 1
fi
```

**Usage:** The script is automatically called by the main application when nginx installation is requested.

## 🚨 Error Handling

The application includes robust error handling for:

- **File I/O Operations**: Handles missing configuration files gracefully
- **JSON Parsing**: Creates new configuration files if corrupted
- **Subprocess Execution**: Catches and logs nginx installation failures
- **Input Validation**: Comprehensive parameter validation with user-friendly error messages
- **Duplicate Names**: Prevents VM name conflicts

## 🔍 Troubleshooting

### Common Issues

1. **Permission Errors:**

   - Ensure write permissions for `configs/` and `logs/` directories
   - Run with appropriate privileges if needed

2. **Missing Dependencies:**

   ```bash
   pip install pydantic
   ```

3. **Bash Script Execution Issues:**

   - Ensure bash is available in your system PATH
   - On Windows, consider using Git Bash or WSL

4. **JSON Configuration Corruption:**
   - Delete `configs/instances.json` to reset configuration
   - The application will create a new file automatically

### Debugging

- Check `logs/provisioning.log` for detailed operation history
- Enable verbose logging by modifying the logging level in `infra_simulator.py`
- Verify VM configurations in `configs/instances.json`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Development Guidelines

- Follow PEP 8 coding standards
- Add comprehensive docstrings to new functions
- Include appropriate error handling
- Update tests for new features
- Maintain backward compatibility

## 🔮 Future Enhancements

- [ ] Web-based dashboard for VM management
- [ ] Support for additional operating systems
- [ ] VM resource monitoring and alerts
- [ ] Automated backup and snapshot functionality
- [ ] Integration with cloud providers (AWS, Azure, GCP)
- [ ] Docker container support
- [ ] REST API for programmatic access
- [ ] VM templates and cloning capabilities

## ‍💻 Author

**Maor Idi** - [@MaorIdi](https://github.com/MaorIdi)

---

_Last updated: August 6, 2025_
