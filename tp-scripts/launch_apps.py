import subprocess
import sys

# Your commands go here
commands = {
    'a': 'echo test works', # test if it works
    'blen': 'blender',
    'vscode': '/usr/bin/code --new-window',
    'obs': '/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=obs com.obsproject.Studio',
    'spotify': '/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=spotify --file-forwarding com.spotify.Client',
    'discord' : '/usr/bin/discord',
    'teams' : 'teams %U',
    'minecraft' : '/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=polymc org.polymc.PolyMC',
    'audacity' : 'audacity'
}

# Get the command-line argument
try:
    arg = sys.argv[1]
except IndexError:
    print("Error: No argument provided.")
    sys.exit()

# Check if the argument is valid
if arg not in commands:
    print(f"Error: Invalid argument '{arg}'.")
    sys.exit()

# Execute the command
command = commands[arg]
subprocess.run(command, shell=True)
