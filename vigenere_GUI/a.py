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

# Nút mở bảng mã hóa
show_table_button = tk.Button(button_frame, text="Bảng mã hóa", font=("Arial", 12), command=show_vigenere_table, bg="lightgray")
show_table_button.grid(row=0, column=1, padx=10)

# Nút mở file OUTPUT
open_output_button = tk.Button(root, text="Mở file OUTPUT", font=("Arial", 12), command=open_output_file, bg="lightcoral")
open_output_button.pack(pady=10)

# Thêm nút giải mã vào giao diện
decrypt_button = tk.Button(root, text="Giải mã file", font=("Arial", 12), command=decrypt_file, bg="lightyellow")
decrypt_button.pack(pady=10)


root.mainloop()
