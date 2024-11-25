from conversor_idade import conversor_idade

dias = int(input("Digite a idade em dias: "))

anos, meses, dias = conversor_idade(dias)


print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")