# 🔐 Advanced Encryption Tool

## 📌 Internship Task-4 | File Encryption & Decryption using AES-256

This project is a **robust encryption and decryption tool** built using Python's `AES-256` algorithm. It features a **user-friendly GUI** that allows you to securely encrypt and decrypt any file using a 256-bit key.

---

## 🚀 Features

- 🔒 AES-256 encryption (using `Crypto.Cipher.AES` from `pycryptodome`)
- 📁 Encrypt and Decrypt **any file** (text, image, PDF, etc.)
- 🧠 Key-based access (Minimum 16 characters)
- 🖥️ Easy-to-use Graphical Interface built with `tkinter`
- 📂 Output saved in the same directory as the selected file

---

## 🛠️ Requirements

- Python 3.x
- `pycryptodome` (for AES encryption)
- `tkinter` (GUI module - pre-installed on most systems)

### Install dependencies:

```bash
# Create a virtual environment (recommended)
python3 -m venv encryption_env
source encryption_env/bin/activate

# Install required libraries
pip install pycryptodome

sudo apt install python3-tk
