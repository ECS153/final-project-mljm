# Before running
# Use $ pip install pycryptodome to install crypto

from Crypto.Cipher import AES
import base64

class MyCrypt:
    def padding_16(s):
        """ Pad the string to exactly 16 bytes(length of 16)"""
        while len(s) % 16 != 0:
            s += b'\x00'
        return s

    def padding_512(s):
        """ 
        Pad the string to a multiple of 512 bit, represented by a binary string
        Arguments:
            s: A string
        Return:
            A binary string with length of a multiple of 512
        
        """
        bits = ""
        for c in s:
            # turn the data into bit representation
            bits += '{0:08b}'.format(ord(c))
        org_len = len(bits)

        # (a) append one "1" 
        bits += "1"

        # (b) append "0"s until the length % 512 == 448
        while len(bits) % 512 != 448:
            bits += "0"
        
        # (c) append last two words(each 32 bit), which is the representation of original data length
        last_two = '{0:064b}'.format(org_len)
        bits += last_two
        return bits

    @classmethod
    def AES_Encrypt(cls, key, data):
        """
        ECB Encryption
        Arguments: 
            key: The key used to encrypt the data. (AES only supports key sizes of 16, 24 or 32 bytes)
            data: The data waiting to be encrypted.

        Return: 
            The encrypted data.
        """
        key = cls.padding_16(key.encode('utf8'))
        data = cls.padding_16(data.encode('utf8'))
        model = AES.new(key, AES.MODE_ECB)

        encrypted = model.encrypt(data)
        encodestrs = base64.encodebytes(encrypted)
        ciphertext = encodestrs.decode('utf8')

        return ciphertext

    @classmethod
    def AES_Decrypt(cls, key, ciphertext):
        """
        ECB Decryption

        Arguments: 
            key: The key used to decrypt the ciphertext.
            ciphertext: The encrypted data waiting to be decrypted.

        Return: 
            The original data.
        """
        text = base64.decodebytes(ciphertext.encode('utf8'))
        key = cls.padding_16(key.encode('utf8'))
        model = AES.new(key, AES.MODE_ECB)

        try:
            data = model.decrypt(text)
            data = data.decode('utf8').strip('\0')
            return data
        except:
            print("Decryption Error")
            return '\0'

    @classmethod
    def SHA1(cls, data):
        """ 
        SHA-1 hashing function, used for master password encryption.
        See more details at: https://www.hjp.at/(st_a)/doc/rfc/rfc3174.html
        Arguments: 
            data: The input message to hash.

        Returns: 
            A hex string calcultaed by sha1 algorithm.
        """
        def f(i, B, C, D):
            if i >= 0 and i <= 19:
                return (B & C) | ((~B) & D)
            elif i >= 20 and i <= 39:
                return B ^ C ^ D
            elif i >= 40 and i <= 59:
                return (B & C) | (B & D) | (C & D)
            else:
                return B ^ C ^ D

        def K(i):
            if i >= 0 and i <= 19:
                return 0x5A827999
            elif i >= 20 and i <= 39:
                return 0x6ED9EBA1
            elif i >= 40 and i <= 59:
                return 0x8F1BBCDC
            else:
                return 0xCA62C1D6


        bits = cls.padding_512(data)

        H0 = 0x67452301
        H1 = 0xEFCDAB89
        H2 = 0x98BADCFE
        H3 = 0x10325476
        H4 = 0xC3D2E1F0

        # divide into chunks and opearate separatly
        # each chunk: 512 bit
        # each word: 32 bit
        for i in range(0, len(bits), 512):
            chunk = bits[i:i+512]
            words = [0] * 80
            for i in range(16):
                words[i] = int(chunk[i*32:(i+1)*32], 2)
            for i in range(16, 80):
                X = (words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16])
                words[i] = (X << 1) | (X >> 31)
            
            A, B, C, D, E = H0, H1, H2, H3, H4

            for i in range(80):
                temp = (A << 5) | (A >> 27) + f(i, B, C, D) + E + words[i] + K(i)
                E = D
                D = C
                C = (B << 30) | (B >> 2)
                B = A
                A = temp & 0xffffffff

            H0 = (H0 + A) & 0xffffffff
            H1 = (H1 + B) & 0xffffffff
            H2 = (H2 + C) & 0xffffffff
            H3 = (H3 + D) & 0xffffffff
            H4 = (H4 + E) & 0xffffffff
        
        return "%08x%08x%08x%08x%08x" % (H0, H1, H2, H3, H4)

if __name__ == '__main__':
    # key = '674522f1efcdab85183adce8702e547542d2c1df'
    # plain_data = 'ucdavis123456'

    # cipher_text = MyCrypt.AES_Encrypt(key, plain_data)
    # key2 = '1122334'
    # data = MyCrypt.AES_Decrypt(key2, cipher_text)
    # print(data)
    
    master_pwd = "ucdavis"
    value = MyCrypt.SHA1(master_pwd)
    print(value)