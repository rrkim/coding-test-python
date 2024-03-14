s = str(input())

length = len(s)
list = []
for i in range(1, length):
    for k in range(i+1, length):
        list.append(s[0:i][::-1] + s[i:k][::-1] + s[k:length][::-1])

print(sorted(list)[0])