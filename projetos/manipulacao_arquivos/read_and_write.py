with open("agile.txt", "r+") as file:
    content = file.read()
    print('Conteúdo inicial: ', content)
    file.write('E um Product Owner.\n')