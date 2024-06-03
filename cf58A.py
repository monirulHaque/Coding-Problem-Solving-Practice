s = input()
word = "hello"
i = 0
flag = False
for c in s:
    if c == word[i]:
        i += 1
    if i == len(word):
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")