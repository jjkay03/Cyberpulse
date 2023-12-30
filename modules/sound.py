# Cyberpulse sound module by jjkay03

from .logger import log  # Cyberpulse modules
import winsound


winsound_list = [
    "SystemAsterisk",
    "SystemExclamation",
    "SystemExit",
    "SystemHand",
    "SystemQuestion"
]


# Function: Plays a windows default sound
def winsound(index):
    winsound.PlaySound(winsound_list[index], winsound.SND_ALIAS)
    log(f"Playing winsound: '{winsound_list[index]}'", debug=True)