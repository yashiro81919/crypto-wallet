from bitcoinlib.mnemonic import Mnemonic
import aes

file_path = "new_seed"

# generate new seed
obj = Mnemonic()
phrase = obj.generate(strength=256)
entropy = obj.to_entropy(phrase).hex()

# encrypt seed and save to file
passphrase = input("Passphrase:")
encrypted_data = aes.aes256gcm_encode(bytes(phrase, "utf-8"), passphrase)
with open(file_path, 'w') as file:
    file.write(encrypted_data.hex())

print("Recovery phrase:", phrase)
print("Entropy:", entropy)