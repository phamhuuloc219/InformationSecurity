from guizero import App, Text, TextBox, PushButton, Box, error

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    
    return ciphertext

def encrypt_text():
    plaintext = input_text.value.strip()
    key = key_input.value.strip()
    
    if not plaintext:
        error("Cảnh báo", "Vui lòng nhập đoạn văn bản cần mã hóa!")
        return
    if not key.isalpha():
        error("Cảnh báo", "Khóa phải chỉ bao gồm các chữ cái!")
        return
    
    ciphertext = vigenere_encrypt(plaintext, key)
    output_text.value = ciphertext

def clear_text():
    input_text.value = ""
    key_input.value = ""
    output_text.value = ""

app = App("Mã hóa Vigenere", width=500, height=400)

Text(app, text="Nhập đoạn văn bản:", size=12, align="top")
input_text = TextBox(app, multiline=True, width=40, height=5, align="top")
input_text.bg = "white"
input_text.padding = 5

Text(app, text="", height=1)

Text(app, text="Nhập khóa:", size=12, align="top")
key_input = TextBox(app, width=30, align="top")
key_input.padding = 5

Text(app, text="", height=1)

button_box = Box(app, layout="grid", align="top")
encrypt_button = PushButton(button_box, text="Mã hóa", grid=[0, 0], command=encrypt_text, width=10)
encrypt_button.bg = "green"
encrypt_button.text_color = "white"
encrypt_button.padding = 5

clear_button = PushButton(button_box, text="Xóa", grid=[1, 0], command=clear_text, width=10)
clear_button.bg = "red"
clear_button.text_color = "white"
clear_button.padding = 5

Text(app, text="", height=1)

Text(app, text="Kết quả mã hóa:", size=12, align="top")
output_text = TextBox(app, multiline=True, width=40, height=5, enabled=False, align="top")
output_text.bg = "white"
output_text.padding = 5

app.display()
