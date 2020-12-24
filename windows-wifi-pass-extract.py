import subprocess

data = subprocess.check_output(['nesth', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
    hasil = subprocess.check_output(['nesth', 'wlan', 'show', 'profiles', wifi, 'key=clear']).decode('utf-8').split('\n')
    hasil = [line.split(':')[1][1:-1] for line in hasil if "Key Content" in line]
    try:
        print(f'Name: {wifi}, Password: {hasil[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Tidak Terbaca!')
