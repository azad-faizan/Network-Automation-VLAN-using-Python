from netmiko import ConnectHandler
import yaml
from jinja2 import Environment, FileSystemLoader
import logging

# Setup logging for debugging purposes
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_devices(yaml_file='devices.yaml'):
    """Load devices from the YAML configuration file."""
    with open(yaml_file) as f:
        return yaml.safe_load(f)['devices']

def render_vlan_config(vlans, template_file='vlan.j2'):
    """Render VLAN configuration from a Jinja2 template."""
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_file)
    return template.render(vlans=vlans)

def configure_device(device):
    """Connect to a device and apply VLAN configuration."""
    connection = None
    try:
        logging.info(f"Connecting to {device['hostname']} at {device['ip']}...")
        connection = ConnectHandler(
            device_type=device['device_type'],
            host=device['ip'],
            port=device.get('port', 22),
            username=device['username'],
            password=device['password']
            # If needed, add 'secret': device.get('secret')
        )
        
        # Render VLAN config for this device
        vlan_config = render_vlan_config(device['vlans'])
        logging.info(f"Generated configuration:\n{vlan_config}")
        
        # Send configuration commands
        output = connection.send_config_set(vlan_config.splitlines())
        logging.info(f"Configuration output from {device['hostname']}:\n{output}")
    
    except Exception as e:
        logging.error(f"Failed to configure {device['hostname']}: {e}")
    
    finally:
        if connection and connection.is_alive():
            connection.disconnect()
            logging.info(f"Disconnected from {device['hostname']}.")

def main():
    devices = load_devices()
    for device in devices:
        configure_device(device)

if __name__ == '__main__':
    main()
