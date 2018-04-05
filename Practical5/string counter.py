

string_dic = {}
text = input("Write a sentece>").lower()
words = text.split()

for word in words:
    if word in words:
        string_dic[word] += 1
    else:
        string_dic[word] = 1

for x,y in sorted(string_dic.items()):
    print('{:{}} is {}'.format(x,len(x),y))