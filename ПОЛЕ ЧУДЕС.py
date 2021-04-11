my_word = input().split()
for i in range(len(my_word)):
    i = input()
    if i not in my_word:
        print(False)
    else:
        print(i)