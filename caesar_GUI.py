from guizero import App, Text, TextBox, PushButton, Box

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def show_result():
    text = input_box.value
    try:
        shift = int(shift_box.value)
        encoded_text = caesar_cipher(text, shift)
        result_box.value = encoded_text
    except ValueError:
        result_box.value = "Hãy nhập số nguyên cho dịch chuyển!"

def clear_result():
    input_box.value = ""
    shift_box.value = ""
    result_box.value = ""

app = App(title="Caesar Cipher Encoder", width=450, height=350, bg="#f7f7f7")

Text(app, text="Mã hóa Caesar", size=18, color="#333333", font="Arial", align="top")

input_area = Box(app, layout="grid", border=1, width="fill")

Text(input_area, text="Văn bản cần mã hóa:", grid=[0, 0], align="left")
input_box = TextBox(input_area, width=40, grid=[1, 0])

Text(input_area, text="Dịch chuyển:", grid=[0, 1], align="left")
shift_box = TextBox(input_area, width=10, grid=[1, 1])

Text(app, text="", height=1)

button_area = Box(app, layout="grid", width="fill")

button_show = PushButton(button_area, text="Xem kết quả", command=show_result, grid=[0, 0], width=15)
button_show.bg = "#4CAF50"
button_show.text_color = "white"

button_clear = PushButton(button_area, text="Xóa tất cả", command=clear_result, grid=[1, 0], width=15)
button_clear.bg = "#f44336"
button_clear.text_color = "white"

Text(app, text="", height=1)

result_area = Box(app, layout="grid", width="fill")

Text(result_area, text="Kết quả mã hóa:", grid=[0, 0], align="left")
result_box = TextBox(result_area, width=40, grid=[1, 0], enabled=False)

app.display()
