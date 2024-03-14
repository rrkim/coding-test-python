E_max = 15
S_max = 28
M_max = 19

user_e, user_s, user_m = map(int, input().split())
e, s, m = 0, 0, 0

year = 0
while e != user_e or s != user_s or m != user_m:
    year += 1
    e = (e % E_max) + 1
    m = (m % M_max) + 1
    s = (s % S_max) + 1

print(year)
