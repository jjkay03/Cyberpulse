# Cyberpulse Collector module by jjkay03

import socket
import getpass

# Function: Gets the name of the PC
def collect_pc_name():
    return socket.gethostname()

# Function: Gets the name of the PC user
def collect_user_name():
    return getpass.getuser()