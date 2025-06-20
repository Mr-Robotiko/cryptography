import string
from typing import List


class Caesar:
    alphabet: str = string.ascii_letters

    @staticmethod
    def encrypt(key: int, plaintext: str) -> str:
        '''
        Encryption of a given plaintext based on a given key.
        E(k,p) := (index + key) mod len(alphabet)
        :param key: provide the public key
        :param plaintext: any plaintext that should be encrypted
        :return: encrypted plaintext
        '''
        encrypted_message: str = ""
        for char in plaintext:
            alphabet_index: int = Caesar.alphabet.find(char)
            new_index: int = (alphabet_index + key) % len(Caesar.alphabet)
            encrypted_char: str = Caesar.alphabet[new_index]
            encrypted_message += encrypted_char
        print(encrypted_message)
        return encrypted_message

    @staticmethod
    def decrypt(key: int, ciphertext) -> str:
        '''
        Decryption of a given ciphertext based on a given key.
        D(k,p) := (index - key) mod len(alphabet)
        :param key: provide the private key which is k_pub
        :param ciphertext: the corresponding ciphertext
        :return: decrypted plaintext
        '''
        decrypted_message: str = ""
        for char in ciphertext:
            alphabet_index: int = Caesar.alphabet.find(char)
            new_index: int = (alphabet_index - key) % len(Caesar.alphabet)
            encrypted_char: str = Caesar.alphabet[new_index]
            decrypted_message += encrypted_char
        print(decrypted_message)
        return decrypted_message

    @staticmethod
    def brute_force(ciphertext: str) -> List[str]:
        '''
        Brute forcing Ceaser is an efficient way of cracking the algorithm. The reason is based on the given key size, which
        will be the length of the alphabet minus one (len(alphabet - 1). The normal Alphabet will have 26 letters, so there
        will be 25 possibilities to shift the letters except the 0. This will have no effect on the given plaintext.
        :param ciphertext: Provide any ciphertext
        :return: A lookup list, where any decrypted word will be brute forced. The index is equivalent to the
        brute force index.
        '''
        lookup_list: List = list()
        for i in range(len(Caesar.alphabet)):
            word: str = Caesar.decrypt(i, ciphertext)
            lookup_list.append(word)
        return lookup_list


if __name__ == '__main__':
    c = Caesar()
    c.decrypt(2, c.encrypt(2, "hallo"))
    c.brute_force("Test")

