import tkinter as tk
from tkinter import messagebox, filedialog, Toplevel
import os

from vigenere_org import vigenere_decrypt, vigenere_encrypt
from vigenere_vie import vigenere_decrypt_vietnamese, vigenere_encrypt_vietnamese

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

# Hiển thị bảng mã hóa Vigenere (Tiếng Việt)
def show_vigenere_table_vietnamese():
    table_window = Toplevel(root)
    table_window.title("Bảng mã hóa Tiếng Việt")
    table_window.geometry("1500x900")

    tk.Label(table_window, text="Bảng mã hóa Vigenere Tiếng Việt", font=("Arial", 14), fg="blue").pack(pady=10)

    frame = tk.Frame(table_window)
    frame.pack()

    for i, char in enumerate(VIETNAMESE_ALPHABET[:29]):
        tk.Label(frame, text=char, width=5, borderwidth=1, relief="solid", font=("Arial", 10)).grid(row=0, column=i + 1)

    for i, char in enumerate(VIETNAMESE_ALPHABET[:29]):
        tk.Label(frame, text=char, width=5, borderwidth=1, relief="solid", font=("Arial", 10)).grid(row=i + 1, column=0)
        for j, shift_char in enumerate(VIETNAMESE_ALPHABET[:29]):
            encrypted_char = VIETNAMESE_ALPHABET[(i + j) % 29]
            tk.Label(frame, text=encrypted_char, width=5, borderwidth=1, relief="solid", font=("Arial", 10)).grid(row=i + 1, column=j + 1)

# Bảng TELEX cho Tiếng Việt
telex_dict = {
    'á': 'as', 'à': 'af', 'ả': 'ar', 'ã': 'ax', 'ạ': 'aj',
    'ắ': 'aws', 'ằ': 'awf', 'ẳ': 'awr', 'ẵ': 'awx', 'ặ': 'awj',
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
    'Ắ': 'AWS', 'Ằ': 'AWF', 'Ẳ': 'AWR', 'Ẵ': 'AWX', 'Ặ': 'AWJ',
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

telex_dict_double_rhyme = {
    'ấ': 'aas', 'ầ': 'aaf', 'ẩ': 'aar', 'ẫ': 'aax', 'ậ': 'aaj',
    'Ấ': 'AAS', 'Ầ': 'AAF', 'Ẩ': 'AAR', 'Ẫ': 'AAX', 'Ậ': 'AAJ',
    'ế': 'ees', 'ề': 'eef', 'ể': 'eer', 'ễ': 'eex', 'ệ': 'eej',
    'Ế': 'EES', 'Ề': 'EEF', 'Ể': 'EER', 'Ễ': 'EEX', 'Ệ': 'EEJ',
    'ố': 'oos', 'ồ': 'oof', 'ổ': 'oor', 'ỗ': 'oox', 'ộ': 'ooj',
    'Ố': 'OOS', 'Ồ': 'OOF', 'Ổ': 'OOR', 'Ỗ': 'OOX', 'Ộ': 'OOJ',
}
def convert_to_telex(text):
    # Thay thế các ký tự tiếng Việt bằng ký tự Telex
    for vi_char, telex_char in telex_dict.items():
        text = text.replace(vi_char, telex_char)
    
    return text

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

        output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT_VIETNAMESE.DAT")
        with open(output_file_path, "w", encoding="utf-8") as outfile:
            outfile.write(ciphertext)

        messagebox.showinfo("Thành công", f"Mã hóa thành công! Kết quả đã được ghi vào {output_file_path}.")

    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

def open_output_file_vietnamese():
    if not input_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT trước!")
        return

    output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT_VIETNAMESE.DAT")
    if os.path.exists(output_file_path):
        os.startfile(output_file_path)
    else:
        messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT_VIETNAMESE.DAT! Vui lòng mã hóa trước.")
        
# Tạo từ điển ngược từ telex_dict
reverse_telex_dict_double_rhyme = {value: key for key, value in telex_dict_double_rhyme.items()}
reverse_telex_dict = {value: key for key, value in telex_dict.items()}

# Hàm chuyển đổi từ Telex về ký tự Tiếng Việt
def convert_from_telex(telex_text):
    for telex_char, vi_char in reverse_telex_dict_double_rhyme.items():
        telex_text = telex_text.replace(telex_char, vi_char)
    for telex_char, vi_char in reverse_telex_dict.items():
        telex_text = telex_text.replace(telex_char, vi_char)
    return telex_text

# Cập nhật hàm giải mã file
def decrypt_file_vietnamese():
    if not input_file_path:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn file INPUT.DAT trước!")
        return

    output_file_path = os.path.join(os.path.dirname(input_file_path), "OUTPUT_VIETNAMESE.DAT")
    if not os.path.exists(output_file_path):
        messagebox.showerror("Lỗi", "Không tìm thấy file OUTPUT_VIETNAMESE.DAT!")
        return

    try:
        # Đọc nội dung từ file OUTPUT_VIETNAMESE.DAT
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

# Giao diện
root = tk.Tk()
root.title("Mã hóa Vigenere")
root.state('zoomed')  # Lắp đầy màn hình

input_file_path = None

# Tạo một frame chính để căn giữa các thành phần
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')

# Cấu hình lưới để giúp căn giữa
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Cấu hình các dòng và cột trong main_frame
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_rowconfigure(3, weight=1)

main_frame.grid_columnconfigure(0, weight=1)

# Frame để căn giữa các thành phần (như file input và khóa)
input_frame = tk.Frame(main_frame)
input_frame.grid(row=0, column=0, pady=30, padx=40)

# Chọn file INPUT
tk.Label(input_frame, text="Chương trình mã hóa và giải mã Vigenere", font=("Arial", 20)).grid(row=0, column=0, padx=20, pady=10, sticky='w')
input_file_button = tk.Button(input_frame, text="Chọn file cần mã hóa", font=("Arial", 12), command=select_input_file, bg="lightblue", width=25)
input_file_button.grid(row=1, column=0, padx=150, pady=10, sticky='w')
input_file_label = tk.Label(input_frame, text="File: Chưa chọn", font=("Arial", 10), fg="gray")
input_file_label.grid(row=2, column=0, padx=150, pady=10, sticky='w')

# Nhập khóa mã hóa
tk.Label(input_frame, text="Nhập khóa mã hóa:", font=("Arial", 14)).grid(row=3, column=0, padx=150, pady=10, sticky='w')
key_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
key_entry.grid(row=4, column=0, padx=150, pady=10, sticky='w')

# Frame để chứa các nút
button_frame = tk.Frame(main_frame)
button_frame.grid(row=1, column=0, pady=30)

# Nút mã hóa
encrypt_button_english = tk.Button(button_frame, text="Mã hóa Vigenere", font=("Arial", 12), command=process_files, bg="lightgreen", width=20)
encrypt_button_english.grid(row=0, column=0, padx=15, pady=10)

# Nút mã hóa Tiếng Việt
encrypt_button_vietnamese = tk.Button(button_frame, text="Mã hóa Vigenere Tiếng Việt", font=("Arial", 12), command=process_files_vietnamese, bg="lightblue", width=30)
encrypt_button_vietnamese.grid(row=0, column=1, padx=15, pady=10)

# Nút mở bảng mã hóa
show_table_button_english = tk.Button(button_frame, text="Bảng mã Vigenere", font=("Arial", 12), command=show_vigenere_table, bg="lightgray", width=20)
show_table_button_english.grid(row=1, column=0, padx=15, pady=10)

# Nút mở bảng mã hóa Tiếng Việt
show_table_button_vietnamese = tk.Button(button_frame, text="Bảng mã Vigenere Tiếng Việt", font=("Arial", 12), command=show_vigenere_table_vietnamese, bg="lightgray", width=30)
show_table_button_vietnamese.grid(row=1, column=1, padx=15, pady=10)

# Nút giải mã file Vigenere và mở file OUTPUT cùng cột với mã hóa Vigenere
decrypt_button = tk.Button(button_frame, text="Giải mã file Vigenere", font=("Arial", 12), command=decrypt_file, bg="lightyellow", width=20)
decrypt_button.grid(row=3, column=0, padx=15, pady=10)

open_output_button = tk.Button(button_frame, text="Mở file OUTPUT", font=("Arial", 12), command=open_output_file, bg="lightcoral", width=20)
open_output_button.grid(row=2, column=0, padx=15, pady=10)

# Nút giải mã Tiếng Việt và mở file OUTPUT Tiếng Việt
decrypt_button_vietnamese = tk.Button(button_frame, text="Giải mã file Vigenere Tiếng Việt", font=("Arial", 12), command=decrypt_file_vietnamese, bg="lightyellow", width=30)
decrypt_button_vietnamese.grid(row=3, column=1, padx=15, pady=10)

open_output_button_vietnamese = tk.Button(button_frame, text="Mở file OUTPUT Tiếng Việt", font=("Arial", 12), command=open_output_file_vietnamese, bg="lightcoral", width=30)
open_output_button_vietnamese.grid(row=2, column=1, padx=15, pady=10)

# Nút Thoát để đóng chương trình
exit_button = tk.Button(main_frame, text="Thoát", font=("Arial", 14), command=root.quit, bg="red", width=20)
exit_button.grid(row=2, column=0, pady=30)

root.mainloop()