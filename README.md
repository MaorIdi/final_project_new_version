# Virtual Machine Infrastructure Simulator

A Python-based infrastructure simulator that allows you to create and manage virtual machine configurations with automated nginx installation capabilities.

## Features

- 🖥️ **Virtual Machine Creation**: Create virtual machines with customizable CPU, memory, storage, and OS specifications
- 📝 **Configuration Management**: Persistent storage of VM configurations in JSON format
- 🔧 **Automated nginx Installation**: Batch installation of nginx on all created VM instances
- 📋 **Input Validation**: Robust validation using Pydantic models
- 📊 **Comprehensive Logging**: Detailed logging with configurable output (console, file, or both)
- 🛡️ **Error Handling**: Graceful error handling and user-friendly error messages

## Project Structure

```
final_project_new_version/
├── configs/
│   └── instances.json          # VM configurations storage
├── logs/
│   └── provisioning.log        # Application logs
├── scripts/
│   └── install_nginx.sh        # nginx installation script
├── src/
│   ├── functions.py            # Core functionality functions
│   ├── infra_simulator.py      # Main application entry point
│   └── machine.py              # VirtualMachine model definition
└── requirements.txt            # Python dependencies
```

## Requirements

- Python 3.7+
- Bash shell (for nginx installation script)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd final_project_new_version
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

Navigate to the `src` directory and run the main simulator:

```bash
cd src
python infra_simulator.py
```

### Interactive Workflow

The application provides an interactive command-line interface:

1. **Create Virtual Machines:**
   - Enter VM name, CPU count, memory (GB), storage (GB), and operating system
   - Supported OS options: `windows`, `win`, `w`, `linux`, `lin`, `l`
   - Continue creating multiple VMs as needed

2. **nginx Installation:**
   - Option to install nginx on all created VM instances
   - Automated execution across all configured machines

### Configuration

#### Environment Variables

- `LOG_OUTPUT`: Controls logging output destination
  - `console`: Log to console only
  - `file`: Log to file only  
  - `both`: Log to both console and file (default)

#### Example Usage

```bash
# Log only to console
LOG_OUTPUT=console python infra_simulator.py

# Log only to file
LOG_OUTPUT=file python infra_simulator.py
```

## Virtual Machine Specifications

### Supported Operating Systems
- **Windows**: `windows`, `win`, `w`
- **Linux**: `linux`, `lin`, `l`

### Resource Requirements
- **CPU**: Must be greater than 0
- **Memory**: Must be greater than 0 (GB)
- **Storage**: Must be greater than 0 (GB)

### Example VM Configuration
```json
{
  "name": "web-server-01",
  "memory": 4.0,
  "cpu": 2.0,
  "storage": 50.0,
  "os": "linux"
}
```

## File Descriptions

### Core Files

- **`src/infra_simulator.py`**: Main application entry point with user interaction loop
- **`src/machine.py`**: Pydantic model for VirtualMachine with validation rules
- **`src/functions.py`**: Core utility functions for VM creation and user input handling

### Configuration Files

- **`configs/instances.json`**: Persistent storage for VM configurations
- **`logs/provisioning.log`**: Application logs and error tracking

### Scripts

- **`scripts/install_nginx.sh`**: Bash script for simulating nginx installation on VMs

## Error Handling

The application includes comprehensive error handling for:

- **Validation Errors**: Invalid VM specifications (CPU, memory, storage values)
- **Duplicate Names**: Prevents creation of VMs with existing names
- **File System Errors**: Handles missing or corrupted configuration files
- **Process Execution**: Manages nginx installation script failures

## Logging

Detailed logging includes:

- VM creation success/failure
- Validation errors with specific field information
- nginx installation progress and errors
- System-level errors and warnings

Log format: `YYYY-MM-DD HH:MM:SS - LEVEL - MODULE - MESSAGE`

## Dependencies

- **pydantic**: Data validation and settings management
- **annotated-types**: Type annotations support
- **typing-extensions**: Extended typing support

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## Support

For questions or issues, please open an issue in the GitHub repository or contact the development team.

---

**Note**: This is a simulation tool for educational and development purposes. No actual virtual machines are created or managed.
