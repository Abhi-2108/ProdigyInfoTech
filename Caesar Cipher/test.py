def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (an integer): "))

    encrypted_message = caesar_cipher(message, shift)
    decrypted_message = caesar_cipher(encrypted_message, -shift)

    print("\nEncrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
