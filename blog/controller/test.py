# -*- coding: utf8 -*-

import binascii
from Crypto.Cipher import DES
import sys


def make_auth_header_signature(key, data):
    def _pad(raw, blocksize=8):
        pad = blocksize - (len(raw) % blocksize)
        return raw + pad * chr(pad)

    codec = DES.new(key, DES.MODE_CBC, key)
    sig = codec.encrypt(_pad(data))
    return binascii.hexlify(sig).upper()


if __name__ == '__main__':
    data = sys.argv[1]
    key = sys.argv[2]
    res = make_auth_header_signature(key, data)
    print(res)