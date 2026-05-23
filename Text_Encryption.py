def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26

            if char.islower():
                result += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# USER SETUP MESSAGE
message = input("Enter Your Secret Message:")

# USER SETUP KEY
shift = int(input("Enter Encryption Key: "))

# ENCRYPT MESSAGE
encrypted = encrypt(message, shift)

print("\n========== ENCRYPTED MESSAGE ==========")
print("Original Message :", message)
print("Encrypted Message:", encrypted)

# DECRYPT MESSAGE
decrypted = decrypt(encrypted, shift)

print("\n========== DECRYPTED MESSAGE ==========")
print("Decrypted Message:", decrypted)