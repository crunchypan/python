import random
import string

def rand_sub(char):
    if char.isupper():
        new_char = random.choice(string.ascii_uppercase)
    else:
        new_char = random.choice(string.ascii_lowercase)
    return new_char

user_input = input("Enter file name: ")
user_file = open(user_input, "r")
file = user_file.read()

result = ""

for char in file:
    if char.isalpha():
        new_char = rand_sub(char)
        result += new_char
    else:
        result += char
        
output_file_path = 'output.txt'
output_file = open(output_file_path, 'w')
output_file.write(result)
output_file.close()

print("Result saved as output.txt")