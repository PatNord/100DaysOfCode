alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'å', 'ä', 'ö']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  'Å', 'Ä', 'Ö']

user_input = input("Write the message to cipher: ")
shift = int(input("Write the shift amount: "))
message = list(user_input)

def encrypt(message, shift, alphabet, upper):
    max_index = len(alphabet)
    encryption = []
    for i in message:

        if i in upper:
            i_value = upper.index(i)
            new_index = (i_value + shift) % max_index
            encryption.append(upper[new_index])
        elif i in alphabet:
            i_value = alphabet.index(i)
            new_index = (i_value + shift) % max_index
            encryption.append(alphabet[new_index])
        else:
            encryption.append(i)
            
    
    return encryption

def decrypt(encrypted_message, shift, alphabet, upper):
    decryption = []
    max_index = len(alphabet)
    choice = input("Do you want to decrypt message? Y or N: ").lower().strip()
    if choice not in ["y", "n"]:
        print("Write Y or N!")
    else:
        if choice == "y":
            for i in encrypted_message:
                if i in upper:
                    i_value = upper.index(i)
                    new_index = (i_value - shift) % max_index
                    decryption.append(upper[new_index])
                
                elif i in alphabet:
                    i_value = alphabet.index(i)
                    new_index = (i_value - shift) % max_index
                    decryption.append(alphabet[new_index])
                else:
                    decryption.append(i)
            return "".join(decryption)
        elif choice == "n":
            return ""
    


encrypted_message = encrypt(user_input,shift,alphabet, alphabet_upper)
str_message = "".join(encrypted_message)

print(str_message)

print(decrypt(encrypted_message, shift, alphabet, alphabet_upper))


