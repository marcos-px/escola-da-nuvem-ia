#enquanto o número(index) estiver entre(1 e 100)
#Se o número for divisível por dois com resto zero ou divisível por três com resto 0

for i in range(1,101):
    if i % 10 == 0:
        print(f"O número {i} é divisível por 10")