import os
import re


def read_powershell_history(max_lines=10):
    """Reads the PowerShell history file and returns the last `max_lines` lines.

    Args:
        max_lines (int, optional): The number of lines to return. Defaults to 10.

    Returns:
        list[str]: A list of the last `max_lines` lines of the PowerShell history.
    """
    history = []

    history_file = os.path.join(
        os.getenv("APPDATA"),
        "Microsoft",
        "Windows",
        "PowerShell",
        "PSReadLine",
        "ConsoleHost_history.txt",
    )

    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = file.readlines()

    history = history[-max_lines:]
    history = [line.strip() for line in history]
    history.reverse()

    return history


def search_powershell_history(substring: str, max_lines=10):
    """Searches the PowerShell history file for lines containing the `substring` and returns the last `max_lines` lines.

    Args:
        substring (str): The substring to search for.
        max_lines (int, optional): The number of lines to return. Defaults to 10.

    Returns:
        list[str]: A list of the last `max_lines` lines of the PowerShell history containing the `substring`.
    """
    history = []

    history_file = os.path.join(
        os.getenv("APPDATA"),
        "Microsoft",
        "Windows",
        "PowerShell",
        "PSReadLine",
        "ConsoleHost_history.txt",
    )

    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = file.readlines()

    history = [line.strip() for line in history if re.search(substring, line)]
    history = history[-max_lines:]
    history.reverse()

    return history


def remove_powershell_history(text: str):
    """Removes a line from the PowerShell history file.

    Args:
        text (str): The line to remove.
    """
    history_file = os.path.join(
        os.getenv("APPDATA"),
        "Microsoft",
        "Windows",
        "PowerShell",
        "PSReadLine",
        "ConsoleHost_history.txt",
    )

    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = file.readlines()

        history = [line for line in history if line.strip() != text]

        with open(history_file, "w") as file:
            file.writelines(history)
