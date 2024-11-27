def process_training_logs(file_name):
    """
    Aqui cria-se um docstrings
    """

    with open(file_name, 'r') as file:
        logs = [line.strip().split(",") for line in file.readlines()]
    
    total_time = 0
    precisions = []
    losses = []
    batches = []

    for log in logs:
        batch_id, time, precision, loss = log[0],int(log[1]), float(log[2]), float(log[3])

        # batch_id = log[0]
        # time = int(log[1])
        # precision = float(log[2])
        # loss = float(log[3])

        total_time += time
        precisions.append(precision)
        losses.append(loss)
        batches.append(batch_id)
    
    average_precision = sum(precisions) / len(precisions)
    batches_high_loss = sum(1 for l in losses if l > 0.5)

    max_precision_batch = batches[precisions.index(max(precisions))]
    min_precision_batch = batches[precisions.index(min(precisions))]

    return total_time, average_precision, batches_high_loss, max_precision_batch, min_precision_batch

if __name__ == "__main__":
    file_name = input("Digite o nome do arquivo: ")

    try:

        total_time, average_precision, batch_loss, max_batch, min_batch = process_training_logs(file_name)

        print(f"Tempo total de treinamento: {total_time} segundos")
        print(f"Precisão Média: {average_precision:.2f}%")
        print(f"Lote com maior precisão: {max_batch}")
        print(f"Lote com menor precisão: {min_batch}")
        print(f"Lote com perda maior que > 0.5: {batch_loss}")


    except FileNotFoundError:
        print(f"Arquivo {file_name} não encontrado na base de dados.")
    except Exception as e:
        print(f"Ocorreu um erro {e}")