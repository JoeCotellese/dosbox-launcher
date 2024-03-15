# This script will launch dosbox with for the folder specified by the user
# on the command-line
# Usage: python launcher.py <folder>
# The Folder contains two items:
# a per-game dosbox.conf file and a sub-folder containing the game files

import os
import subprocess
import sys


def main():
    # Check if the user has provided a folder
    if len(sys.argv) < 2:
        print("Usage: python launcher.py <folder>")
        sys.exit(1)

    # Get the folder name
    folder = sys.argv[1]

    # Check if the folder exists
    if not os.path.exists(folder):
        print("Folder does not exist")
        sys.exit(1)

    # Check if the folder contains a dosbox.conf file
    dosbox_conf = os.path.join(folder, "dosbox.conf")
    if not os.path.exists(dosbox_conf):
        print("missing config file, will assume defaults")
        dosbox_conf = None

    # load the sub-folder C.harddrive
    gamedrive = os.path.join(folder, "C.harddrive")
    if not os.path.exists(gamedrive):
        print("missing game folder")
        sys.exit(1)

    # Launch dosbox
    DOSBOX_LOCATION = "/Applications/dosbox-x.app/Contents/MacOS/dosbox-x"
    subprocess.run([DOSBOX_LOCATION, "-conf", dosbox_conf, "-c",
                    "mount c " + gamedrive, "-c", "c:", "-c", "exit"])


if __name__ == "__main__":
    main()
