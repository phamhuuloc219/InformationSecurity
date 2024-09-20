def generate_vigenere_table():
    table = []
    for i in range(26):
        row = [(chr((i + j) % 26 + 65)) for j in range(26)]
        table.append(row)
    return table

def encrypt_vigenere(plaintext, keyword):
    table = generate_vigenere_table()
    keyword_repeated = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]
    ciphertext = ""
    for p, k in zip(plaintext, keyword_repeated):
        row = ord(k) - 65
        col = ord(p) - 65
        ciphertext += table[row][col]
    return ciphertext

def decrypt_vigenere(ciphertext, keyword):
    table = generate_vigenere_table()
    keyword_repeated = (keyword * ((len(ciphertext) // len(keyword)) + 1))[:len(ciphertext)]
    plaintext = ""
    for c, k in zip(ciphertext, keyword_repeated):
        row = ord(k) - 65
        col = table[row].index(c)
        plaintext += chr(col + 65)
    return plaintext

# Ví dụ sử dụng
plaintext = input("Enter your message: ")
keyword = input("Enter keyword: ")
ciphertext = encrypt_vigenere(plaintext, keyword)
print("Bản mã:", ciphertext)
print("Giải mã:", decrypt_vigenere(ciphertext, keyword))
