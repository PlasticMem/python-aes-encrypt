#!/usr/bin/env python
# coding=utf-8

import base64
from Crypto.Cipher import AES
from Crypto import Random


# 调整key的长度至16位，24位或者32位
def adjust_key(key):
    if len(key) <= 16:
        key = key + (16 - len(key)) * chr(0)
    elif 16 < len(key) <= 24:
        key = key + (24 - len(key)) * chr(0)
    elif 24 < len(key) <= 32:
        key = key + (32 - len(key)) * chr(0)
    else:
        print("the key can not be longer than 32 characters. Your key is longer than the limit，"
              "We will take the prior 32 characters as the key.")
        key = key[:32]
    return key


# 补全数据长度的方法
def adjust_string(string):
    bs = AES.block_size
    string = string + (bs - len(string) % bs) * chr(0)
    return string


class AesEncrypt(object):
    def __init__(self, key_file_path):
        # 默认用CBC模式
        self.mode = AES.MODE_CBC
        self.key = ""
        with open(key_file_path) as f:
            self.key = f.read().strip()

    def encrypt(self, plain_text):
        iv = Random.new().read(AES.block_size)
        cryptor = AES.new(adjust_key(self.key).encode('utf-8'), self.mode, iv)
        cipher_text = cryptor.encrypt(adjust_string(plain_text).encode('utf-8'))
        return base64.b64encode(iv + cipher_text).strip().decode('utf-8')

    def decrypt(self, cipher_text):
        cipher_text = base64.b64decode(cipher_text)
        iv = cipher_text[0:AES.block_size]
        cipher_text = cipher_text[AES.block_size:len(cipher_text)]
        cryptor = AES.new(adjust_key(self.key).encode('utf-8'), self.mode, iv)
        plain_text = cryptor.decrypt(cipher_text).decode('utf-8')
        return plain_text.strip()


if __name__ == '__main__':
    ae = AesEncrypt('./crypt_key_test')
    passwd = "plasticmem123"
    c_text = ae.encrypt(passwd)
    p_text = ae.decrypt(c_text)
    print("Origin Text: %s" % passwd)
    print("Encrypted Text: %s" % c_text)
    print("Decrypted Text: %s" % p_text)
