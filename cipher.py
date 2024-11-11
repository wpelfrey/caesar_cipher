# add your code here
#Caesar Cipher 

alphabet_subs = {"a": "f", "b": "g", "c": "h", "d": "i", "e": "j", "f": "k", "g": "l",
                 "h": "m", "i": "n", "j": "o", "k": "p", "l": "q", "m": "r", "n": "s",
                 "o": "t", "p": "u", "q": "v", "r": "w", "s": "x", "t": "y", "u": "z",
                 "v": "a", "w": "b", "x": "c", "y": "d", "z": "e",}

plain_text = input("Please enter a sentence: ")
plain_text = plain_text.lower()

print(plain_text)

secret_code = ""
for char in plain_text:
    if char in alphabet_subs:
        char = alphabet_subs[char]
    secret_code += char

print(secret_code)

