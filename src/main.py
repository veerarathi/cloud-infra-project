import sys
import json
from aws_services import validate_config

def run_provisioner(config_path):
    print(f"--- Initializing Cloud Provisioner ---")
    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
            
      
        print(f"Strategy:{config.get('strategy', 'Rehosting')}")
        print(f"Deploying to:{config.get('region', 'us-east-1')}")
        
     
        if validate_config(config):
            print("Status: Infrastructure Plan Validated Successfully.")
            
        else:
            print("Status: Validation Failed. Check Resource Constraints.")
            
    except FileNotFoundError:
        print(f"Error: {config_path} not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_config_json>")
    else:
        run_provisioner(sys.argv[1])
