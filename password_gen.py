from random import *

def gen_pass(length, chars):
    s = ''
    m = sample(chars, length)
    for c in m:
        s += c
    return s

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exclude = 'il1Lo0O'
chars = ''

print('Сколько паролей сгенерировать?')
n = int(input())
print('Длина пароля?')
length = int(input())
print('Включить в пароль цифры 0123456789? 1 - Да, 0 - Нет')
is_dig = int(input())
print('Включить в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? 1 - Да, 0 - Нет')
is_upper = int(input())
print('Включить в пароль строчные буквы abcdefghijklmnopqrstuvwxyz? 1 - Да, 0 - Нет')
is_lower = int(input())
print('Включить в пароль символы !#$%&*+-=?@^_? 1 - Да, 0 - Нет')
is_symbol = int(input())
print('Исключить из пароля неоднозначные символы il1Lo0O? 1 - Да, 0 - Нет')
is_exclude = int(input())

if is_dig:
    chars += digits
if is_upper:
    chars += uppercase_letters
if is_lower:
    chars += lowercase_letters
if is_symbol:
    chars += punctuation
if is_exclude:
    for c in exclude:
        chars = chars.replace(c, '')
for i in range(n):
    print(gen_pass(length, chars))