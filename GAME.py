"""
--- MAGIC SWORD ---

by:  Mason, Michael, Anthony

"""

import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


print("\n\n\n")
cprint(figlet_format('MAGIC SWORD', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])


print("\n\nCHOOSE YOUR CHARACTER\n1)MASON\n2)MICHAEL\n3)ANTHONY")
character = input()

print("\nYou are about to be hit by an incoming punch\n")
