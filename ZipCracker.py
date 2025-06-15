import pyzipper
import os

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def crack_zip(file, wordlist):
    found = False
    total = 0

    if not os.path.isfile(file):
        print(f"{RED}❌ ZIP file not found: {file}{RESET}")
        return
    if not os.path.isfile(wordlist):
        print(f"{RED}❌ Wordlist file not found: {wordlist}{RESET}")
        return

    try:
        with pyzipper.AESZipFile(file) as zf:
            for pwd in open(wordlist, "r", errors="ignore"):
                total += 1
                pwd_clean = pwd.strip()
                try:
                    zf.extractall(pwd=pwd_clean.encode())
                    print(f"\n{GREEN}[+] Password Found: {pwd_clean}{RESET}")
                    found = True
                    break
                except:
                    print(f"{RED}[-] Trying: {pwd_clean}{RESET}")
    except Exception as e:
        print(f"{RED}❌ Error opening ZIP file: {e}{RESET}")
        return

    print(f"\n Total Passwords Tried: {total}\n")
    if not found:
        print(f"{RED}[-] ❌ Password not found in wordlist.{RESET}")
    else:
        print(f"{GREEN}[✔] Cracking complete{RESET}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen first

    print(f"{GREEN}Tool by @Demon_Owner7{RESET}")
    print(f"{GREEN}Use : For Zip Cracking{RESET}\n")
    
    zip_file = input("Enter ZIP file path: ").strip()
    wordlist_file = input("Enter password wordlist path: ").strip()
    crack_zip(zip_file, wordlist_file)

if __name__ == "__main__":
    main()