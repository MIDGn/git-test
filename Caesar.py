# print('Введите текст, который необходимо обработать')
s = input().split()
# print('Шифрование или дешифрование? 1 - Шифрование, 0 - Дешифрование')
type_op = 1
# print('Какой язык? 1 - Русский, 0 - Английский')
lang = 0
# print('Шаг сдвига?')
# rot = int(input())

# ru_low = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# ru_up = ru_low.upper()
eng_low = 'abcdefghijklmnopqrstuvwxyz'
eng_up = eng_low.upper()

def caesar(s, rot):
    ans = ''
    for c in s:
        if c.isalpha():
            if lang == 1:
                if c == c.upper():
                    print(c)
                    if type_op == 1:
                        c = ru_up[(ru_up.find(c) + rot) % 32]
                    else:
                        c = ru_up[(ru_up.find(c) - rot) % 32]
                else:
                    if type_op == 1:
                        c = ru_low[(ru_low.find(c) + rot) % 32]
                    else:
                        c = ru_low[(ru_low.find(c) - rot) % 32]
            else:
                if c == c.upper():
                    if type_op == 1:
                        c = eng_up[(eng_up.find(c) + rot) % len(eng_up)]
                    else:
                        c = eng_up[(eng_up.find(c) - rot) % len(eng_up)]
                else:
                    if type_op == 1:
                        c = eng_low[(eng_low.find(c) + rot) % len(eng_low)]
                    else:
                        c = eng_low[(eng_low.find(c) - rot) % len(eng_low)]
        ans += c
    return ans
ans = ''
l_w = []
for w in s:
    rot = 0
    for i in w:
        if i.isalpha():
            rot += 1
    ans += caesar(w, rot) + ' '
print(ans)
