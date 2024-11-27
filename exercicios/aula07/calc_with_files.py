def process_numbers_file(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    total = sum(numbers) #total
    average = total / len(numbers) #media
    min_value = min(numbers) #minimo
    max_value = max(numbers) #maximo

    return total, average, min_value, max_value

if __name__ == "__main__":
    file_name = input("Digite o nome do arquivo: ")
    total, average, min_value, max_value = process_numbers_file(file_name)

    print(f"Soma: {total}")
    print(f"Média: {average:.2f}")
    print(f"Menor {min_value}")
    print(f"Maior: {max_value}")

