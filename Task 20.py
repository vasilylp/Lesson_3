"""Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы."""
# from langdetect import detect, DetectorFactory
# DetectorFactory.seed = 0
#
# dctEnglish = {("A", "E", "I", "O", "U", "L", "N", "S", "T", "R"): 1, ("D", "G"): 2, ("B", "C", "M", "P"): 3, ("F", "H", "V", "W", "Y"): 4, ("K",): 5, ("J", "X"): 8, ("Q", "Z"): 10}
# dctRussin = {('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'): 1, ('Д', 'К', 'Л', 'М', 'П', 'У'): 2, ('Б', 'Г', 'Ё', 'Ь', 'Я'): 3,('Й', 'Ы'): 4, ('Ж', 'З', 'Х', 'Ц', 'Ч'): 5, ('Ш', 'Э', 'Ю'): 8, ('Ф', 'Щ', 'Ъ'): 10 }
# word = input("Введите слово : ")
# score = 0
# detect_language = detect(word)
# if detect_language == 'sw':
#     for w in word:
#         for i in dctEnglish :
#             for j in i:
#                 if w == j:
#                     score += dctEnglish[i]
# else:
#     for w in word:
#         for i in dctRussin :
#             for j in i:
#                 if w == j:
#                     score += dctRussin[i]
#
# print(score)

# 2 solution _________________________________________________________

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}

word = input("Введите слово : ").upper()
count = 0
if word[0] in 'AEIOULNSTRDGBCMPFHVWYKJXQZ':
    for sym in word:
        for point in points_en:
            if sym in points_en[point]:
                count += point
else:
    for sym in word:
        for point in points_ru:
            if sym in points_ru[point]:
                count += point

print(f"Ура у вас {count} очков !")
