import requests

print('''\033[1;91m  ____  ____  _   _ ____   \033[0;33m ____  _                 _          
\033[1;91m |  _ \|  _ \| \ | / ___|  \033[0;33m|  _ \(_)___  __ _ _   _(_)___  ___  
\033[1;91m | | | | | | |  \| \___ \  \033[0;33m| | | | / __|/ _` | | | | / __|/ _ \ 
\033[1;91m | |_| | |_| | |\  |___) | \033[0;33m| |_| | \__ \ (_| | |_| | \__ \  __/
\033[1;91m |____/|____/|_| \_|____/  \033[0;33m|____/|_|___/\__, |\__,_|_|___/\___|
\033[1;91m                           \033[0;33m             |___/
\033[1;34m         Created by \033[1;35m@0xCoto\033[1;34m - https://github.com/0xCoto/
''')

print('\033[4;34mNo-IP Account Credentials\033[0m')
username = raw_input('\033[0;36m  Username or Email: \033[0;32m')
password = raw_input('\033[0;36m  Password: \033[0;32m')

print('\n\033[4;34mHostname Modification\033[0m')
hostname = raw_input('\033[0;36m  Hostname: \033[0;32m')
ip = raw_input('\033[0;36m  IPv4 Address (leave blank for random): \033[0;32m')

if ip == '':
	ip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(5,250),4))

print('\n\033[4;33mRedirecting...\033[0m')
print('\033[0;33m  Redirecting \033[0;32m'+hostname+'\033[0;33m to \033[0;32m'+ip+'\033[0;33m...')

r = requests.get('https://'+username+':'+password+'@dynupdate.no-ip.com/nic/update?hostname='+hostname+'&myip='+ip)

print('')
if 'good' in r.text:
	print('\033[4;32mHostname modified successfully\033[0m')
	print('\033[0;32m  Hostname \033[0;33m'+hostname+'\033[0;32m has been successfully modified to redirect to \033[0;33m'+ip+'\033[0;32m.')
elif 'badauth' in r.text:
	print('\033[4;31mAuthentication Error\033[0m')
	print('\033[0;31m  Failed to authenticate. Please check your credentials and try again.')
elif 'nohost' in r.text:
	print('\033[4;31mInvalid Hostname\033[0m')
	print('\033[0;31m  That Hostname is not associated with your No-IP account.')
else:
	print('\033[4;31mError\033[0m')
	print('\033[0;31m  An unknown error has occurred: '+r.text)
print('\033[0m')