import logging
import os
from pathlib import Path
import json
import subprocess
from functions import (
    get_vm_details,
    ask_user_for_flag,
    create_virtual_machine,
)
from pydantic import ValidationError

log_file = (Path(__file__).parent / "../logs/provisioning.log").resolve()
log_file.parent.mkdir(parents=True, exist_ok=True)

config_file = (Path(__file__).parent / "../configs/instances.json").resolve()
config_file.parent.mkdir(parents=True, exist_ok=True)


log_output = os.getenv("LOG_OUTPUT", "both").lower()

handlers = []
if log_output in ["console", "both"]:
    handlers.append(logging.StreamHandler())
if log_output in ["file", "both"]:
    handlers.append(logging.FileHandler(log_file))

if not handlers:
    handlers = [logging.FileHandler(log_file), logging.StreamHandler()]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=handlers,
)
logger = logging.getLogger(Path(__file__).name)


flag = ask_user_for_flag("Do you want to create a new virtual machine? (y/n): ")

while flag:
    vm_name, cpu, memory, disk, os = get_vm_details()

    try:
        vm = create_virtual_machine(vm_name, cpu, memory, disk, os, config_file)
        logger.info(f"created vm: {str(vm)} successfully.")

    except ValidationError as e:
        for error in e.errors():
            field = error["loc"][0]
            if field == "os":
                msg = "Operating system must be one of the following options: w, win, windows, lin, l, linux"
            else:
                msg = error["msg"]

            logger.warning(f"Validation error in field '{field}': {msg}")

        flag = ask_user_for_flag("Do you want to create a new virtual machine? (y/n): ")
        continue

    except Exception as e:
        logger.error(f"An error occurred while creating the virtual machine: {e}")

    flag = ask_user_for_flag("Do you want to create another virtual machine? (y/n): ")


install_nginx_flag = ask_user_for_flag(
    "Would you like to install nginx on all machine instances? (y/n): "
)


if install_nginx_flag:
    nginx_script = (Path(__file__).parent / "../scripts/install_nginx.sh").resolve()
    try:
        with open(config_file, "r") as f:
            data = json.load(f)
            for machine in data:
                try:
                    result = subprocess.run(
                        ["bash", str(nginx_script), machine["name"]],
                        capture_output=True,
                        text=True,
                        check=True,
                    )
                    if result.stdout:
                        for line in result.stdout.strip().split("\n"):
                            logger.info(line)
                    if result.stderr:
                        for line in result.stderr.strip().split("\n"):
                            logger.warning(f"'{machine['name']}': {line}")
                except subprocess.CalledProcessError as e:
                    if e.stderr:
                        for line in e.stderr.strip().split("\n"):
                            logger.error(
                                f"nginx installation failed for '{machine['name']}': {line}"
                            )
                    else:
                        logger.error(str(e))
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open(config_file, "w") as f:
            json.dump([], f)

        logger.error(
            "The configuration file is empty, corrupted or does not exist. Please create a virtual machine first."
        )
