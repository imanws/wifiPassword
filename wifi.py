import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for username in profiles:
    passwords = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', username, 'key=clear']).decode('utf-8').split('\n')
    passwords = [b.split(":")[1][1:-1] for b in passwords if "Key Content" in b]
    try:
        print ("{:<50}  |  {:<}".format(username, passwords[0]))
    except IndexError:
        print ("{:<50}|  {:<}".format(username, ""))
