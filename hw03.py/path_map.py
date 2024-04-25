from colorama import Fore, Style
from pathlib import Path
import sys

colors = [Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.RED, Fore.MAGENTA]


def path_way(direct: str) -> str:
    """
    Prints the file tree of the directory
    """
    try:

        def explore_directory(directory, level=0):
            for path in directory.iterdir():
                print((colors[level % len(colors)]) + str(path) + Style.RESET_ALL)
                if path.is_dir() and not str(path).startswith("."):
                    explore_directory(path, level + 1)

        directory = Path(direct)
        explore_directory(directory)

    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    try:
        path_way(sys.argv[1])
    except IndexError:
        print("Enter path argument")
        sys.exit()
