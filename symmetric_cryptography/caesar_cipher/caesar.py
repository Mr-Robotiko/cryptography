import string


class Caesar:
    alphabet: str = string.ascii_letters

    @staticmethod
    def encrypt(key: int, plaintext: str) -> str:
        encrypted_message: str = ""
        for char in plaintext:
            alphabet_index: int = Caesar.alphabet.find(char)
            new_index: int = (alphabet_index + key) % len(Caesar.alphabet)
            encrypted_char: str = Caesar.alphabet[new_index]
            encrypted_message += encrypted_char
        print(encrypted_message)
        return encrypted_message

    @staticmethod
    def decrypt(key: int, ciphertext):
        decrypted_message: str = ""
        for char in ciphertext:
            alphabet_index: int = Caesar.alphabet.find(char)
            new_index: int = (alphabet_index - key) % len(Caesar.alphabet)
            encrypted_char: str = Caesar.alphabet[new_index]
            decrypted_message += encrypted_char
        print(decrypted_message)
        return decrypted_message


if __name__ == '__main__':
    c = Caesar()
    c.decrypt(2, c.encrypt(2, "hallo"))

