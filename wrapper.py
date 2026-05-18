import argparse
import sys
import os
from colorama import Fore, Style, Back, init
from pwn import *

init(autoreset=True)
def checking_files(path_files):
    if not os.path.exists(path_files):
        print(f"The path file is not valid {path_files}")
        return
    
    print(f"[*] Processing the {path_files} file")

    try:
        elf = ELF(path_files, checksec=False)
    except Exception as e:
        print(f"Failed to process the {path_files} file because {e}")
        return
    
    print(f"The summary of the file")

    if elf.execstack:
        print(f"[-] Eexcstack: {Fore.LIGHTGREEN_EX + str(elf.execstack)}")
    else:
        print(f"[-] Execstack: {Fore.LIGHTRED_EX + str(elf.execstack)}")
    
    if elf.fortify:
        print(f"[-] Fortify: {Fore.LIGHTGREEN_EX + str(elf.fortify)}")
    else:
        print(f"[-] Fortify: {Fore.LIGHTRED_EX + str(elf.fortify)}")
    
    if elf.nx:
        print(f"[-] NX: {Fore.LIGHTGREEN_EX + str(elf.nx)}")
    else:
        print(f"[-] NX: {Fore.LIGHTRED_EX + str(elf.nx)}")
    
    if elf.cannary:
        print(f"[-] Canary: {Fore.LIGHTGREEN_EX + str(elf.canary)}")
    else:
        print(f"[-] Canary: {Fore.LIGHTRED_EX + str(elf.canary)}")

    if elf.relro == "Full":
        print(f"[-] Relro: {Fore.LIGHTGREEN_EX + elf.relro}")
    elif elf.relro == "Partial":
        print(f"[-] Relro: {Fore.LIGHTYELLOW_EX + elf.relro}")
    elif elf.relro == "None":
        print(f"[-] Relro: {Fore.LIGHTRED_EX + elf.relro}")

    print(f"[-] OS: {Fore.LIGHTYELLOW_EX  + elf.os}")
    
    if elf.pie:
        print(f"[-] PIE: {Fore.LIGHTGREEN_EX + str(elf.pie)}")
    else:
        print(f"[-] PIE: " + Fore.LIGHTRED_EX + f"{Fore.LIGHTRED_EX + str(elf.pie)}")

    if elf.rpath == None:
        print(f"[-] RPATH: {Fore.LIGHTRED_EX + str(elf.rpath)}")
    else:
        print(f"[-] RPATH: {Fore.LIGHTGREEN_EX + str(elf.rpath)}")
    
    if elf.runpath == None:
        print(f"[-] RUNPATH: {Fore.LIGHTRED_EX + str(elf.runpath)}")
    else:
        print(f"[-] RUNPATH: {Fore.LIGHTGREEN_EX + str(elf.runpath)}")

def creating_exploit(path_files):
    elf = ELF(path_files, checksec=False)
    arch = elf.arch
    bits = elf.bits
    
    template_payload = f"""
from pwn import *

#context file

context.binary = '{path_files}'
context.arch = {arch}
context.log_level = 'debug' 

#vuln

execstack = {elf.execstack}
fortify = {elf.fortify}
nx = {elf.nx}
os = '{elf.os}'
relro = '{elf.relro}'
pie = {elf.pie}

io = process("{path_files}")
#io = remote('addr_ip', port_ip)

#payload = b'a' * offset * p{bits}(addr_ip)

#io.interactive
"""
    output_file = 'exploit.py'
    with open(output_file, "w") as f:
        f.write(template_payload)

    print(f"[+] Succed to create the exploit file")

def creating_pattern(how_long):
    print(cyclic(how_long))

def find_pattern(pattern):
    print(cyclic_find(pattern))

def main():
    parser = argparse.ArgumentParser(description="This  the CLI that I create to help me to exploit in Binary Exploitation")

    parser.add_argument('--check', '-c', type=str, help="check the vulnerabilities of file")
    parser.add_argument('--create', '-e', type=str, help="create the template of exploitation")
    parser.add_argument('--pattern', '-p', type=int, help="create the pattern to find the offset")
    parser.add_argument('--find', '-f', type=str, help="find the offset")

    args = parser.parse_args()

    if args.create:
        creating_exploit(args.create)
    elif args.pattern:
        creating_pattern(args.pattern)
    elif args.find:
        find_pattern(args.find)
    elif args.check:
        checking_files(args.check)

if __name__ == "__main__":
    main()
