#!/usr/bin/env python3
# =======================================
# Encryption Tool by PxCSA
# For educational purposes only
# =======================================

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("==================================================")
    print("        Encryption Tool by SHIVAMxCSA")
    print("==================================================")

    while True:
        print("\nWhat do you want to do?")
        print("  1. Encrypt a message")
        print("  2. Decrypt a message")
        print("  3. Quit")

        choice = input("\nEnter choice (1/2/3): ")

        if choice == "1":
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift number (e.g. 3): "))
            encrypted = encrypt(message, shift)
            print(f"\n  Original  : {message}")
            print(f"  Encrypted : {encrypted}")
            print(f"  Shift     : {shift}")

        elif choice == "2":
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift number (e.g. 3): "))
            decrypted = decrypt(message, shift)
            print(f"\n  Encrypted : {message}")
            print(f"  Decrypted : {decrypted}")
            print(f"  Shift     : {shift}")

        elif choice == "3":
            print("\n  Goodbye! Stay secure! 🔐")
            break

        else:
            print("\n  [!] Invalid choice. Please enter 1, 2 or 3.")

if __name__ == "__main__":
    main()
