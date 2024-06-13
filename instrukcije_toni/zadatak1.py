def zbroj_znamenki(broj):
    broj_s = str(broj)
    zbroj_znamenki = 0
    for znamenka in broj_s:
        zbroj_znamenki = zbroj_znamenki + int(znamenka)
    return zbroj_znamenki


lista_brojeva = []
for i in range(10):
    broj = int(input("Unesi broj: "))
    lista_brojeva.append(broj)

sortirana_lista = sorted(lista_brojeva, key=zbroj_znamenki)

print(sortirana_lista)


print(zbroj_znamenki(12234))
