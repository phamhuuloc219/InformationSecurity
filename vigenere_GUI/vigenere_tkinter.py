import tkinter as tk
from tkinter import messagebox, Toplevel
import os

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
    plaintext = input_text.get("1.0", tk.END).strip()
    key = key_entry.get().strip()
    
    if not plaintext:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đoạn văn bản cần mã hóa!")
        return
    if not key.isalpha():
        messagebox.showwarning("Cảnh báo", "Khóa phải chỉ bao gồm các chữ cái!")
        return
    
    ciphertext = vigenere_encrypt(plaintext, key)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ciphertext)
    
    save_file(ciphertext)

def save_file(content):
    output_path = r"D:\Learning\GitHub\InformationSecurity\vigenere_GUI\OUTPUT.DAT"
    
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, "w") as file:
            file.write(content)
        messagebox.showinfo("Thông báo", f"File đã được lưu tại {output_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu file: {e}")

def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)

def read_input_file():
    try:
        with open(r"D:\Learning\GitHub\InformationSecurity\vigenere_GUI\INPUT.DAT", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                input_text.delete("1.0", tk.END)
                input_text.insert(tk.END, lines[0].strip())
                key_entry.delete(0, tk.END)
                key_entry.insert(tk.END, lines[1].strip())
            else:
                messagebox.showwarning("Cảnh báo", "File INPUT.DAT không hợp lệ.")
    except FileNotFoundError:
        messagebox.showwarning("Cảnh báo", "Không tìm thấy file INPUT.DAT.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đọc file lỗi: {e}")

def show_vigenere_table():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_table = []

    for i in range(26):
        vigenere_table.append(alphabet[i:] + alphabet[:i])

    table_window = Toplevel(root)
    table_window.title("Bảng mã hóa Vigenere")
    
    table_window.geometry("800x700")
    
    for i in range(27):
        table_window.grid_columnconfigure(i, weight=1, minsize=25)
    for i in range(27):
        table_window.grid_rowconfigure(i, weight=1, minsize=25)
        
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

root = tk.Tk()
root.title("Mã hóa Vigenere")
root.geometry("500x400")

tk.Label(root, text="Nhập đoạn văn bản:", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=5, width=50, font=("Arial", 12))
input_text.pack(pady=5)

tk.Label(root, text="Nhập khóa:", font=("Arial", 12)).pack(pady=5)
key_entry = tk.Entry(root, font=("Arial", 12), width=30)
key_entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Mã hóa", font=("Arial", 12), command=encrypt_text, bg="lightblue")
encrypt_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Xóa", font=("Arial", 12), command=clear_text, bg="lightcoral")
clear_button.grid(row=0, column=1, padx=10)

read_button = tk.Button(button_frame, text="Đọc file INPUT.DAT", font=("Arial", 12), command=read_input_file, bg="lightyellow")
read_button.grid(row=0, column=2, padx=10)

show_table_button = tk.Button(root, text="Bảng mã hóa", font=("Arial", 12), command=show_vigenere_table, bg="lightgreen")
show_table_button.pack(pady=10)

tk.Label(root, text="Kết quả mã hóa:", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, width=50, font=("Arial", 12), state=tk.NORMAL)
output_text.pack(pady=5)

root.mainloop()
