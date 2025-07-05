import ui
import time 


def caesar_cipher(mode) :
    # mode : encrypt or decrypt 
    if mode == "1" :

        # Encrypt 
        try : 
            shift = int(input("Enter the key  > "))
            plain_text = input("Enter the plaintext > ")
        except ValueError:
            ui.print_error("Error")
            time.sleep(1)
            ui.clear_screen()
            return 

        j = []    
        for i in plain_text :
            if i.isalpha() :
                if i.islower() :    
                    k = ord(i) - 97 
                    j.append((( k + shift ) % 26) + 97 )
                elif i.isupper() :
                    k = ord(i) - 65
                    j.append((( k + shift ) % 26) + 65 )
            else : 
                j.append(ord(i))

        cipher_text=""
        for i in range(len(j)) :
            cipher_text = cipher_text + f"{chr(j[i])}"
            
        ui.print_success(f"Cipher Text : {cipher_text}\n")
        ui.print_info("Tab to return")
        input()
        ui.clear_screen()

    elif mode == "2" :

        # Decrypt
        try :
            shift = int(input("Enter the key  > "))
            plain_text = input("Enter the cipher text > ")
        except ValueError :
            ui.print_error("Error")
            time.sleep(1)
            ui.clear_screen()
            return 
        
        j = []    
        for i in plain_text :
            if i.isalpha() :
                if i.islower() :    
                    k = ord(i) - 97 
                    j.append((( k - shift ) % 26) + 97 )
                elif i.isupper() :
                    k = ord(i) - 65
                    j.append((( k - shift ) % 26) + 65 )
            else :
                j.append(ord(i))

        plain_text=""
        for i in range(len(j)) :
            plain_text = plain_text + f"{chr(j[i])}"
            
        ui.print_success(f"Plain Text : {plain_text}\n")
        ui.print_info("Tab to return")
        input()
        ui.clear_screen()

    elif mode == "c" :
        ui.clear_screen()
        return 
    else :
        ui.print_error("Error")
        time.sleep(1)
        ui.clear_screen()
        return  
        

def vigenere_cipher(mode) :
    # Encrypt 
    if mode == "1" :
        key = input("Enter the Keyword  > ").lower()
        if not key.isalpha():
                ui.print_error("Error: Keyword must contain only letters.")
                time.sleep(1)
                ui.clear_screen()
                return

        plain_text = input("Enter the plaintext > ").replace(" ","").lower()
        
        
        p_i = []
        k_i = []
        
        for i in plain_text :
            if i.isalpha() :                 
                    a = ord(i) - 97 
                    p_i.append(a)
            else : 
                p_i.append(ord(i))
        for j in key :
            if j.isalpha() :
                    b = ord(j) - 97
                    k_i.append(b)
        c_i = []
        k = 0
        for i in range(len(p_i)) :
            if 0 <= p_i[i] <= 25 :
                key_char_num = k_i[k % len(k_i)]
                k += 1
                c_i.append((( p_i[i] + key_char_num  ) % 26) + 97)  
            else:
                c_i.append(p_i[i])

        cipher_text=""
        for i in range(len(c_i)) :
            cipher_text = cipher_text + f"{chr(c_i[i])}"

        ui.print_success(f"Cipher Text : {cipher_text}\n")
        ui.print_info("Tab to return")
        input()
        ui.clear_screen()

    # Decrypt
    elif mode == "2" :
        key = input("Enter the Keyword  > ").lower()
        if not key.isalpha():
                ui.print_error("Error: Keyword must contain only letters.")
                time.sleep(1)
                ui.clear_screen()
                return
        cipher_text = input("Enter the ciphertext > ").replace(" ","").lower()
        
        e_i = []
        k_i = []
        
        for i in cipher_text :
            if i.isalpha() :                 
                    a = ord(i) - 97 
                    e_i.append(a)
            else : 
                e_i.append(ord(i))
        for j in key :
            if j.isalpha() :
                    b = ord(j) - 97
                    k_i.append(b)
        p_i = []
        k = 0
        for i in range(len(e_i)) :
            if 0 <= e_i[i] <= 25 :
                key_char_num = k_i[k % len(k_i)]
                k += 1
                p_i.append((( e_i[i] - key_char_num  ) % 26) + 97)  
            else:
                p_i.append(e_i[i])

        plain_text=""
        for i in range(len(p_i)) :
            plain_text = plain_text + f"{chr(p_i[i])}"

        ui.print_success(f"Plain Text : {plain_text}\n")
        ui.print_info("Tab to return")
        input()
        ui.clear_screen()
    
    elif mode == "c" :
        ui.clear_screen()
        return 
    else :
        ui.print_error("Error")
        time.sleep(1)
        ui.clear_screen()
        return   


