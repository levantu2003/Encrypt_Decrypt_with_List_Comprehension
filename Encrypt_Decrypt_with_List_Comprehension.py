def encryt_char(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + key) % 26)

def decrypt_char(char, key):
    return encryt_char(char, 26 - key)

if __name__ == "__main__":
    choice = int(input("1. Encrypt\n2. Decrypt\nEnter your choice: "))
    print(f"You choose {choice}!")
    key = 3
    
    if choice == 1:
        text = input("Enter your text: ")
        cipher_list = [encryt_char(c,key) if c not in ' ,.' else c for c in text.upper()]
        print(''.join(cipher_list))
    
    elif choice == 2:
        text = input("Enter your text: ")
        message_list = [decrypt_char(c, key) if c not in ' ,.' else c for c in text.upper()]
        print(''.join(message_list))
    
    else:
        print("Invalid choice!")
