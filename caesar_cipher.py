# Caesar Cipher - Enhanced with decrypt and lowercase support

def encrypt(text, shift):
    """
    Encrypt text using Caesar cipher.
    Supports both uppercase and lowercase letters.
    Non-alphabetic characters remain unchanged.
    """
    result = ""
    for char in text:
        if char.isupper():
            # Change 1: Handle uppercase letters
            # ord('A') = 65, converts char to 0-25 range, applies shift, converts back
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            # Change 2: Handle lowercase letters
            # ord('a') = 97, same logic but for lowercase
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Non-alphabetic characters (spaces, punctuation, numbers) stay the same
            result += char
    return result


def decrypt(text, shift):
    """
    Decrypt text by reversing the Caesar cipher.
    Simply encrypts with negative shift.
    """
    # Change 3: Decrypt is just encrypt with negative shift
    return encrypt(text, -shift)


# Main program
text = input("Enter your text: ")
shift = int(input("Enter your shift (1-25): "))

# Perform encryption and decryption
encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

# Change 4: Nice formatted output showing all three versions
print("\n" + "=" * 40)
print("RESULTS")
print("=" * 40)
print(f"Original:   {text}")
print(f"Encrypted:  {encrypted}")
print(f"Decrypted:  {decrypted}")
print("=" * 40)
