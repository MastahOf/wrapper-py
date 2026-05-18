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
    
    print(f"The summary of the file")

    execstack = elf.execstack
    fortify = elf.fortify
    nx = elf.nx
    canaries = elf.canary
    system_opetation = elf.os
    relro = elf.relro
    pie = elf.pie
    rpath = elf.rpath
    runpath = elf.runpath
    if execstack == True:
        print("[-] Eexcstack: " + Fore.LIGHTGREEN_EX + f"{execstack}")
    else:
        print("[-] Execstack: " + Fore.LIGHTRED_EX + f"{execstack}")
    
    if fortify == True:
        print("[-] Fortify: " + Fore.LIGHTGREEN_EX + f"{fortify}")
    else:
        print("[-] Fortify: " + Fore.LIGHTRED_EX + f"{fortify}")
    
    if nx == True:
        print("[-] NX: " + Fore.LIGHTGREEN_EX + f"{nx}")
    else:
        print("[-] NX: " + Fore.LIGHTRED_EX + f"{nx}")
    
    if canaries == True:
        print("[-] Canary: " + Fore.LIGHTGREEN_EX + f"{canaries}")
    else:
        print("[-] Canary: " + Fore.LIGHTRED_EX + f"{canaries}")

    if relro == "Full":
        print('[-] Relro:  ' + Fore.LIGHTGREEN_EX + f"{relro}")
    elif relro == "Partial":
        print("[-] Relro: " + Fore.LIGHTYELLOW_EX + f"{relro}")
    elif relro == "None":
        print("[-] Relro:" + Fore.LIGHTRED_EX + f"{relro}")

    print(f"[-] OS: " + Fore.LIGHTYELLOW_EX + f"{system_opetation}")
    
    if pie == True:
        print("[-] PIE: " + Fore.LIGHTGREEN_EX + f"{pie}")
    else:
        print("[-] PIE: " + Fore.LIGHTRED_EX + f"{pie}")

    if rpath == None:
        print("[-] RPATH: " + Fore.LIGHTRED_EX + f"{rpath}")
    else:
        print("[-] RPATH: " + Fore.LIGHTGREEN_EX + f"{rpath}")
    
    if runpath == None:
        print("[-] RUNPATH: " + Fore.LIGHTRED_EX + f"{runpath}")
    else:
        print("[-] RUNPATH: " + Fore.LIGHTGREEN_EX + f"{runpath}")

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
    print(str(cyclic(how_long)))

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
