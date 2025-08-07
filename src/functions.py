import json
from machine import VirtualMachine
from pydantic import ValidationError


def get_vm_details():
    vm_name = input("Enter the name of the virtual machine: ").strip()
    cpu = input("Enter the number of CPUs: ").strip()
    memory = input("Enter the amount of memory: ").strip()
    storage = input("Enter the size of the amount of storage: ").strip()
    os = input("Enter the operating system (windows/linux): ").strip().lower()
    return vm_name, cpu, memory, storage, os


def ask_user_for_flag(msg):
    flag = input(msg).strip().lower() == "y"
    return flag


def create_virtual_machine(vm_name, cpu, memory, storage, os, config_file):
    try:
        if os == "win" or os == "w":
            os = "windows"
        elif os == "lin" or os == "l":
            os = "linux"
        vm = VirtualMachine(
            name=vm_name,
            memory=memory,
            cpu=cpu,
            storage=storage,
            os=os,
        )
    except ValidationError as e:
        raise e

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
