from sys import argv
from os import system
arguments = list(argv)

globally = '--global'
# IF NOT RUNNING GLOBALLY UNCOMMENT THE NEXT LINE
#globally = ''

documentation = '''Welcome to SCOOPYMAN

FLAGS           USE CASE
-               Show this page. Yeah that's how you got here
-S              Install an/multiiple apps
-Syu            Update the system and install apps (if you want tho)
-Q              List all apps installed (You can also grep this if you want to search for a single app)
-Qe             Runs scoop which for your app of choice
-Ss             Search online for your app
-R              Removes/Uninstalls an app

Anything else   INVALID OPTION and you also get this file as a ball of shame!'''

# to remove the pacman.py argument
arguments.pop(0)

# TODO: CHECK IF RUNNING IN SUDO
# SCOOP INSTALL
if arguments[0] == '-S':
    arguments.pop(0)
    print("Installing", *arguments)
    for i in arguments:
        system(f"scoop install {i} {globally}")

#SCOOP UPDATE ALL / SCOOP INSTALL
elif arguments[0] == '-Syu':
    arguments.pop(0)
    print("Updating all apps...")
    system("scoop update *")
    print("Running scoop status")
    system("scoop status")
    for i in arguments:
        print("Installing", *arguments)
        system(f"scoop install {i} {globally}")
    
#SCOOP LIST
elif arguments[0] == '-Q':
    print("Listing all applications...")
    system("scoop list")

#SCOOP SEARCH INSTALLED
elif arguments[0] == '-Qe':
    arguments.pop(0)
    print("WARN Scoop which is not exactly working as intended. I am trying to fix that damn issue")
    print("Searching for:", *arguments)
    for i in arguments:
        system(f"scoop which {i}")


#SCOOP SEARCH
elif arguments[0] == '-Ss':
    arguments.pop(0)
    print("Searching for:", *arguments)
    for i in arguments:
        system(f"scoop search {i}")


#SCOOP UNINSTALL
elif arguments[0] == '-R':
    arguments.pop(0)
    print("Uninstalling:", *arguments)
    for i in arguments:
        system(f"scoop uninstall {i} {globally}")

elif arguments[0] == '-' or arguments[0] == '--help' or arguments[0] == '-h':
    print(documentation)

else:
    print("INVALID OPTION")
    print(documentation)
