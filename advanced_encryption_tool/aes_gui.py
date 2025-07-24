from tkinter import filedialog, messagebox, Tk, Button, Label, Entry
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def pad(data):
    while len(data) % 16 != 0:
        data += b' '
    return data

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        plaintext = f.read()
    cipher = AES.new(pad(key.encode())[:32], AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    with open(filename + '.enc', 'wb') as f:
        f.write(cipher.nonce + tag + ciphertext)
    return filename + '.enc'

def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(pad(key.encode())[:32], AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    with open(filename[:-4] + '_decrypted', 'wb') as f:
        f.write(plaintext)
    return filename[:-4] + '_decrypted'

def choose_encrypt():
    filename = filedialog.askopenfilename()
    key = key_entry.get()
    if not key:
        messagebox.showerror("Error", "Please enter a key!")
        return
    output = encrypt_file(filename, key)
    messagebox.showinfo("Encrypted", f"File encrypted to: {output}")

def choose_decrypt():
    filename = filedialog.askopenfilename()
    key = key_entry.get()
    if not key:
        messagebox.showerror("Error", "Please enter a key!")
        return
    output = decrypt_file(filename, key)
    messagebox.showinfo("Decrypted", f"File decrypted to: {output}")

# GUI
root = Tk()
root.title("AES-256 Encryption Tool")

Label(root, text="Enter Key (min 16 chars):").pack()
key_entry = Entry(root, width=40, show="*")
key_entry.pack()

Button(root, text="Encrypt File", command=choose_encrypt).pack(pady=10)
Button(root, text="Decrypt File", command=choose_decrypt).pack(pady=10)

root.mainloop()
