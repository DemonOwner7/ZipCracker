Telergam :@Demon_Owner7

# 🔐 ZipCracker - Bruteforce Zip Password Cracking Tool

**ZipCracker** is a Python-based brute-force attack tool that attempts to crack password-protected `.zip` files using a wordlist.  
It is lightweight, easy to use in Termux or any Linux-based system, and uses the `pyzipper` library for fast cracking.



## ▶️ How to Use

1. Install the tool using the commands given below.  
2. When the script runs, it will ask you to:
   - Enter the path of the `.zip` file you want to crack.  
   - Enter the path of the password list file (e.g., `rockyou.txt`).  
3. The tool will try each password from the list.  
4. When the correct password is found, it will be displayed on the screen.



## 📋 Features

- 🔍 Brute-force attack using a password list  
- 📦 Supports `.zip` file format  
- ⚡ Fast and simple to use  
- 🐍 Python-based and works on Termux/Linux  



## 🛠️ Installation

Run the following commands step-by-step in **Termux** or Linux terminal:

```bash
pkg update && pkg upgrade
pkg install python
pip install pyzipper
pkg install git
git clone https://github.com/DemonOwner7/ZipCracker.git
cd ZipCracker
python ZipCracker.py
