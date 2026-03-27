def validate_config(config):
    """
    Checks if the cloud plan meets standard architecture requirements.
    """
    resources = config.get("resources", [])
    

    has_vpc = any(res['type'] == 'VPC' for res in resources)
    

    has_subnets = any(res['type'] == 'Subnet' for res in resources)
    
    return has_vpc and has_subnets
