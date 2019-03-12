#!/usr/bin/env python
# coding=utf-8

import sys
import getopt
from aes_encrypt import AesEncrypt

CRYPT_KEY_PATH = "/home/ubuntu/.scm_key/crypt_key"


def encrypt_passwd(origin_passwd):
    ae = AesEncrypt(CRYPT_KEY_PATH)
    return ae.encrypt(origin_passwd)


def _decrypt_passwd(encrypted_passwd):
    ae = AesEncrypt(CRYPT_KEY_PATH)
    return ae.decrypt(encrypted_passwd)


def usage():
    print("First, please make sure your crypt key file is in the directory %s" % CRYPT_KEY_PATH)
    print("Usage: python password_tools.py [OPTS] <password>")
    print("  -h, --help                  print this help and exit")
    print("  -e, --encrypt               encrypt your password")
    print("  -d, --decrypt               decrypt your password")


def main(argv):
    password = ""
    encrypt = ""
    try:
        opts, args = getopt.getopt(argv, "he:d:", ["help", "encrypt=", "decrypt="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    if opts:
        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit(2)
            elif o in ("-e", "--encrypt"):
                password = a
            elif o in ("-d", "--decrypt"):
                encrypt = a
    elif not opts and args:
        if len(args) == 1:
            password = args[0]
        else:
            usage()
            sys.exit(2)
    else:
        usage()
        sys.exit(2)
    if password:
        print(encrypt_passwd(password))
    elif encrypt:
        print(_decrypt_passwd(encrypt))
    else:
        usage()
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])
