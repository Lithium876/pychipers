def caesar(plainText, shift):
    cipherText = ''                    #The final encrypted text   
    for character in plainText:        #For each character in the plaintext
      caesarText = ord(character)+shift  #Store the numberic value of each character in caesat text 
      #For Encrpyting purposing
      if character.islower():          #If character is lower cased
        if caesarText > ord('z'):      #if the numeric in caesarText value is greater than 122 'z'
          caesarText -= 26             #Minus 26 from that value to wrap around the letters
        #For Decrpyting purposing
        elif caesarText < ord('a'):    #if the numeric in caesarText value is less than 97 'a'
          caesarText += 26             #Add 26 from that value to wrap around the letters
      #For Encrpyting purposing
      elif character.isupper():        #If character is upper cased
        if caesarText > ord('Z'):      #if the numeric in caesarText value is greater than 90 'Z'
          caesarText -= 26             #Minus 26 from that value to wrap around the letters
        #For Decrpyting purposing
        elif caesarText < ord('A'):    #if the numeric in caesarText value is less than 65 'A'
          caesarText += 26             #Add 26 from that value to wrap around the letter
      ''' 
      Convert the numeric value in caesar text to ascii equivalent 
      and append the latter to the Cipher text variable
      '''
      cipherText += chr(caesarText)
    #return encrypted or decrypted text
    return cipherText+' '

def caesarCipher(message, key):
  cipherMessage = ""                       #Final cipher message
  words = message.split()                  #Split up words in message
  for word in words:                       #Send each word to be encrypted/decrypted
    cipherMessage+=caesar(word, key) #encryted/decrypted text returned
  return cipherMessage                     #return encryted/decrypted message