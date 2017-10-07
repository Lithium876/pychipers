import string, operator

def vernamCipher(plainText, key, operate):
	if len(plainText) == len(key):				#check if the plaintext and key is same length
		Alphabet = list(string.ascii_lowercase)
		plainText = plainText.lower()
		key = key.lower()

		plainTextAsInt = [Alphabet.index(character) for character in plainText]
		KeyAsInt = [Alphabet.index(character) for character in key]

		values = [operate(x,y) for x, y in zip(plainTextAsInt, KeyAsInt)]
		fin = [i%25 for i in values]
		cipherText = [Alphabet[i] for i in fin]

		return ''.join(cipherText)+" "
	elif len(plainText) > len(key):
		key = key*len(plainText)
		key = key[0:len(plainText)]
		return vernamCipher(plainText, key, operate)
	else:
		key = key[0:len(plainText)]
		return vernamCipher(plainText, key, operate)

def oneTimePad(message, key, operate):
	cipherMessage = ""                   #Final cipher message
	words = message.split()              #Split up words in message
	for word in words:                   #Send each word to be encrypted/decrypted
		cipherMessage+=vernamCipher(word, key, operate) #encryted/decrypted text returned
	return cipherMessage                 #return encryted/decrypted message