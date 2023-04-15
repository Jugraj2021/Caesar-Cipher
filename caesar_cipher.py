def caesar_cipher(message, shift, mode):
    if mode == 'encode':
        shift = shift % 26
    elif mode == 'decode':
        shift = -shift %26
    else :
        return 'Invalid Mode'

    result = ''
    for char in message:
        if char.isalpha():
            char_code = ord(char) + shift
            if char .isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -=26
                elif char_code < ord('a'):
                    char_code +=26

            result += chr(char_code)
        else:
            result += char

    return result

message  = input("Enter any thing you want to encode or decode : - ")
shift = int (input("Enter the shift value : - "))

enpt_msg = caesar_cipher(message , shift , 'encode')
print("The encrypted value is : - ", enpt_msg)

dept_msg = caesar_cipher(message , shift , 'decode')
print("The decrypted value is : - ", dept_msg)




