from Crypto.Cipher import AES
import os

# Load the AES key and IV from the 'key.txt' file
with open('key.txt', 'rb') as key_file:
    key = key_file.read(32)  # AES-256 key is 32 bytes
    iv = key_file.read(16)  # AES block size is 16 bytes for CBC mode


# Decrypt the .enc file
def decrypt_file(file_path):
    # Check if the file is already decrypted
    if not file_path.endswith(".enc"):
        print(f"Skipping non-encrypted file: {file_path}")
        return

    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    # Set up AES decryption
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove padding
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    # Save the decrypted file without the .enc
#    decrypted_file_path = file_path[:-8]+".decrypted"+file_path[-8:-4]
    decrypted_file_path = file_path.replace(".enc", ".decrypted")
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

    print(f"Decrypted file saved as {decrypted_file_path}")


# Insert your own path
decrypt_file('user/date/file-name.xxx.enc')
