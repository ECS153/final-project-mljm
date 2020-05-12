# Before running
# Use $ pip install pycryptodome to install crypto

from Crypto.Cipher import AES
import base64

class MyCrypt:

    def padding(s):
        """ Pad the string to a multiple of 16 byte"""
        while len(s) % 16 != 0:
            s += b'\x00'
        return s

    @classmethod
    def AES_Encrypt(cls, key, data):
        """
        ECB Encryption
        Return: string type
        """
        key = cls.padding(key.encode('utf8'))
        data = cls.padding(data.encode('utf8'))
        model = AES.new(key, AES.MODE_ECB)

        encrypted = model.encrypt(data)
        encodestrs = base64.encodebytes(encrypted)
        ciphertext = encodestrs.decode('utf8')

        return ciphertext

    @classmethod
    def AES_Decrypt(cls, key, ciphertext):
        """
        ECB Decryption
        Return: string type
        """
        text = base64.decodebytes(ciphertext.encode('utf8'))
        key = cls.padding(key.encode('utf8'))
        model = AES.new(key, AES.MODE_ECB)

        try:
            data = model.decrypt(text)
            data = data.decode('utf8').strip('\0')
            return data
        except:
            print("Password Retrieving Error")
            return '\0'
        

if __name__ == '__main__':
    key = '11223344'
    plain_data = '18987654321q34985724589tuhjesjkedfhgskj,dfhgsjkldrf'

    cipher_text = MyCrypt.AES_Encrypt(key, plain_data)
    key2 = '1233224'
    data = MyCrypt.AES_Decrypt(key2, cipher_text)
    print(data)
        