import math
import random

alpha = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special_char = '@#$%&*'

length = int(input('Enter Length of Password to be generated: '))

alpha_length = length//2
num_length = math.ceil(length*30/100)
special_len = length-alpha_length-num_length

password = []

def generate(length, str, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(str)-1)
        char = str[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                char = char.upper()
        password.append(char)

generate(alpha_length, alpha, True)
generate(num_length, numbers)
generate(special_len, special_char)

random.shuffle(password)
generatedPassword = ''
for i in password:
    generatedPassword = generatedPassword + str(i)
print(generatedPassword)