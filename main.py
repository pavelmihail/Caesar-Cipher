def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            result += char

    return result

def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        plaintext = file.read()
        encrypted_text = caesar_cipher(plaintext, shift)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        encrypted_text = file.read()
        decrypted_text = caesar_cipher(encrypted_text, -shift)

    with open(output_file, 'w') as file:
        file.write(decrypted_text)

# Example usage:
input_filename = 'input.txt'
output_filename_encrypted = 'encrypted_output.txt'
output_filename_decrypted = 'decrypted_output.txt'
shift_amount = 3

# Encrypt the content of the input file and write to an encrypted output file
encrypt_file(input_filename, output_filename_encrypted, shift_amount)

# Decrypt the content of the encrypted output file and write to a decrypted output file
decrypt_file(output_filename_encrypted, output_filename_decrypted, shift_amount)
