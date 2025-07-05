import os 
import platform


class Colors :
    # class attribute 
    SUCCESS = "\033[92m"
    ERROR = "\033[91m"
    INFO = "\033[96m"
    RESET = "\033[0m"


def print_success(message) :
    print(f"{Colors.SUCCESS}{message}{Colors.RESET}")
def print_error(message) :
    print(f"{Colors.ERROR}{message}{Colors.RESET}")
def print_info(message) :
    print(f"{Colors.INFO}{message}{Colors.RESET}")


def header() :
    print_success("""
 ▄▄· ▪   ▄▄▄· ▄ .▄▄▄▄ .▄▄▄   ▄▄· ▄▄▄   ▄▄▄· ·▄▄▄▄▄▄▄▄
▐█ ▌▪██ ▐█ ▄███▪▐█▀▄.▀·▀▄ █·▐█ ▌▪▀▄ █·▐█ ▀█ ▐▄▄·•██  
██ ▄▄▐█· ██▀·██▀▐█▐▀▀▪▄▐▀▀▄ ██ ▄▄▐▀▀▄ ▄█▀▀█ ██▪  ▐█.▪
▐███▌▐█▌▐█▪·•██▌▐▀▐█▄▄▌▐█•█▌▐███▌▐█•█▌▐█ ▪▐▌██▌. ▐█▌·
·▀▀▀ ▀▀▀.▀   ▀▀▀ · ▀▀▀ .▀  ▀·▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀  ▀▀▀               
     Command-line tool for classical cryptography
_____________________________________________________               
""")


def clear_screen() :
    if platform.system() == "Windows" :
        os.system("cls")
    else : 
        os.system("clear")


def display_main_menu() :
    clear_screen()
    header()
    print_info("""
    [1] Caesar Cipher
    [2] Vigenère Cipher

    [q] Quit   
               """)


def display_cipher_selection_menu() :
    print_info("""
    [1] Encrypt
    [2] Decrypt

    [c] Cancel 
               """)




    