

string_count_dic = {}
text = input("Write a sentece>").lower()
words = text.split()

for word in words:
    if word in string_count_dic:
        string_count_dic[word] += 1
    else:
        string_count_dic[word] = 1

for x,y in sorted(string_count_dic.items()):
    print('{:} is {}'.format(x,y))