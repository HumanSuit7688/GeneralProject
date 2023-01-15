from func_back_end import sound_count, list, every_let

word = input()
word_list = list(word)

print(sound_count(word_list))
print(every_let(word_list, 1))