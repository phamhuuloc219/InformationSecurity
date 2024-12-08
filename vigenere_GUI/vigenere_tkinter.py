import tkinter as tk
from tkinter import messagebox

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

def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)
    key_entry.delete(0, tk.END)

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

tk.Label(root, text="Kết quả mã hóa:", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, width=50, font=("Arial", 12), state=tk.NORMAL)
output_text.pack(pady=5)

root.mainloop()

# while True:
#     try:
#         root.update()
#         root.update_idletasks()
#     except tk.TclError:
#         break