# DBL - Dosbox Launcher

This is a simple python utility to launch DOSBox games on macOS.

## Assumptions

Games are installed using the following structure.

- game_folder_name
  - dosbox.conf or dosbox-x.conf
  - C.disk or C.harddrive folder

## Dependencies

You need to install dosbox-x

## Usage

dbl <game_folder_name>

This will startup Dosbox, load a custom config file if it is present and mount the disk folder.
It's up to you to install and launch the game.


