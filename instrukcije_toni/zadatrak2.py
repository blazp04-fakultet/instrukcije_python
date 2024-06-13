
lista_brojeva = []
for i in range(10):
    broj = float(input("Unesi broj: "))
    lista_brojeva.append(int(broj//1))


def provjera_parnosti(broj):
    if broj % 2 == 0:
        return 0
    else:
        return 1


sortirana_lista = sorted(lista_brojeva, key=provjera_parnosti)


print(sortirana_lista)
