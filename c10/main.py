import pathlib as pl
import base64
import struct

pl.Path("home")
p = pl.Path("home")
pp = list(p.iterdir())
pp = [list(p.iterdir())[0] for p in pp]
pp = [list(p.iterdir())[0] for p in pp]
keys = []
for p in pp:
    with p.open() as f:
        keys.append(f.read())
        
namekeys = [dict(name = n, key = k) for _, k, n in map(lambda x: x.split(), keys)]
keys = [k['key'] for k in keys]
bk1 = base64.b64decode(k1)

parts = []
while keydata:
    # read the length of the data
    dlen = struct.unpack('>I', keydata[:4])[0]
    # read in <length> bytes
    data, keydata = keydata[4:dlen+4], keydata[4+dlen:]
    parts.append(data)

#n_val = eval('0x' + ''.join(['%02X' % struct.unpack('B', x)[0] for x in parts[2]]))
#n_val = '0x' + ''.join(['%02X' % struct.unpack('B', x)[0] for x in parts[2]])
#n_val = ''.join(['%02X' % struct.unpack('B', x)[0] for x in parts[2]])
#n_val = ['%02X' % struct.unpack('B', x)[0] for x in parts[2]]
