import random, string

length = int(input("Password length: "))
print("Choose complexity:")
print("1. Letters only")
print("2. Letters + numbers")
print("3. Letters + numbers + symbols")
level = int(input("Your choice (1-3): "))

if level == 1:
    chars = string.ascii_letters
elif level == 2:
    chars = string.ascii_letters + string.digits
else:
    chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choices(chars, k=length))
print("Generated Password:", password)
