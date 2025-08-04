import logging
from pathlib import Path
import json
import subprocess
from functions import get_vm_details, validate_vm_details, ask_user_for_flag, create_virtual_machine


log_file = (Path(__file__).parent / "../logs/provisioning.log").resolve()
log_file.parent.mkdir(parents=True, exist_ok=True)

config_file = (Path(__file__).parent / "../configs/instances.json").resolve()
config_file.parent.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)
logger = logging.getLogger(Path(__file__).name)



flag = ask_user_for_flag("Do you want to create a new virtual machine? (y/n): ")

while flag:
    vm_name, cpu, memory, disk, os = get_vm_details()
    errors = validate_vm_details(vm_name, cpu, memory, disk, os)
    if errors:
        for error in errors:
            logger.warning(error)
        flag = ask_user_for_flag("Do you want to create a new virtual machine? (y/n): ")
        continue
    
    if os == 'win' or os == 'w':
        os = 'windows'
    elif os == 'lin' or os == 'l':
        os = 'linux'

    try:
        vm = create_virtual_machine(vm_name, cpu, memory, disk, os, config_file)
        logger.info(f"created vm: {str(vm)} successfully")

    except Exception as e:
        logger.error(f"An error occurred while creating the virtual machine: {e}")

    flag = ask_user_for_flag("Do you want to create another virtual machine? (y/n): ")


install_nginx_flag = ask_user_for_flag("Would you like to install nginx on all machine instances? (y/n): ")


if install_nginx_flag:
    nginx_script = (Path(__file__).parent / "../scripts/install_nginx.sh").resolve()
    with open(config_file, 'r') as f:
        data = json.load(f)
        for machine in data:
            try:
                subprocess.run(['bash', str(nginx_script), machine['name']], check=True)
                logger.info(f"Successfully installed nginx on {machine['name']}")
            except subprocess.CalledProcessError as e:
                logger.error(f"Failed to install nginx on {machine['name']}: {e}")