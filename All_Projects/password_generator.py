import random
import string

s = string.ascii_letters + string.digits + string.punctuation

print("Available characters:")
print(s)

n = int(input("Enter the length of password: "))
passwd = "".join(random.choice(s) for i in range(n))

print("Your password is:", passwd)