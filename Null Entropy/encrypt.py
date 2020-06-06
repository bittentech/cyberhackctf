from Crypto.Cipher import AES
import binascii, sys
from flag import flag

key = "3N7g309d6Y7enT**"
IV = flag

message = 'Security is not a joke, mind it. But complete security is a myth'

def encrypt(message,passphrase):
	aes = AES.new(passphrase, AES.MODE_CBC, IV)
	return aes.encrypt(message)

print("Encrypted data: ", binascii.hexlify(encrypt(message,key)).decode())
