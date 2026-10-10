# CipherForge

A lightweight Python toolkit for decoding encoded data and classical ciphers commonly encountered in cybersecurity labs, CTF challenges, and forensic investigations.

## Supported Formats

- Base64
- Hexadecimal
- Binary
- ROT13
- Caesar Cipher

## Why CipherForge?

During security assessments and CTFs, analysts frequently encounter encoded or obfuscated data. CipherForge provides a simple command-line solution to quickly decode multiple formats from a single interface.

## Features

✔ Multi-format decoding  
✔ Error handling  
✔ Input validation  
✔ Beginner-friendly CLI  
✔ CTF-ready workflow  

## Installation

### Clone the repository

```bash
git clone https://github.com/mdwasifraza01/CipherForge.git
```

### Navigate to the project directory

```bash
cd CipherForge
```

### Verify Python installation

```bash
python --version
```

or

```bash
python3 --version
```

## Usage

Run the tool:

```bash
python decoder.py
```

or

```bash
python3 decoder.py
```

Follow the on-screen menu to select a decoding method and provide the encoded input.

## Example

Encoded Input:

```text
68656c6c6f
```

Decoded Output:

```text
hello
```

## Project Structure

```text
CipherForge/
│
├── decoder.py
├── README.md
```

## Future Improvements

- Automatic format detection
- Encoding support (Base64, Hex, Binary)
- Hash generation (MD5, SHA256)
- File-based decoding
- GUI version

## Author

**Md Wasif Raza**

Cybersecurity Student | Offensive Security Enthusiast
