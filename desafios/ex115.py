import urllib.error
import urllib.request
try:
    site = urllib.request.urlopen('http://10.0.0.1/index.html#!/main/status')
except urllib.error.URLError:
    print('O site não esta acessivel no momento!')
else:
    print('O site esta no ar!')
