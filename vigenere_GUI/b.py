# import tkinter as tk
# from tkinter import messagebox, filedialog, Toplevel
# import os

# va = "aáàảãạăắằẳẵặâấầẩẫậbcdđeéèẻẽẹêếềểễệfghiíìỉĩịjklmnoóòỏõọôốồổỗộơớờởỡợpqrstuúùủũụưứừửữựvxyzđ"
# # Chuyển văn bản tiếng Việt sang Telex
# def convert_to_telex(text):
#     telex_dict = {
#         'á': 'as', 'à': 'af', 'ả': 'ar', 'ã': 'ax', 'ạ': 'aj',
#         'ấ': 'aas', 'ầ': 'aaf', 'ẩ': 'aar', 'ẫ': 'aax', 'ậ': 'aaj',
#         'é': 'es', 'è': 'ef', 'ẻ': 'er', 'ẽ': 'ex', 'ẹ': 'ej',
#         'ế': 'ees', 'ề': 'eef', 'ể': 'eer', 'ễ': 'eex', 'ệ': 'eej',
#         'í': 'is', 'ì': 'if', 'ỉ': 'ir', 'ĩ': 'ix', 'ị': 'ij',
#         'ó': 'os', 'ò': 'of', 'ỏ': 'or', 'õ': 'ox', 'ọ': 'oj',
#         'ố': 'oos', 'ồ': 'oof', 'ổ': 'oor', 'ỗ': 'oox', 'ộ': 'ooj',
#         'ớ': 'ows', 'ờ': 'owf', 'ở': 'owr', 'ỡ': 'owx', 'ợ': 'owj',
#         'ú': 'us', 'ù': 'uf', 'ủ': 'ur', 'ũ': 'ux', 'ụ': 'uj',
#         'ứ': 'uws', 'ừ': 'uwf', 'ử': 'uwr', 'ữ': 'uwx', 'ự': 'uwj',
#         'ý': 'ys', 'ỳ': 'yf', 'ỷ': 'yr', 'ỹ': 'yx', 'ỵ': 'yj',
#         'đ': 'dd', 'ă':'aw','â':'aa','ê':'ee','ư':'uw','ô':'oo','ơ':'ow',
#         ' ': ' '  # Giữ khoảng trắng
#     }
    
#     result = []
#     for char in text:
#         if char.lower() in telex_dict:
#             # Kiểm tra nếu ký tự là hoa thì giữ hoa trong kết quả
#             telex_char = telex_dict[char.lower()]
#             if char.isupper():
#                 result.append(telex_char.upper())
#             else:
#                 result.append(telex_char)
#         else:
#             result.append(char)  # Giữ nguyên các ký tự không có trong từ điển (ví dụ dấu câu)
    
#     return ''.join(result)


# # Hàm mã hóa Vigenère
# def vigenere_encrypt_vietnamese(plaintext, key):
#     ciphertext = ""
#     key_index = 0
    
#     for char in plaintext:
#         if char.isalpha():  # Mã hóa chỉ với ký tự chữ
#             char_code = ord(char)
#             key_char = key[key_index % len(key)].lower()  # Lấy ký tự trong khóa
#             key_shift = ord(key_char) - ord('a')  # Tính độ dịch chuyển
#             if char.islower():
#                 encrypted_char = chr((char_code - ord('a') + key_shift) % 26 + ord('a'))
#             else:
#                 encrypted_char = chr((char_code - ord('A') + key_shift) % 26 + ord('A'))
#             ciphertext += encrypted_char
#             key_index += 1
#         else:
#             ciphertext += char  # Thêm các ký tự không phải chữ như dấu cách, dấu chấm
#     return ciphertext

# # Hàm chọn file INPUT.DAT
# def select_input_file():
#     global input_file_path
#     input_file_path = filedialog.askopenfilename(
#         title="Chọn file INPUT.DAT",
#         filetypes=[("Text Files", "*.DAT"), ("All Files", "*.*")]
#     )
#     if input_file_path:
#         input_file_label.config(text=f"File: {os.path.basename(input_file_path)}")

# # Hàm mã hóa file Tiếng Việt
# def process_files_vietnamese():
#     if not input_file_path:
#         messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT!")
#         return

#     try:
#         with open(input_file_path, "r", encoding="utf-8") as infile:
#             plaintext = infile.read().strip()
            
#         key = key_entry.get().strip().lower()
#         if not all(char in va for char in key):
#             messagebox.showwarning("Cảnh báo", "Khóa phải chỉ chứa các ký tự Tiếng Việt hợp lệ!")
#             return

#         ciphertext = vigenere_encrypt_vietnamese(plaintext, key)

#         output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT_VIETNAMESE.DAT")
#         with open(output_file_path, "w", encoding="utf-8") as outfile:
#             outfile.write(ciphertext)

#         messagebox.showinfo("Thành công", f"Mã hóa Tiếng Việt thành công! Kết quả đã được ghi vào {output_file_path}.")
#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# # Hàm hiển thị nội dung file OUTPUT_VIETNAMESE.DAT
# def show_output_file():
#     output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT_VIETNAMESE.DAT")
#     if not os.path.exists(output_file_path):
#         messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT_VIETNAMESE.DAT!")
#         return

#     try:
#         with open(output_file_path, "r", encoding="utf-8") as outfile:
#             content = outfile.read()

#         output_window = Toplevel(root)
#         output_window.title("Nội dung file OUTPUT_VIETNAMESE.DAT")
#         output_window.geometry("600x400")

#         text_area = tk.Text(output_window, font=("Arial", 12), wrap="word")
#         text_area.insert("1.0", content)
#         text_area.config(state="disabled")
#         text_area.pack(expand=True, fill="both", padx=10, pady=10)

#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Không thể đọc file OUTPUT_VIETNAMESE.DAT: {e}")

# # Giao diện tkinter
# root = tk.Tk()
# root.title("Mã hóa Vigenère Tiếng Việt")
# root.geometry("600x400")

# input_file_path = None

# select_file_button = tk.Button(root, text="Chọn file INPUT.DAT", font=("Arial", 12), command=select_input_file, bg="lightgreen")
# select_file_button.pack(pady=10)

# input_file_label = tk.Label(root, text="Chưa chọn file", font=("Arial", 12))
# input_file_label.pack(pady=10)

# tk.Label(root, text="Nhập khóa mã hóa:", font=("Arial", 12)).pack(pady=5)
# key_entry = tk.Entry(root, font=("Arial", 12), width=30)
# key_entry.pack(pady=5)

# encrypt_button_vietnamese = tk.Button(root, text="Mã hóa Tiếng Việt", font=("Arial", 12), command=process_files_vietnamese, bg="lightblue")
# encrypt_button_vietnamese.pack(pady=10)

# show_output_button = tk.Button(root, text="Hiện file OUTPUT_VIETNAMESE.DAT", font=("Arial", 12), command=show_output_file, bg="lightpink")
# show_output_button.pack(pady=10)

# root.mainloop()

import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel
import os

# Bảng TELEX cho Tiếng Việt
telex_dict = {
    'á': 'as', 'à': 'af', 'ả': 'ar', 'ã': 'ax', 'ạ': 'aj',
    'ấ': 'aas', 'ầ': 'aaf', 'ẩ': 'aar', 'ẫ': 'aax', 'ậ': 'aaj',
    'é': 'es', 'è': 'ef', 'ẻ': 'er', 'ẽ': 'ex', 'ẹ': 'ej',
    'ế': 'ees', 'ề': 'eef', 'ể': 'eer', 'ễ': 'eex', 'ệ': 'eej',
    'í': 'is', 'ì': 'if', 'ỉ': 'ir', 'ĩ': 'ix', 'ị': 'ij',
    'ó': 'os', 'ò': 'of', 'ỏ': 'or', 'õ': 'ox', 'ọ': 'oj',
    'ố': 'oos', 'ồ': 'oof', 'ổ': 'oor', 'ỗ': 'oox', 'ộ': 'ooj',
    'ớ': 'ows', 'ờ': 'owf', 'ở': 'owr', 'ỡ': 'owx', 'ợ': 'owj',
    'ú': 'us', 'ù': 'uf', 'ủ': 'ur', 'ũ': 'ux', 'ụ': 'uj',
    'ứ': 'uws', 'ừ': 'uwf', 'ử': 'uwr', 'ữ': 'uwx', 'ự': 'uwj',
    'ý': 'ys', 'ỳ': 'yf', 'ỷ': 'yr', 'ỹ': 'yx', 'ỵ': 'yj',
    'đ': 'dd', 'ă': 'aw', 'â': 'aa', 'ê': 'ee', 'ư': 'uw', 'ô': 'oo', 'ơ': 'ow',
    'Á': 'AS', 'À': 'AF', 'Ả': 'AR', 'Ã': 'AX', 'Ạ': 'AJ',
    'Ấ': 'AAS', 'Ầ': 'AAF', 'Ẩ': 'AAR', 'Ẫ': 'AAX', 'Ậ': 'AAJ',
    'É': 'ES', 'È': 'EF', 'Ẻ': 'ER', 'Ẽ': 'EX', 'Ẹ': 'EJ',
    'Ế': 'EES', 'Ề': 'EEF', 'Ể': 'EER', 'Ễ': 'EEX', 'Ệ': 'EEJ',
    'Í': 'IS', 'Ì': 'IF', 'Ỉ': 'IR', 'Ĩ': 'IX', 'Ị': 'IJ',
    'Ó': 'OS', 'Ò': 'OF', 'Ỏ': 'OR', 'Õ': 'OX', 'Ọ': 'OJ',
    'Ố': 'OOS', 'Ồ': 'OOF', 'Ổ': 'OOR', 'Ỗ': 'OOX', 'Ộ': 'OOJ',
    'Ớ': 'OWS', 'Ờ': 'OWF', 'Ở': 'OWR', 'Ỡ': 'OWX', 'Ợ': 'OWJ',
    'Ú': 'US', 'Ù': 'UF', 'Ủ': 'UR', 'Ũ': 'UX', 'Ụ': 'UJ',
    'Ứ': 'UWS', 'Ừ': 'UWF', 'Ử': 'UWR', 'Ữ': 'UWX', 'Ự': 'UWJ',
    'Ý': 'YS', 'Ỳ': 'YF', 'Ỷ': 'YR', 'Ỹ': 'YX', 'Ỵ': 'YJ',
    'Đ': 'DD', 'Ă': 'AW', 'Â': 'AA', 'Ê': 'EE', 'Ư': 'UW', 'Ô': 'OO', 'Ơ': 'OW'
}

def convert_to_telex(text):
    # Thay thế các ký tự tiếng Việt bằng ký tự Telex
    for vi_char, telex_char in telex_dict.items():
        text = text.replace(vi_char, telex_char)
    
    return text

def vigenere_encrypt(plaintext, key):
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

def vigenere_decrypt(ciphertext, key):
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

    return ''.join(plaintext)

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(
        title="Chọn file INPUT.DAT",
        filetypes=[("Text Files", "*.DAT"), ("All Files", "*.*")]
    )
    if input_file_path:
        input_file_label.config(text=f"File: {os.path.basename(input_file_path)}")

def process_files():
    if not input_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT!")
        return

    try:
        with open(input_file_path, "r", encoding="utf-8") as infile:
            plaintext = infile.read().strip()

        key = key_entry.get().strip()
        if not key.isalpha():
            messagebox.showwarning("Cảnh báo", "Khóa phải chỉ bao gồm các chữ cái!")
            return

        telex_plaintext = convert_to_telex(plaintext)
        ciphertext = vigenere_encrypt(telex_plaintext, key)

        output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT.DAT")
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            outfile.write(ciphertext)

        messagebox.showinfo("Thành công", f"Mã hóa thành công! Kết quả đã được ghi vào {output_file_path}.")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

def open_output_file():
    if not input_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT trước!")
        return

    output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT.DAT")
    if os.path.exists(output_file_path):
        os.startfile(output_file_path)
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT.DAT! Vui lòng mã hóa trước.")
        
# Hàm giải mã Vigenère
def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += decrypted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext

# Hàm giải mã từ file OUTPUT.DAT
def decrypt_file():
    if not input_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT trước!")
        return

    output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT.DAT")
    if not os.path.exists(output_file_path):
        messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT.DAT!")
        return

    try:
        # Đọc nội dung từ file OUTPUT.DAT
        with open(output_file_path, "r", encoding="utf-8") as infile:
            ciphertext = infile.read().strip()

        # Lấy khóa từ giao diện người dùng
        key = key_entry.get().strip()
        if not key.isalpha():
            messagebox.showwarning("Cảnh báo", "Khóa phải chỉ bao gồm các chữ cái!")
            return

        # Giải mã văn bản
        plaintext = vigenere_decrypt(ciphertext, key)

        # Hiển thị kết quả giải mã
        messagebox.showinfo("Kết quả giải mã", f"Văn bản giải mã:\n{plaintext}")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")
        
# Giao diện tkinter
root = tk.Tk()
root.title("Mã hóa Vigenère từ file")
root.geometry("500x400")

input_file_path = None

# Chọn file INPUT
tk.Label(root, text="Chọn file INPUT.DAT:", font=("Arial", 12)).pack(pady=5)
input_file_button = tk.Button(root, text="Chọn file INPUT", font=("Arial", 12), command=select_input_file, bg="lightblue")
input_file_button.pack(pady=5)
input_file_label = tk.Label(root, text="File: Chưa chọn", font=("Arial", 10), fg="gray")
input_file_label.pack(pady=5)

# Nhập khóa mã hóa
tk.Label(root, text="Nhập khóa mã hóa:", font=("Arial", 12)).pack(pady=5)
key_entry = tk.Entry(root, font=("Arial", 12), width=30)
key_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Nút mã hóa file
process_button = tk.Button(button_frame, text="Mã hóa file", font=("Arial", 12), command=process_files, bg="lightgreen")
process_button.grid(row=0, column=0, padx=10)

# Nút mở file OUTPUT
open_output_button = tk.Button(root, text="Mở file OUTPUT", font=("Arial", 12), command=open_output_file, bg="lightcoral")
open_output_button.pack(pady=10)

# Thêm nút giải mã vào giao diện
decrypt_button = tk.Button(root, text="Giải mã file", font=("Arial", 12), command=decrypt_file, bg="lightyellow")
decrypt_button.pack(pady=10)


root.mainloop()