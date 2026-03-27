import os
import json
import datetime

def log_status(message, level="INFO"):
    """
    Standardizes console output with timestamps for professional logging.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def validate_file_extension(filepath, extension=".json"):
    """
    Ensures the user is providing the correct file type via CLI.
    """
    return filepath.lower().endswith(extension)

def load_schema_config(filepath):
    """
    Safely loads and parses the JSON configuration file.
    """
    if not os.path.exists(filepath):
        log_status(f"File not found: {filepath}", "ERROR")
        return None
        
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            log_status(f"Configuration loaded: {os.path.basename(filepath)}")
            return data
    except json.JSONDecodeError:
        log_status("Failed to decode JSON. Check file syntax.", "ERROR")
        return None

def calculate_resource_count(config):
    """
    A utility to summarize the infrastructure plan.
    """
    resources = config.get("resources", [])
    return len(resources)
