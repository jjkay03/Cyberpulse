# Cyberpulse notification module by jjkay03

from .logger import log  # Cyberpulse modules
# from notifypy import Notify


icon_path_pc = "assets/icons/pc.ico"

'''
# Function: Sends a windows notification
def notification(app=" ", title=" ", message=" ", icon=" "):
    notification = Notify()
    notification.application_name = app
    notification.title = title
    notification.message = message

    if icon == "pc": notification.icon = icon_path_pc
    else: notification.icon = icon
    
    notification.send()
    log("Sending notification", debug=True)
'''