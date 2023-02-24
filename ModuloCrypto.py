def encrytion(message): 
    alfabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
    new_alfabet = "zxywvutsrqponmñkljighfedcbaZXCVBNMASDFGHJKLQWERTYUIOPÑ"
    encrypted_message = ""

    for letter in message:
      for l in range(len(alfabet)):
        if letter == alfabet[l]:
          encrypted_message += new_alfabet[l]
    
    return encrypted_message

def decrytion(message): 
    new_alfabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
    alfabet = "zxywvutsrqponmñkljighfedcbaZXCVBNMASDFGHJKLQWERTYUIOPÑ"
    decrypted_message = ""

    for letter in message:
      for l in range(len(alfabet)):
        if letter == alfabet[l]:
          decrypted_message += new_alfabet[l] + " "
    
    return decrypted_message



message = input ("Ingrese un mensaje: \n")

ecryp = encrytion(message)

print (ecryp)

decryp_message = decrytion(ecryp)

print (decryp_message)


