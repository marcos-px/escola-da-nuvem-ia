with open("agile.txt", "r") as file:
    line = file.readlines()
    print("Todas as linhas: ", line)
    file.close()