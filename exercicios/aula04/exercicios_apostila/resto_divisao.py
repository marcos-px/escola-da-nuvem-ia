x, y = map(int, input().split())

if x > y:
    x, y = y, x

for i in range(x+1, y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)