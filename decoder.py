import base64
import codecs


def decode_base64(data):
    try:
        decoded = base64.b64decode(data, validate=True)
        return decoded.decode()
    except Exception:
        return "Error: Invalid Base64 input."


def decode_hex(data):
    try:
        decoded = bytes.fromhex(data)
        return decoded.decode()
    except Exception:
        return "Error: Invalid hexadecimal input."


def decode_binary(data):
    try:
        parts = data.split()

        result = ""

        for part in parts:

            if len(part) != 8:
                return "Error: Binary values should be 8 bits."

            number = int(part, 2)

            result += chr(number)

        return result

    except Exception:
        return "Error: Invalid binary input."


def decode_rot13(data):
    try:
        return codecs.decode(data, "rot_13")
    except Exception:
        return "Error: ROT13 decoding failed."


def decode_caesar(data, shift):
    result = ""

    for ch in data:

        if ch.isalpha():

            base = ord("A") if ch.isupper() else ord("a")

            result += chr((ord(ch) - base - shift) % 26 + base)

        else:
            result += ch

    return result


print("""
=========================
      MULTI DECODER
=========================

1. Base64
2. Hex
3. Binary
4. ROT13
5. Caesar Cipher

=========================
""")

choice = input("Enter choice: ").strip()

data = input("Enter encoded text: ").strip()

if choice == "1":

    print("\nDecoded:", decode_base64(data))

elif choice == "2":

    print("\nDecoded:", decode_hex(data))

elif choice == "3":

    print("\nDecoded:", decode_binary(data))

elif choice == "4":

    print("\nDecoded:", decode_rot13(data))

elif choice == "5":

    shift_input = input("Enter Caesar shift: ").strip()

    try:

        shift = int(shift_input)

        print("\nDecoded:", decode_caesar(data, shift))

    except ValueError:

        print("Error: Shift must be an integer.")

else:

    print("Error: Invalid menu choice.")