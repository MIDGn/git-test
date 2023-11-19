from random import *

def is_valid_ans(text):
    if text.isdigit():
        if 0 <= int(text) <= 1:
            return True
        else:
            return False
    else:
        return False

pos_ans = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен(а) в этом']
semi_pos_ans = ['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']
neut_ans = ['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
            'Сконцентрируйся и спроси опять']
neg_ans = ['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
           'Весьма сомнительно']
res = []
res.append(pos_ans)
res.append(semi_pos_ans)
res.append(neut_ans)
res.append(neg_ans)
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как Вас зовут?')
name = input()
print(f'Привет, {name}')

while True:
    print('Какой вопрос тебя интересует?')
    quest = input()
    x = randint(0, 3)
    print(choice(res[x]))
    ans = input('Хотите спросить еще раз? 1 - Да, 0 - Нет\n')
    if is_valid_ans(ans):
        if int(ans) == 0:
            print('Возвращайся если возникнут вопросы!')
            break
