from question import QUESTION
def result_test(result: dict, user_id: str):
    if result[user_id]['False answer'] > 4:
        general = 'Ответы ложные, не имеет смысла анализировать данный результат'
    elif result[user_id]['extraversion'] >= 19:
        general = 'яркий экстраверт'
    elif result[user_id]['extraversion'] >= 15:
        general = 'экстраверт'
    elif result[user_id]['extraversion'] >= 12:
        general = 'склонность к экстраверсии'
    elif result[user_id]['extraversion'] == 12:
        general = 'среднее значение, неопределённый тип личности'
    elif result[user_id]['extraversion'] <= 5:
        general = 'глубокий интроверт'
    elif result[user_id]['extraversion'] <= 9:
        general = 'интроверт'
    elif result[user_id]['extraversion'] < 12:
        general = 'склонность к интроверсии'
    else:
        general = 'error'
    return general

c = 1
user_answer = [] #приходит с сайта
user_id = 'email_user' #приходит с сайта
# for q in QUESTION:
#     print(f'{c}. {q}')
#     while True:
#         user = int(input('Введите 1, если утверждение верно и 0, если для Вас оно не верно: '))
#         if user == 1 or user == 1:
#             user_answer.append(user)
#             break
#     c += 1

extraversion = [1, '-', 1, '-', 0, '-', '-', 1, '-', 1,
                '-', '-', 1, '-', 0, '-', 1, '-', '-',
                0, '-', 1, '-', '-', 1, '-', 1, '-', 0,
                '-', '-', 0, '-', 0, '-', '-', 0, '-',
                1, '-', 0, '-', '-', 1, '-', 1, '-', '-',
                1, '-', 0, '-', 1, '-', '-', '-', '-']

neirotizm =  [1, 1, '-', '-', 1, 1, 1, '-', 1, '-', 1,
              '-', 1, '-', 1, 1, '-', '-', 1, '-', '-',
              1, '-', 1, '-', 1, '-', '-', 1, 1, '-', '-',
              1, 1, 1, '-', 1, '-', 1, '-', 1, 1, '-']

print(extraversion)
print(neirotizm)

result = {user_id:{'extraversion': 0,
                   'intoversion': 0,
                   'neirotizm': 0,
                   'False answer': 0,
                   'catrgory': ''}}
false_mines_answer = [11, 17, 29, 41, 47, 53]
false_plus_answer = [5, 23, 36]

for id_ans in range(len(user_answer)):
    if user_answer[id_ans] == 1:
        if extraversion[id_ans] == 1:
            result[user_id]['extraversion'] += 1
        elif neirotizm[id_ans] == 1:
            result[user_id]['neirotizm'] += 1
        elif id_ans in false_plus_answer:
            result[user_id]['False answer'] += 1
    elif user_answer[id_ans] == 0:
        if id_ans in false_mines_answer:
            result[user_id]['False answer'] += 1
        elif extraversion[id_ans] == 0:
            result[user_id]['extraversion'] += 1


result_test(result, user_id)



