# Cyberpulse communicator module by jjkay03

import subprocess

note_number = 1

def notepad(messages):
    global note_number

    temp_notepad_path = f"temp/note_{note_number}.txt"
    note_number += 1

    # Write messages to the temporary file
    with open(temp_notepad_path, 'w') as temp_file:
        temp_file.write(messages)

    # Open Notepad with the temporary file
    subprocess.Popen(['notepad.exe', temp_notepad_path])