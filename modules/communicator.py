# Cyberpulse communicator module by jjkay03

from .logger import log  # Cyberpulse modules
import subprocess

note_number = 1

def notepad(messages):
    global note_number

    temp_note_path = f"temp/note_{note_number}.txt"
    note_number += 1

    # Write messages to the temporary file
    with open(temp_note_path, 'w') as temp_file:
        temp_file.write(messages)

    # Open Notepad with the temporary file
    subprocess.Popen(['notepad.exe', temp_note_path])

    log(f"Creating and openning: '{temp_note_path}'", debug=True)