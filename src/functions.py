import json
from machine import VirtualMachine

def get_vm_details():
    vm_name = input("Enter the name of the virtual machine: ").strip()
    cpu = input("Enter the number of CPUs: ").strip()
    memory = input("Enter the amount of memory: ").strip()
    disk = input("Enter the size of the disk: ").strip()
    os = input("Enter the operating system (windows/linux): ").strip().lower()
    return vm_name, cpu, memory, disk, os

def validate_vm_details(vm_name, cpu, memory, disk, os):
    errors = []
    if not vm_name:
        errors.append("VM name is required.")
    if not cpu:
        errors.append("CPU count is required.")
    elif not cpu.isdigit():
        errors.append("CPU count must be a positive number.")
    elif int(cpu) <= 0:
        errors.append("CPU count must be greater than 0.")

    if not memory:
        errors.append("Memory amount is required.")
    elif not memory.isdigit():
        errors.append("Memory must be a positive number.")
    elif int(memory) <= 0:
        errors.append("Memory must be greater than 0.")

    if not disk:
        errors.append("Disk size is required.")
    elif not disk.isdigit():
        errors.append("Disk size must be a positive number.")
    elif int(disk) <= 0:
        errors.append("Disk size must be greater than 0.")

    valid_os = {'windows', 'linux', 'win', 'lin', 'w', 'l'}
    if not os:
        errors.append("Operating system is required.")
    elif os not in valid_os:
        errors.append("OS name must be one of: 'windows', 'linux', 'win', 'lin', 'w', or 'l'.")

    return errors



def ask_user_for_flag(msg):
    flag = (
    input(msg).strip().lower() == "y"
    )
    return flag 


def create_virtual_machine(vm_name, cpu, memory, disk, os, config_file):
    vm = VirtualMachine(name=vm_name, ram=memory, cpu=cpu, os=os, storage=disk)
    if " " in vm.name:
        vm.name = vm.name.replace(" ", "-")
    try:
        with open(config_file, "r") as f:
            data = json.load(f)
            if vm.name in [machine['name'] for machine in data]:
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
