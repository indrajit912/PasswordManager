# /utils/cli_utils.py
# Author: Indrajit Ghosh
# Created On: Jun 13, 2024
# 

import os
import sys
from datetime import date

import pwinput
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from vaultsafe.version import __version__
from vaultsafe.config import APP_NAME, COPYRIGHT_STATEMENT, DATABASE_PATH, GITHUB_REPO

console = Console()

def clear_terminal_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def input_password(info_msg="Enter your password: "):
    bullet_unicode = '\u2022'
    pw = pwinput.pwinput(info_msg, mask=bullet_unicode)
    return pw

def multiline_input(prompt):
    """Prompt the user for multiline input."""
    console.print(Panel(prompt, title="Input", style="bold blue"))
    lines = []
    empty_line_count = 0
    while True:
        line = input()
        if line == "":
            empty_line_count += 1
            if empty_line_count == 3:
                break
        else:
            empty_line_count = 0
        lines.append(line)
    return "\n".join(lines[:-2])

def check_db_init():
    """Checks whether db is initialized or not."""
    if not DATABASE_PATH.exists():
        return False
    else:
        return True

def assert_db_init():
    # Check db_init
    if not check_db_init():
        console.print(Panel("[red]No vault found![/red] The app is probably not initialized yet.", title="Error", style="bold red"))
        console.print("Please use the [bold]`init`[/bold] command to initialize the app.", style="yellow")
        sys.exit(1)


# Function to print basic information
def print_basic_info():

    clear_terminal_screen()

    # Create title with centered alignment
    title = Panel(f"{APP_NAME} - Password Manager App\nGitHub: {GITHUB_REPO}", title=f"{APP_NAME}", title_align="center", style="bold white on blue", border_style="bright_blue")

    # Create information table with centered alignment
    info_table = Table(show_header=False)
    info_table.add_row("[center]Version[/center]", f"[center]{__version__}[/center]")
    info_table.add_row("[center]Copyright[/center]", f"[center]{COPYRIGHT_STATEMENT}[/center]")
    info_table.add_row("[center]Today's Date[/center]", f"[center]{date.today().strftime('%B %d, %Y')}[/center]")

    # Print title and information table
    console.print(title)
    console.print(info_table)
    console.print("\n")