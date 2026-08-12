#!/usr/bin/env python3

# Colors
cyan = "\033[1;36m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
red = "\033[1;31m"
reset = "\033[0m"

# Variables
version = "1.0"
shailesh_footer = "\x53\x68\x61\x69\x6c\x65\x73\x68\x2d\x5a\x78" # Shailesh-Zx

# Locked each line separately to prevent space mismatch
l1 = r"  ___            _       _  _____ _           _ _ "
l2 = r" / _ \ _ __ ___ (_)_ __ (_)/ ___/| |__   ___ | | |"
l3 = r"| | | | '_ ` _ \| | '_ \| |\___ \| '_ \ / _ \| | |"
l4 = r"| |_| | | | | | | | | | | | ___) | | | |  __/| | |"
l5 = r" \___/|_| |_| |_|_|_| |_|_|/____/|_| |_|\___ |_|_|"

# Print banner with precise spacing
print(cyan + l1)
print(cyan + l2)
print(cyan + l3)
print(cyan + l4)
print(cyan + l5)
print(yellow + " " * 44 + f"[{blue}v{version}{yellow}]")
print(cyan + " " * 41 + f"[{blue}By {green}{shailesh_footer}{cyan}]{reset}\n")

# Options Menu
while True:
    print(f"{green}[1]{reset} {cyan}Bat File{reset}")
    print(f"{green}[2]{reset} {cyan}Image File{reset}")
    print(f"{green}[3]{reset} {cyan}PDF File{reset}")
    print(f"{green}[4]{reset} {cyan}Office File (Word, Office){reset}")
    print(f"{green}[5]{reset} {cyan}Help{reset}")
    print(f"{green}[6]{reset} {red}Exit{reset}\n")
    
    # Get user input
    choice = input(f"{yellow}Select an option > {reset}")
    
    if choice == '1':
        print(f"\n{green}[+] Starting Bat File process...{reset}\n")
        # Write Bat File logic here
        break
        
    elif choice == '2':
        print(f"\n{green}[+] Starting Image File process...{reset}\n")
        # Write Image File logic here
        break
        
    elif choice == '3':
        print(f"\n{green}[+] Starting PDF File process...{reset}\n")
        # Write PDF File logic here
        break
        
    elif choice == '4':
        print(f"\n{green}[+] Starting Office File process...{reset}\n")
        # Write Office File logic here
        break
        
    elif choice == '5':
        print(f"\n{blue}[i] Help: Display tool usage instructions here.{reset}\n")
        # Return to menu after displaying help
        
    elif choice == '6':
        print(f"\n{red}[!] Exiting program...{reset}\n")
        break
        
    else:
        print(f"\n{red}[!] Invalid option! Please choose a number between 1 and 6.{reset}\n")
