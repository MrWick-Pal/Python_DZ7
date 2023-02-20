# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод: Парам пам-пам
stroka = input('Введите стих: ')
stroka = stroka.lower().split(' ')

def counter(frase):
    glas_list = ['а','о','э','е','и','ы','у','ё','ю','я']
    glas_counter = 0
    for fra in frase:
        for char in fra:
            for letter in glas_list:
                if char == letter:
                    glas_counter += 1       
    return glas_counter

def check_song_rythm(song_rythm):
    flag = 0
    for i in range(len(song_rythm) - 1):
        if song_rythm[i] == song_rythm[i + 1]:
            continue
        else:
            flag += 1
            break
    if flag == 0:
        awnser = print("Парам пам-пам")
        return awnser
    if flag == 1:
        awnser = print("Пам парам")
        return awnser

rythm = list(map(counter, stroka))
check_song_rythm(rythm)