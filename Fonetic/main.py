from func_back_end import sound_count, list, every_let
from info_back_end import special_vowels, vowels

word = input()
word_list = list(word)

print(sound_count(word_list))
ev_let = every_let(word_list, 2)
index = 0
for p in ev_let:
    if p[0] in special_vowels and p[1] in vowels:
        print(f'{p[0]} - ['
              f'{p[1]}] - {p[2]}{p[3]}')
    elif p[0] in special_vowels:
        x = f'{p[0]} - '
        for d in p[1]:
            x += d
        print(x)
        print(f'  - {p[2]}{p[3]}{p[4]}')
    else:
        y = ''
        for a in p:
            y += a
        print(y)
    index += 1

print('\n')
print('\n')
for i in ev_let:
    print(i)