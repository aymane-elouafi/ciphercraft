import ui 
import ciphers


def main() :
    ui.clear_screen()
    while True :
        ui.header()
        ui.display_main_menu()
        cipher = input("    > ").strip()
        if cipher == "1" :
            ui.clear_screen()
            ui.header()
            ui.display_cipher_selection_menu()
            mode = input("> ").strip()
            ciphers.caesar_cipher(mode)
        elif cipher == "2" :
            ui.clear_screen()
            ui.header()
            ui.display_cipher_selection_menu()
            mode = input("> ").strip()
            ciphers.vigenere_cipher(mode)
        elif cipher == "q" :
            ui.clear_screen()
            return

            
if __name__ == "__main__" :
    main()