# Run from /tmp/fesse

import os
from pwn import *

context.log_level = 'debug'

with open('/tmp/anus', "w") as f:
    f.write('\x00\x0a\x00\xff')

with open('/tmp/poil', "w") as f:
    f.write('\x00\x0a\x02\xff')

with open('\x0a', "w") as f:
    f.write('\x00\x00\x00\x00')

os.environ['\xde\xad\xbe\xef'] = '\xca\xfe\xba\xbe'
cmd = '/home/input2/input ' + " ''" * 65 + " '\x20\x0a\x0d'" + " '1234'" + " ''" * 32 + " < /tmp/anus 2< /tmp/poil"
print cmd

r = process(cmd, shell=True)
r.interactive()

