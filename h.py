# word = input()
#
# word_list = []
# x = 0
# for l in word:
#     word_list.append(word[x])
#     x += 1
#
# for i in word_list:
#     print(i)
#
# print(len(word))
# print(word_list)
# x = {'я' : ['й', 'а'], 'ю' : ['й', 'у']}
# print(x.get('я'))

# w = input()
# print(w.lower())

# word = input()
# word_list = []
# for i in word:
#     word_list.append(i)
#
# print(word_list)


# word = input()
# w = word[5:-1]
# e = word[-2:]
# print(w)
# print(e)

x = ['а', 'б', 'в', 'г', 'д']
index = 0
for i in x:
    if index > 0:
        index_i = x.index(i, index)
        print(f'Старый - {x[index_i]}')
        print(f'Новый - {x[index]}')
    else:
        print("НЭТ")
    index += 1