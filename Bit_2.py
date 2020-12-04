from bitcoin.rpc import RawProxy
import hashlib

p = RawProxy()
# Big-endian values to little-endian
# naudotas https://www.reddit.com/r/learnpython/comments/2m65dy/endianness_conversion_of_hex_values_in_python_2x/
def swap(member):
    sz = bytearray.fromhex(member)
    sz.reverse()
    x = ''.join(format(a, '02x') for a in sz) #dvejetaine sistema
    return x

# The block height where Alice's transaction was recorded
blockheight = 245615

block_hash = p.getblockhash(blockheight)    #is uzduoties pvz
block = p.getblock(block_hash)

# Headeris

#Cia viskas sukeiciama i bitus
versionHex = swap(block["versionHex"])
previousblockhash = swap(block["previousblockhash"])
merkleroot = swap(block["merkleroot"])
time = swap('{:02x}'.format(block["time"])) #keiciama atskirai
bits = swap(block["bits"])
nonce = swap('{:02x}'.format(block["nonce"])) #keiciama atskirai
head = (versionHex + previousblockhash + merkleroot + time + bits + nonce) #viskas sudedama

#viskas vel verciama i 16-ne
head_bin = head.decode('hex')

# naudotas https://www.programcreek.com/python/example/957/hashlib.sha256
hash = hashlib.sha256(hashlib.sha256(head_bin).digest()).digest()

print("Tikrintas hashas: ")
print hash[::-1].encode('hex_codec')
print("Esamas hashas: ")
print block['hash']     #tiesiog info is bloko