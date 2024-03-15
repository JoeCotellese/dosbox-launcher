# This script will launch dosbox with for the folder specified by the user
# on the command-line
# Usage: python launcher.py <folder>
# The Folder contains two items:
# a per-game dosbox.conf file and a sub-folder containing the game files

import os
import subprocess
import sys

# Global Config
DOSBOX_LOCATION = "/Applications/dosbox-x.app/Contents/MacOS/dosbox-x"
GAMES_FOLDER = "/Volumes/External/DOSBox"


def main():
    # Check if the user has provided a folder
    if len(sys.argv) < 2:
        print("Usage: python launcher.py <gamename>")
        sys.exit(1)

    # Get the folder name
    game_name = sys.argv[1]

    folder = os.path.join(GAMES_FOLDER, game_name)

    # Check if the folder exists
    if not os.path.exists(folder):
        print("Folder does not exist")
        sys.exit(1)

    # Check if the folder contains a dosbox.conf or a dosbox-x config file
    dosbox_conf = None
    for file in os.listdir(folder):
        if file.lower() == "dosbox.conf" or file.lower() == "dosbox-x.conf":
            print("found config file: ", file)
            dosbox_conf = os.path.join(folder, file)
            break

    if not os.path.exists(dosbox_conf):
        print("missing config file, will assume defaults")
        dosbox_conf = None

    # get a list of all of the subfolders in the folder
    subfolders = [f for f in os.listdir(folder) 
                  if os.path.isdir(os.path.join(folder, f))]
    # find "C.disk or C.harddrive" in subfolders
    for gamedrive in subfolders:
        print("checking for game folder: ", gamedrive)
        if gamedrive == "C.disk" or gamedrive == "C.harddrive":
            print("found game folder: ", gamedrive)
            break
    else:
        print("missing game folder")
        sys.exit(1)
        # change the working directory to the folder
    os.chdir(folder)
    subprocess.run([DOSBOX_LOCATION, "-conf", dosbox_conf, "-c",
                    "mount c " + gamedrive, "-c", "c:"])


if __name__ == "__main__":
    main()
