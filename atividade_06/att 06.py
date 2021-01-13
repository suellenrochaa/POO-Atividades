import csv
import matplotlib.pyplot as plt

with open("tabela.csv") as arquivo_csv:

    ler = csv.reader(arquivo_csv, delimiter=",")
    num = []
    nome = []

    for colunas in ler:
        num.append(int(colunas[0]))
        nome.append(colunas[1])

    plt.plot(num, nome)
    plt.show()

    fig, ax = plt.subplots()
    ax.pie(num, labels=nome, startangle=90, autopct='%d')
    plt.show()

    plt.bar(nome, num)
    plt.show()
