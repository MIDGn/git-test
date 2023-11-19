import random as r

def is_valid(text, r):
    if text.isdigit():
        if 1 <= int(text) <= r:
            return True
        else:
            return False
    else:
        return False

def is_valid_ans(text):
    if text.isdigit():
        if 0 <= int(text) <= 1:
            return True
        else:
            return False
    else:
        return False

while True:
    print('Добро пожаловать в числовую угадайку')
    print('Введите число r, чтобы угадать случайное число от 1 до r')
    right = int(input())
    x = r.randint(1, right)
    tries = 0
    while True:
        n = input('Попробуйте угадать число: ')
        tries += 1
        if is_valid(n, right):
            n = int(n)
            if n > x:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n < x:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print(f'Количество попыток: {tries}')
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {right}?')
    ans = input('Хотите сыграть еще раз? 1 - Да, 0 - Нет\n')
    if is_valid_ans(ans):
        if int(ans) == 0:
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')