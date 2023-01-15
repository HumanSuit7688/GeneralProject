word = input()

word_list = []
x = 0
for l in word:
    word_list.append(word[x])
    x += 1

for i in word_list:
    print(i)

print(len(word))
print(word_list)