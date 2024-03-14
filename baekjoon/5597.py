import sys

list = list(range(1, 31))
for i in range(28):
    try:
        list.remove(int(sys.stdin.readline().rstrip()))
    except:
        pass

for i in sorted(list):
    print(i)