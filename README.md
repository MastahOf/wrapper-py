# Overview
Wrapper for pwntools, shortcut

# Features
  - "--check", "-c" : used for checking the vulnerabilities in ELF file
  - "--create", "-e" : used for creating the template of exploitation
  - "--pattern", "-p" : used for creating the pattern to find the offset
  - "--find", "-f" : used for finding the offset from the subseq

# Installation & Global Usage

You can run this tool from any directory without any complication

  ## Windows Setup (VS Code / Powershell / CMD)

    1. **Create The Folder** to store the 'wrapper.py' file (eg. 'C:\User\wrapper-py')
    2. Add the 'wrapper.bat'
    3. Inside 'wrapper.bat' write the code or you can download it
       '''batch
       @python "%~dp0wrapper.py" %*
    4. Add the folder path in System Environment Variables (PATH)
         - Search for 'Environment Variables' or 'env' in Start Windows
         - Edit the 'path' variable under User Variable with click 'New'
         - Paste you folder path in it
         - Click OK and restart your computer
    5. You may try it in Terminal or Powershell or VS Code with type 'wrapper -c ./elf_file'

  ## Linux Setup

     1. Make the script executeable with type 'chmod +x wrapper.py'
     2. Copy to your local bin directory with type 'sudo cp wrapper.py /usr/local/bin/wrapper-file'
     3. Run it with type 'wrapper -c ./elf_file'

# Disclaimer:
  - This sript was used solely for Educational Purpose and for recording my learning journey, After all, this sctipt was still updated soon
