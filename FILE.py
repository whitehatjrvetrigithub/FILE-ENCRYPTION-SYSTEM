from tkinter import *
from tkinter import filedialog as fd
import hashlib

root = Tk()
root.title("File Encryption System")
root.geometry("300x240")
root.config(bg = "cyan")

def apply_md5():
    print("MD5 Function")
    text_file = fd.askopenfilename(title = "Open Text File", filetypes = (("Text Files", "*.txt"), ))
    print(text_file)
    read_file = open(text_file, 'r')
    paragraph = read_file.read()
    file_result = hashlib.md5(paragraph.encode())
    file_hexd = file_result.hexdigest()
    md5_file = open(text_file, 'w')
    md5_file.write(file_hexd)
    print(file_hexd)
    md5_file.close()
    
def apply_sha256():
    print("SHA Function")
    print("MD5 Function")
    text_file2 = fd.askopenfilename(title = "Open Text File", filetypes = (("Text Files", "*.txt"), ))
    print(text_file2)
    read_file2 = open(text_file2, 'r')
    paragraph2 = read_file2.read()
    file_result2 = hashlib.md5(paragraph2.encode())
    file_hexd2 = file_result2.hexdigest()
    sha256_file = open(text_file2, 'w')
    sha256_file.write(file_hexd2)
    print(file_hexd2)
    sha256_file.close()
    
btn = Button(root, text = "Apply MD5", command = apply_md5, bg = "orange", fg = "white", relief = "flat")
btn.place(relx = 0.3, rely = 0.5, anchor = CENTER)

btn1 = Button(root, text = "Apply SHA256", command = apply_sha256, bg = "orange", fg = "white", relief = "flat")
btn1.place(relx = 0.7, rely = 0.5, anchor = CENTER)

root.mainloop()