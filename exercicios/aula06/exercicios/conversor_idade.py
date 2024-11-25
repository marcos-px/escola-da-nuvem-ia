

def conversor_idade(dias):
    anos = dias // 365
    dias_restantes = dias % 365
    meses = dias_restantes // 30
    dias_final = dias_restantes % 30
    return anos, meses, dias_final
