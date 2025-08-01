from machine import VirtualMachine
from pydantic import ValidationError
import logging
from pathlib import Path
import json

log_file = (Path(__file__).parent / '../logs/provisioning.log').resolve()
log_file.parent.mkdir(parents=True, exist_ok=True)

config_file = (Path(__file__).parent / '../configs/instances.json').resolve()
config_file.parent.mkdir(parents=True, exist_ok=True)



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(Path(__file__).name)



vm_name = input("Enter the name of the virtual machine: ")
cpu = input("Enter the number of CPUs: ")
memory = input("Enter the amount of memory: ")
disk = input("Enter the size of the disk: ")
os = input("Enter the operating system: ")



try:
    
    vms = []
    
    
    vm = VirtualMachine(
        name= vm_name,
        ram= memory,
        cpu= cpu,
        os= os,
        storage= disk
    ) 


    try:
        with open(config_file, 'r') as f:
            data = json.load(f)
            
    except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
        with open(config_file, 'w') as f:
            json.dump([], f)

        
    vms.append(dict(vm))
    
    with open(config_file, 'w') as f:
        json.dump(vms, f)
       
    logger.info(f"created vm: {vm} successfully") 
    
except ValidationError as e:        
    for error in e.errors():
        field = error['loc'][0]

        if field == 'os':
            error['msg'] = "Invalid operating system format. Please use a valid OS name."
        
        logger.info(f"'{field}': {error['msg']}")

except Exception as e:
    logger.error(f'An error occured: {e}')