def chipher(meassage):
    """Returns the encrypted text."""
    encrypted_text = ""
    for i in meassage:
        ascii = ord(i)
        if (65<=ascii<89) or (97<=ascii<121):
            new_ascii = ascii + 2
            new_letter =  chr(new_ascii)
        elif ascii == 89:
            new_letter = "A"
        elif ascii == 90:
            new_letter = "B"
        elif ascii == 121:
            new_letter = "a"
        elif ascii == 122:
            new_letter = "b"
        elif i == " ":
            new_letter = " "

        encrypted_text += new_letter

    return encrypted_text

def read_message():
    """Reads the message of message.txt"""
    file = open("D:\Musfique - 0152330101\lab_1\message.txt", 'r')
    text = file.read()
    file.close()
    return text


data = read_message()
new_data = chipher(data)
print(new_data)
file = open("D:\Musfique - 0152330101\lab_1\encrypted_message.txt", 'w')
file.write(new_data)
file.close()


def decripted_message(messages):
    """Returns the dencrypted text."""
    encrypted_text = ""
    for i in messages:
        ascii = ord(i)
        if (66<ascii<=90) or (98<ascii<=122):
            new_ascii = ascii - 2
            new_letter =  chr(new_ascii)
        elif ascii == 66:
            new_letter = "Z"
        elif ascii == 65:
            new_letter = "Y"
        elif ascii == 98:
            new_letter = "z"
        elif ascii == 97:
            new_letter = "y"
        elif i == " ":
            new_letter = " "

        encrypted_text += new_letter

    return encrypted_text

print(decripted_message(new_data))