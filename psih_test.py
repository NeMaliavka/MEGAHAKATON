import random
question = ['Часто ли Вы испытываете тягу к новым впечатлениям, к тому чтобы отвлечься, испытать сильные ощущения?',
            'Часто ли вы чувствуете, что нуждаетесь в друзьях, которые могут вас понять, одобрить или посочувствовать?',
            'Считаете ли вы себя беззаботным человеком?', 'Очень ли трудно вам отказываться от своих намерений?',
            'Обдумываете ли вы свои дела не спеша и предпочитаете подождать, прежде чем действовать?',
            'Всегда ли вы сдерживаете свои обещания, даже если вам это невыгодно?', 'Часто ли у вас бывают спады и подъемы настроения?',
            'Быстро ли вы обычно действуете и говорите, не затрачиваете ли много времени на обдумывание?',
            'Возникало ли у вас когда-нибудь чувство, что вы несчастны, хотя никакой серьезной причины на это не было?',
            'Верно ли, что "на спор" вы способны решиться на все?',
            'Смущаетесь ли вы, когда хотите познакомиться с человеком противоположного пола, который вам симпатичен?',
            'Бывает ли когда-нибудь, что, разозлившись, вы выходите из себя?', 'Часто ли действуете необдуманно, под влиянием момента?',
            'Часто ли вас беспокоят мысли о том, что вам не следовало чего-либо делать или говорить?', 'Предпочитаете ли вы чтение книг встречам с людьми?',
            'Верно ли, что вас легко задеть?', 'Любите ли вы часто бывать в компании?',
            'Бывают ли у вас такие мысли, которыми вам не хотелось делиться с другими людьми?',
            'Верно ли, что иногда вы настолько полны энергии, что все горит в руках, а иногда вы чувствуете сильную вялость?',
            'Стараетесь ли вы ограничить круг своих знакомств небольшим числом самых близких людей?', 'Много ли вы мечтаете?',
            'Когда на вас кричат, отвечаете ли тем же?', 'Считаете ли вы свои привычки хорошими?',
            'Часто ли у вас появляется чувство, что вы чем-то виноваты?',
            'Способны ли вы иногда дать волю своим чувств и беззаботно развлечься с веселой компанией?',
            'Можно ли сказать, что часто у вас нервы бывают натянуты до предела?',
            'Слывете ли вы за человека веселого и живого?',
            'После того, как дело сделано, часто ли вы мысленно возвращаетесь к нему и думаете, что могли бы сделать лучше?',
            'Чувствуете ли вы себя неспокойно, находясь в большой компании?', 'Бывает ли, что вы передаете слухи?',
            'Бывает ли, что вам не спится из-за того, что в голову лезут разные мысли?',
            'Что вы предпочитаете, если хотите что-либо узнать: найти это в книге или спросить у друзей?',
            'Бывают ли у вас сильные сердцебиения?', 'Нравится ли вам работа, требующая сосредоточения?',
            'Бывают ли у вас приступы дрожи?', 'Всегда ли вы говорите только правду?',
            'Бывает ли вам неприятно находиться в компании, где все подшучивают друг над другом?',
            'Раздражительны ли вы?', 'Нравится ли вам работа, требующая быстрого действия?',
            'Верно ли, что вам часто не дают покоя мысли о разных неприятностях и "ужасах", которые могли бы произойти, хотя все кончилось благополучно?',
            'Верно ли, что вы неторопливы в движениях и несколько медлительны?', 'Опаздывали ли вы когда-нибудь на работу или встречу с кем-то?',
            'Часто ли вам снятся кошмары?', 'Верно ли что вы так любите поговорить, что не упускаете любого удобного случая побеседовать с новым человеком?',
            'Беспокоят ли вас какие-либо боли?', 'Огорчились бы вы, если бы не смогли долго видеться с друзьями?', 'Можете ли вы назвать себя нервным человеком?',
            'Есть ли среди ваших знакомых такие, которые вам явно не нравятся?',
            'Могли бы вы сказать, что вы уверенный в себе человек?', 'Легко ли вас задевает критика ваших недостатков, или вашей работы?',
            'Трудно ли вам получить настоящее удовольствие от мероприятий, в которых участвует много народу?',
            'Беспокоит ли вас чувство, что вы чем-то хуже других?', 'Сумели бы вы внести оживление в скучную компанию?',
            'Бывает ли, что вы говорите о вещах, в которых совсем не разбираетесь?', 'Беспокоитесь ли вы о своем здоровье?',
            'Любите ли вы подшутить над другими?', 'Страдаете ли вы бессонницей?']
# question = ['Часто ли Вы испытываете тягу к новым впечатлениям, к тому чтобы отвлечься, испытать сильные ощущения?',
# 'Часто ли вы чувствуете, что нуждаетесь в друзьях, которые могут вас понять, одобрить или посочувствовать?',
#  'Считаете ли вы себя беззаботным человеком?',
# 'Очень ли трудно вам отказываться от своих намерений?',
# 'Обдумываете ли вы свои дела не спеша и предпочитаете подождать, прежде чем действовать?',
# 'Всегда ли вы сдерживаете свои обещания, даже если вам это невыгодно?',
# 'Часто ли у вас бывают спады и подъемы настроения?',
# 'Быстро ли вы обычно действуете и говорите, не затрачиваете ли много времени на обдумывание?',
# 'Возникало ли у вас когда-нибудь чувство, что вы несчастны, хотя никакой серьезной причины на это не было?',
# 'Верно ли, что "на спор" вы способны решиться на все?',
# 'Смущаетесь ли вы, когда хотите познакомиться с человеком противоположного пола, который вам симпатичен?',
# 'Бывает ли когда-нибудь, что, разозлившись, вы выходите из себя?',
# 'Часто ли действуете необдуманно, под влиянием момента?',
# 'Часто ли вас беспокоят мысли о том, что вам не следовало чего-либо делать или говорить?',
# 'Предпочитаете ли вы чтение книг встречам с людьми?',
# 'Верно ли, что вас легко задеть?',
# 'Любите ли вы часто бывать в компании?',
# 'Бывают ли у вас такие мысли, которыми вам не хотелось делиться с другими людьми?',
# 'Верно ли, что иногда вы настолько полны энергии, что все горит в руках, а иногда вы чувствуете сильную вялость?',
# 'Стараетесь ли вы ограничить круг своих знакомств небольшим числом самых близких людей?',
# 'Много ли вы мечтаете?',
# 'Когда на вас кричат, отвечаете ли тем же?',
# 'Считаете ли вы свои привычки хорошими?',
# 'Часто ли у вас появляется чувство, что вы чем-то виноваты?',
# 'Способны ли вы иногда дать волю своим чувств и беззаботно развлечься с веселой компанией?',
# 'Можно ли сказать, что часто у вас нервы бывают натянуты до предела?',
# 'Слывете ли вы за человека веселого и живого?',
# 'После того, как дело сделано, часто ли вы мысленно возвращаетесь к нему и думаете, что могли бы сделать лучше?']
#
#
# text = '''29. Чувствуете ли вы себя неспокойно, находясь в большой компании?
#
# 30. Бывает ли, что вы передаете слухи?
#
# 31. Бывает ли, что вам не спится из-за того, что в голову лезут разные мысли?
#
# 32. Что вы предпочитаете, если хотите что-либо узнать: найти это в книге или спросить у друзей?
#
# 33. Бывают ли у вас сильные сердцебиения?
#
# 34.Нравится ли вам работа, требующая сосредоточения?
#
# 35. Бывают ли у вас приступы дрожи?
#
# 36. Всегда ли вы говорите только правду?
#
# 37. Бывает ли вам неприятно находиться в компании, где все подшучивают друг над другом?
#
# 38. Раздражительны ли вы?
#
# 39. Нравится ли вам работа, требующая быстрого действия?
#
# 40. Верно ли, что вам часто не дают покоя мысли о разных неприятностях и "ужасах", которые могли бы произойти, хотя все кончилось благополучно?
#
# 41. Верно ли, что вы неторопливы в движениях и несколько медлительны?
#
# 42. Опаздывали ли вы когда-нибудь на работу или встречу с кем-то?
#
# 43. Часто ли вам снятся кошмары?
#
# 44. Верно ли что вы так любите поговорить, что не упускаете любого удобного случая побеседовать с новым человеком?
#
# 45. Беспокоят ли вас какие-либо боли?
#
# 46. Огорчились бы вы, если бы не смогли долго видеться с друзьями?
#
# 47. Можете ли вы назвать себя нервным человеком?
#
# 48. Есть ли среди ваших знакомых такие, которые вам явно не нравятся?
#
# 49. Могли бы вы сказать, что вы уверенный в себе человек?
#
# 50. Легко ли вас задевает критика ваших недостатков, или вашей работы?
#
# 51. Трудно ли вам получить настоящее удовольствие от мероприятий, в которых участвует много народу?
#
# 52. Беспокоит ли вас чувство, что вы чем-то хуже других?
#
# 53. Сумели бы вы внести оживление в скучную компанию?
#
# 54. Бывает ли, что вы говорите о вещах, в которых совсем не разбираетесь?
#
# 55. Беспокоитесь ли вы о своем здоровье?
#
# 56. Любите ли вы подшутить над другими?
#
# 57. Страдаете ли вы бессонницей?'''
#
# lst_text = text.split('\n')
#
# for i in range(len(lst_text)):
#     lst_text[i] = lst_text[i][3:].strip()
#     if lst_text[i] != '':
#         question.append(lst_text[i])
# print(question)
c = 1
user_answer = []
user_id = 1
for q in question:
    print(f'{c}. {q}')
    user = random.randint(0,1)
    print(user)
    user_answer.append(user)
#     if c == 35:
#         break
#     # while True:
#     #     user = int(input('Введите 1, если утверждение верно и 0, если для Вас оно не верно: '))
#     #     if user == 1 or user == 0:
#     #         user_answer.append(user)
#     #         break
    c += 1

B1 = [1, '-', 1, '-', 0, '-', '-', 1, '-', 1, '-', '-', 1,
                '-', 0, '-', 1, '-', '-', 0, '-', 1, '-', '-', 1, '-',
                1, '-', 0, '-', '-', 0, '-', 0, '-', '-', 0, '-', 1,
                '-', 0, '-', '-', 1, '-', 1, '-', '-', 1, '-', 0, '-',
                1, '-', '-', 1, '-']

B2 = ['-', '-', '-', '-', 1, '-', '-', '-', '-', '-', '-', '-',
               '-', '-', 1, '-', '-', '-', '-', 1, '-', '-', '-', '-', '-',
               '-', '-', '-', 1, '-', '-', 1, '-', 1, '-', '-', 1, '-', '-',
               '-', 1, '-', '-', '-', '-', '-', '-', '-', '-', '-', 1, '-',
               '-', '-', '-', '-', '-']

C1 = ['-', 1, '-', 1, '-', '-', 1, '-', 1, '-', 1, '-', '-', 1,
             '-', 1, '-', '-', 1, '-', 1, '-', 1, '-', '-', '-', '-',
             1, '-', '-', 1, '-', 1, '-', 1, '-', '-', 1, '-', 1, '-',
             '-', 1, '-', 1, '-', 1, '-', '-', 1, '-', 1, '-', '-', 1, 1, '-']


# for i in range(1, 58):
#     if i == 1 or i == 3 or i == 8 or i == 10 or i == 13 or i == 17 \
#             or i == 22 or i == 25 or i == 27 or i == 39 or i == 44 \
#             or i == 46 or i == 49 or i == 3 or i == 53:
#         #extraversion.append(1)
#         intoversion.append('-')
#         #neirotizm.append('-')
#     elif i == 5 or i == 15 or i == 20 or i == 29 or i == 32\
#             or i == 34 or i == 37 or i == 41 or i == 51:
#         #extraversion.append(0)
#         intoversion.append(1)
#         #neirotizm.append('-')
#     elif  i == 2 or i == 4 or i == 7 or i == 9 or i == 11 \
#             or i == 14 or i == 16 or i == 19 or i == 21 \
#             or i == 23 or i == 28 or i == 31 or i == 33 or i == 35 \
#             or i == 38 or i == 40 or i == 43 or i == 45 or i == 47 \
#             or i == 50 or i == 52 or i == 55 or i == 56:
#         #extraversion.append('-')
#         intoversion.append('-')
#         #neirotizm.append(1)
#     else:
#         #extraversion.append('-')
#         intoversion.append('-')
#         #neirotizm.append('-')
# print(extraversion, len(extraversion))
# print(intoversion, len(intoversion))
# print(neirotizm, len(neirotizm))

result = {user_id:{'Ложные ответы': 0,
                   'показатель Б': 0,
                   'показатель В': 0,
                   'психотип1': '',
                   'психотип2': ''}}

A1 = [5, 23, 35]
A2 = [11, 17, 29, 41, 47, 53]

# introvert = [5, 15, 20, 29, 32, 34, 37, 41, 51]
# 9 отлавливаемых ложных ответов

for id_ans in range(len(user_answer)):
    if user_answer[id_ans] == 1:
        if id_ans in A2:
            result[user_id]['Ложные ответы'] += 1
        if B2[id_ans] == 1 or B1[id_ans] == 1:
            result[user_id]['показатель Б'] += 1
        elif C1[id_ans] == 1:
            result[user_id]['показатель В'] += 1
    elif user_answer[id_ans] == 0:
        if id_ans in A1:
            result[user_id]['Ложные ответы'] += 1
        if B1[id_ans] == 0:
            result[user_id]['показатель Б'] += 1

if result[user_id]['показатель Б'] == 12 or result[user_id]['показатель В'] == 12:
    result[user_id]['психотип1'] = 'Результат не подлежит анализу'
elif 0 <= result[user_id]['показатель Б'] <= 12 and 0 <= result[user_id]['показатель В'] <= 12:
    result[user_id]['психотип1'] = 'Флегматик'
elif 0 <= result[user_id]['показатель Б'] <= 12 and 12 <= result[user_id]['показатель В'] <= 24:
    result[user_id]['психотип1'] = 'Меланхолик'
elif 12 <= result[user_id]['показатель Б'] <= 24 and 12 <= result[user_id]['показатель В'] <= 24:
    result[user_id]['психотип1'] = 'Холерик'
elif 12 <= result[user_id]['показатель Б'] <= 24 and 0 <= result[user_id]['показатель В'] <= 12:
    result[user_id]['психотип1'] = 'Сангвиник'

#
# print(result)
if result[user_id]['Ложные ответы'] > 4:
    general = 'Ответы ложные, не имеет смысла анализировать данный результат'
elif result[user_id]['показатель Б'] >= 19:
        general = 'яркий экстраверт'
elif result[user_id]['показатель Б'] >= 15:
    general = 'экстраверт'
elif result[user_id]['показатель Б'] >= 12:
    general = 'склонность к экстраверсии'
elif result[user_id]['показатель Б'] == 12:
    general = 'среднее значение, неопределённый тип личности'
elif result[user_id]['показатель Б'] <= 5:
    general = 'глубокий интроверт'
elif result[user_id]['показатель Б'] <= 9:
    general = 'интроверт'
elif result[user_id]['показатель Б'] < 12:
    general = 'склонность к интроверсии'
result[user_id]['психотип2'] = general
print(result)




