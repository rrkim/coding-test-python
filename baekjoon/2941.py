croatia_dict = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
text = input()
for i in croatia_dict:
    text = text.replace(i, '*')

print(len(text))