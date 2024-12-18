import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel
import os

#Hàm mã hóa Vigenère
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

#Hàm chọn file INPUT.DAT
def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(
        title="Chọn file INPUT.DAT",
        filetypes=[("Text Files", "*.DAT"), ("All Files", "*.*")]
    )
    if input_file_path:
        input_file_label.config(text=f"File: {os.path.basename(input_file_path)}")

def process_files():
    """Hàm đọc file INPUT.DAT, mã hóa và ghi vào OUTPUT.DAT"""
    if not input_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT!")
        return

    try:
        # Đọc nội dung từ file INPUT.DAT
        with open(input_file_path, "r", encoding="utf-8") as infile:
            plaintext = infile.read().strip()
        
        # Lấy khóa từ giao diện người dùng
        key = key_entry.get().strip()
        if not key.isalpha():
            messagebox.showwarning("Cảnh báo", "Khóa phải chỉ bao gồm các chữ cái!")
            return
        
        # Mã hóa văn bản
        ciphertext = vigenere_encrypt(plaintext, key)
        
        # Ghi kết quả vào file OUTPUT.DAT
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


#hiển thị bảng mã hóa Vigenère
def show_vigenere_table():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_table = []
    
    for i in range(26):
        vigenere_table.append(alphabet[i:] + alphabet[:i])

    table_window = Toplevel(root)
    table_window.title("Bảng mã hóa Vigenere")
    
    table_window.geometry("800x700")
    
    for i in range(27):
        table_window.grid_columnconfigure(i, weight=1, minsize=20)
    for i in range(27):
        table_window.grid_rowconfigure(i, weight=1, minsize=20)

    for col_index, char in enumerate(alphabet):
        label = tk.Label(table_window, text=char, font=("Arial", 8), width=3, height=2, borderwidth=1, relief="solid")
        label.grid(row=0, column=col_index + 1, sticky="nsew")
    
    for row_index, char in enumerate(alphabet):
        label = tk.Label(table_window, text=char, font=("Arial", 8), width=3, height=2, borderwidth=1, relief="solid")
        label.grid(row=row_index + 1, column=0, sticky="nsew")

    for row_index, row in enumerate(vigenere_table):
        for col_index, char in enumerate(row):
            label = tk.Label(table_window, text=char, font=("Arial", 8), width=3, height=2, borderwidth=1, relief="solid")
            label.grid(row=row_index + 1, column=col_index + 1, sticky="nsew")
            
# Bảng chữ cái Tiếng Việt
VIETNAMESE_ALPHABET = "AĂÂBCDĐEÊGHIKLMNOÔƠPQRSTUƯVXY" 
# Hàm mã hóa Vigenère (Tiếng Việt)
# def vigenere_encrypt_vietnamese(plaintext, key):
#     key = key.lower()
#     key_index = 0
#     ciphertext = ""

#     for char in plaintext:
#         # Nếu ký tự nằm trong bảng Tiếng Việt
#         if char.lower() in VIETNAMESE_ALPHABET:
#             is_upper = char.isupper()  # Kiểm tra chữ hoa
#             char_lower = char.lower()  # Chuyển về chữ thường để xử lý
#             char_index = VIETNAMESE_ALPHABET.index(char_lower)
#             key_char = key[key_index % len(key)].lower()
#             key_index_char_index = VIETNAMESE_ALPHABET.index(key_char)

#             # Tính chỉ số mã hóa
#             new_index = (char_index + key_index_char_index) % len(VIETNAMESE_ALPHABET)
#             new_char = VIETNAMESE_ALPHABET[new_index]

#             # Khôi phục chữ hoa nếu cần
#             ciphertext += new_char.upper() if is_upper else new_char
#             key_index += 1  # Chuyển sang ký tự khóa tiếp theo
#         else:
#             # Giữ nguyên ký tự không hợp lệ
#             ciphertext += char

#     return ciphertext

# Hiển thị bảng mã hóa Vigenère (Tiếng Việt)
def show_vigenere_table_vietnamese():
    table_window = Toplevel(root)
    table_window.title("Bảng mã hóa Tiếng Việt")
    table_window.geometry("1500x900")

    tk.Label(table_window, text="Bảng mã hóa Vigenère Tiếng Việt", font=("Arial", 14), fg="blue").pack(pady=10)

    frame = tk.Frame(table_window)
    frame.pack()

    for i, char in enumerate(VIETNAMESE_ALPHABET[:29]):
        tk.Label(frame, text=char, width=5, borderwidth=1, relief="solid", font=("Arial", 10)).grid(row=0, column=i + 1)

    for i, char in enumerate(VIETNAMESE_ALPHABET[:29]):
        tk.Label(frame, text=char, width=5, borderwidth=1, relief="solid", font=("Arial", 10)).grid(row=i + 1, column=0)
        for j, shift_char in enumerate(VIETNAMESE_ALPHABET[:29]):
            encrypted_char = VIETNAMESE_ALPHABET[(i + j) % 29]
            tk.Label(frame, text=encrypted_char, width=5, borderwidth=1, relief="solid", font=("Arial", 10)).grid(row=i + 1, column=j + 1)

# # Hàm xử lý mã hóa Tiếng Việt
# def process_files_vietnamese():
#     if not input_file_path:
#         messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT!")
#         return

#     try:
#         with open(input_file_path, "r", encoding="utf-8") as infile:
#             plaintext = infile.read().strip()
            
#         key = key_entry.get().strip().upper()  # Chuẩn hóa khóa thành chữ hoa
#         if not all(char in VIETNAMESE_ALPHABET for char in key):
#             messagebox.showwarning("Cảnh báo", "Khóa phải chỉ chứa các ký tự Tiếng Việt hợp lệ!")
#             return

#         ciphertext = vigenere_encrypt_vietnamese(plaintext, key)

#         output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT_VIETNAMESE.DAT")
#         with open(output_file_path, "w", encoding="utf-8") as outfile:
#             outfile.write(ciphertext)

#         messagebox.showinfo("Thành công", f"Mã hóa Tiếng Việt thành công! Kết quả đã được ghi vào {output_file_path}.")
#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# # Hàm mở file OUTPUT_VIETNAMESE.DAT
# def open_output_file_vietnamese():
#     if not input_file_path:
#         messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT trước!")
#         return

#     output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT_VIETNAMESE.DAT")
#     if os.path.exists(output_file_path):
#         os.startfile(output_file_path)
#     else:
#         messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT_VIETNAMESE.DAT! Vui lòng mã hóa trước.")

# # Hàm giải mã file OUTPUT_VIETNAMESE.DAT
# def decrypt_file_vietnamese():
#     if not input_file_path:
#         messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT trước!")
#         return

#     output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT.DAT")
#     if not os.path.exists(output_file_path):
#         messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT.DAT!")
#         return

#     try:
#         # Đọc nội dung từ file OUTPUT.DAT
#         with open(output_file_path, "r", encoding="utf-8") as infile:
#             ciphertext = infile.read().strip()

#         # Lấy khóa từ giao diện người dùng
#         key = key_entry.get().strip()
#         if not key.isalpha():
#             messagebox.showwarning("Cảnh báo", "Khóa phải chỉ bao gồm các chữ cái!")
#             return

#         # Giải mã văn bản
#         plaintext = vigenere_decrypt(ciphertext, key)

#         # Hiển thị kết quả giải mã
#         messagebox.showinfo("Kết quả giải mã", f"Văn bản giải mã:\n{plaintext}")

#     except Exception as e:
#         messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")
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

def select_input_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(
        title="Chọn file INPUT.DAT",
        filetypes=[("Text Files", "*.DAT"), ("All Files", "*.*")]
    )
    if input_file_path:
        input_file_label.config(text=f"File: {os.path.basename(input_file_path)}")

def process_files_vietnamese():
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
        ciphertext = vigenere_encrypt_vietnamese(telex_plaintext, key)

        output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT.DAT")
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            outfile.write(ciphertext)

        messagebox.showinfo("Thành công", f"Mã hóa thành công! Kết quả đã được ghi vào {output_file_path}.")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

def open_output_file_vietnamese():
    if not input_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT trước!")
        return

    output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT.DAT")
    if os.path.exists(output_file_path):
        os.startfile(output_file_path)
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT.DAT! Vui lòng mã hóa trước.")
        
# Tạo từ điển ngược từ telex_dict
reverse_telex_dict = {value: key for key, value in telex_dict.items()}

# Hàm chuyển đổi từ Telex về ký tự Tiếng Việt
def convert_from_telex(telex_text):
    for telex_char, vi_char in reverse_telex_dict.items():
        telex_text = telex_text.replace(telex_char, vi_char)
    return telex_text

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

# Cập nhật hàm giải mã file
def decrypt_file_vietnamese():
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
        plaintext = vigenere_decrypt_vietnamese(ciphertext, key)

        # Hiển thị kết quả giải mã
        messagebox.showinfo("Kết quả giải mã", f"Văn bản giải mã:\n{plaintext}")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# Giao diện tkinter
root = tk.Tk()
root.title("Mã hóa Vigenère Tiếng Anh và Tiếng Việt")
root.geometry("600x500")

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

# Nút mã hóa Tiếng Anh
encrypt_button_english = tk.Button(button_frame, text="Mã hóa Tiếng Anh", font=("Arial", 12), command=process_files, bg="lightgreen")
encrypt_button_english.grid(row=0, column=0, padx=10)

# Nút mã hóa Tiếng Việt
encrypt_button_vietnamese = tk.Button(button_frame, text="Mã hóa Tiếng Việt", font=("Arial", 12), command=process_files_vietnamese, bg="lightblue")
encrypt_button_vietnamese.grid(row=0, column=1, padx=10)

# Nút mở bảng mã hóa Tiếng Anh
show_table_button_english = tk.Button(button_frame, text="Bảng mã Anh", font=("Arial", 12), command=show_vigenere_table, bg="lightgray")
show_table_button_english.grid(row=1, column=0, padx=10, pady=10)

# Nút mở bảng mã hóa Tiếng Việt
show_table_button_vietnamese = tk.Button(button_frame, text="Bảng mã Việt", font=("Arial", 12), command=show_vigenere_table_vietnamese, bg="lightgray")
show_table_button_vietnamese.grid(row=1, column=1, padx=10, pady=10)

# Nút mở file OUTPUT
open_output_button = tk.Button(root, text="Mở file OUTPUT", font=("Arial", 12), command=open_output_file, bg="lightcoral")
open_output_button.pack(pady=10)

# Nút mở file OUTPUT_VIETNAMESE
open_output_button_vietnamese = tk.Button(root, text="Mở file OUTPUT Tiếng Việt", font=("Arial", 12), command=open_output_file_vietnamese, bg="lightcoral")
open_output_button_vietnamese.pack(pady=5)

# Nút giải mã file Tiếng Việt
decrypt_button_vietnamese = tk.Button(root, text="Giải mã file Tiếng Việt", font=("Arial", 12), command=decrypt_file_vietnamese, bg="lightyellow")
decrypt_button_vietnamese.pack(pady=5)


# Thêm nút giải mã vào giao diện
decrypt_button = tk.Button(root, text="Giải mã file", font=("Arial", 12), command=decrypt_file, bg="lightyellow")
decrypt_button.pack(pady=10)

root.mainloop()
