import random
import datetime

class Enigma:
    
    def __init__(self, message):
        self.message = message.lower()
        self.shiftable_characters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [" "]
        
    def get_shifts(self):
        rand_digit = str(random.randint(0, 99999)).zfill(5)
        keys = [int(rand_digit[0]), int(rand_digit[1])]
        for i in range(2, len(rand_digit)):
            keys.append(int(rand_digit[i]))
        
        current_date = datetime.datetime.now()
        date_key = int(f"{current_date.day:02}{current_date.month:02}{str(current_date.year)[2:]}") ** 2
        date_key_str = str(date_key)
        offsets = [int(d) for d in date_key_str[-4:]]
        
        shifts = [keys[i] + offsets[i] for i in range(4)]
        return shifts
    
    def encrypt(self):
        shifts = self.get_shifts()
        encrypted_message = []
        for i, char in enumerate(self.message):
            if char in self.shiftable_characters:
                char_index = self.shiftable_characters.index(char)
                shift = shifts[i % len(shifts)]
                encrypted_char = self.shiftable_characters[(char_index + shift) % len(self.shiftable_characters)]
                encrypted_message.append(encrypted_char)
            else:
                encrypted_message.append(char)
        return ''.join(encrypted_message), shifts
    
    
    def decrypt(self, encrypted_message, shifts):
        decrypted_message = []
        for i, char in enumerate(encrypted_message):
            if char in self.shiftable_characters:
                char_index = self.shiftable_characters.index(char)
                shift = shifts[i % len(shifts)]
                decrypted_char = self.shiftable_characters[(char_index - shift) % len(self.shiftable_characters)]
                decrypted_message.append(decrypted_char)
            else:
                decrypted_message.append(char)
        return ''.join(decrypted_message)


# ------------------------------- Example ---------------------------- #
message = "hello world"
message0 = "It's worth noting that WhatsApp's revenue model is focused on providing value to businesses and organizations while maintaining a free and user-friendly experience for individuals. This approach has allowed WhatsApp to maintain a large and engaged user base while generating significant revenue."
message1 = "hello world, seedy!"
message2 = "hello, veronica!"
enigma = Enigma(message)

# Encrypt
encrypted_message, shifts = enigma.encrypt()
print("Encrypted Message:", encrypted_message)
print("Shifts:", shifts)

# Decrypt
decrypted_message = enigma.decrypt(encrypted_message, shifts)
print("Decrypted Message:", decrypted_message)