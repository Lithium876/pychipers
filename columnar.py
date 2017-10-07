def columnarCipher(plainText, key):
	cipherText = ['']*len(key)
	cipherText = list(key)

	for col in range(len(key)):
		pointer = col
		for i in range(pointer, len(plainText), len(key)):
			cipherText[col]+=plainText[i]

	#order the columns in order of key letters
	cipherText.sort()
	for i in range(len(cipherText)):
		cipherText[i] = cipherText[i][1:] #remove the key first letter

	return ' '.join(cipherText)

def columnardecode(text, key):
	# cipherText = ['']*len(key)
	key = list(key)
	key.sort()
	key = ''.join(key)
	print(key)
	# cipherText = list(key)
	# print(key)

	# for col in range(len(key)):
	# 	pointer = col
	# 	for i in range(pointer, len(plainText), len(key)):
	# 		cipherText[col]+=plainText[i]

	# #order the columns in order of key letters
	# cipherText.sort(reverse=True)
	# for i in range(len(cipherText)):
	# 	cipherText[i] = cipherText[i][1:] #remove the key first letter

	# return ' '.join(cipherText)

# print(columnarCipher("THISISACOLUMNAR", "HELLO"))
print(columnardecode("HAM TSU ICN SOA ILR", "HELLO"))
#THISISACOLUMNAR
#HAMTSUICNSOAILR

# Col = 0 Pos = 0
# T

# Col = 0 Pos = 0+5
# TS

#Col = 0 Pos = 5+5
# TSU

# Col = 0 Pos = 15
# break

# Col = 1 Pos = 1
# H

# Col = 1 Pos = 1+5
# HA