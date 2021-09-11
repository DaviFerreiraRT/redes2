import csv
ip=[]
mask = []
interface=[]
with open('tabelaRota.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        ip.append(row[0])
        mask.append(row[1])
        interface.append(row[2])


ipFormatado = ip[1:]
maskFormatada = mask[1:]
interfaceFormatada = interface[1:]

a = ipFormatado[0]

primeiraParte = a[0:a.index(".")]

print(bin(int(primeiraParte))[2:])

