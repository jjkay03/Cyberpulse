# Cyberpulse Collector module by jjkay03

from .logger import log  # Cyberpulse modules
import socket
import getpass

# Function: Gets the name of the PC
def collect_pc_name():
    pc_name = socket.gethostname()
    log(f"Fetching PC name: '{pc_name}'", debug=True)
    return pc_name

# Function: Gets the name of the PC user
def collect_pc_user_name():
    pc_user_name = getpass.getuser()
    log(f"Fetching PC user name: '{pc_user_name}'", debug=True)
    return pc_user_name