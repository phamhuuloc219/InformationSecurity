from vigenere_main import convert_from_telex


def vigenere_encrypt_vietnamese(plaintext, key):
    ciphertext = []
    key_index = 0
    key = key.lower()

    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)

    return ''.join(ciphertext)

# Cập nhật hàm giải mã Vigenère để chuyển từ Telex về Tiếng Việt
def vigenere_decrypt_vietnamese(ciphertext, key):
    # Giải mã Vigenère ban đầu
    plaintext = []
    key_index = 0
    key = key.lower()

    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            base = ord('A') if is_upper else ord('a')
            key_char = key[key_index % len(key)]
            shift = ord(key_char) - ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)

    # Chuyển đổi từ Telex về Tiếng Việt
    decrypted_text = ''.join(plaintext)
    return convert_from_telex(decrypted_text)