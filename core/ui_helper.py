from colorama import Fore, Style, init

init(autoreset=True)

def show_banner():
    print(f"{Fore.MAGENTA}{Style.BRIGHT}" + "="*50)
    print(f"{Fore.WHITE}       SPY-E ASCII MASTER ULTIMATE")
    print(f"{Fore.MAGENTA}    Multi-Font & Image-to-ASCII Generator")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}" + "="*50 + "\n")

def get_color(color_name):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "white": Fore.WHITE
    }
    return colors.get(color_name.lower(), Fore.WHITE)
