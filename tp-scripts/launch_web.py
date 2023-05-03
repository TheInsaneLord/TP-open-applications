import subprocess
import sys

# Your commands go here
commands = {
    'chrome': 'com.google.Chrome',
    'firefox': 'firefox',
    '1': 'com.google.Chrome',
    '2': 'firefox'
}

# Get the command-line arguments
try:
    browser = commands[sys.argv[1]]
    url = sys.argv[2]
except (IndexError, KeyError):
    print("Error: Invalid arguments provided.")
    sys.exit()

# Open the specified URL in the specified browser
command = f"{browser} {url}"
subprocess.run(command, shell=True)

