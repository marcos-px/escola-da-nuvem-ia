n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    if y == 0:
        print("divisao impossivel")
    else:
        print(f"{x / y:.1f}")