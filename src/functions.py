import json
from machine import VirtualMachine


def get_vm_details():
    vm_name = input("Enter the name of the virtual machine: ").strip()
    cpu = input("Enter the number of CPUs: ").strip()
    memory = input("Enter the amount of memory: ").strip()
    disk = input("Enter the size of the disk: ").strip()
    os = input("Enter the operating system (windows/linux): ").strip().lower()
    return vm_name, cpu, memory, disk, os


def ask_user_for_flag(msg):
    flag = input(msg).strip().lower() == "y"
    return flag


def create_virtual_machine(vm_name, cpu, memory, disk, os, config_file):
    errors = []
    cpu_float = memory_float = disk_float = None

    try:
        cpu_float = float(cpu)
    except ValueError:
        errors.append(f"CPU: '{cpu}' is not a valid number")

    try:
        memory_float = float(memory)
    except ValueError:
        errors.append(f"Memory: '{memory}' is not a valid number")

    try:
        disk_float = float(disk)
    except ValueError:
        errors.append(f"Disk: '{disk}' is not a valid number")

    if errors:
        error_message = "Validation errors found:\n" + "\n".join(
            f"- {error}" for error in errors
        )
        raise ValueError(error_message)

    vm = VirtualMachine(
        name=vm_name, ram=memory_float, cpu=cpu_float, storage=disk_float, os=os
    )

    if " " in vm.name:
        vm.name = vm.name.replace(" ", "-")
    try:
        with open(config_file, "r") as f:
            data = json.load(f)
            if vm.name in [machine["name"] for machine in data]:
                raise ValueError("A machine with that name already exists!")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open(config_file, "w") as f:
            json.dump([], f)
        data = []

    vms = data.copy()
    vms.append(dict(vm))
    with open(config_file, "w") as f:
        json.dump(vms, f)
    return vm
