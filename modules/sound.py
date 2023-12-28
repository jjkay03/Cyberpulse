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