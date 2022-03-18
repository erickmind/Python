import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[32mO site pudim.com.br está acessível!\033[m')
