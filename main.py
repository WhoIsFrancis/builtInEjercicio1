def main():
    cant_paises = int(input("Ingrese la cantidad de paises a cargar: "))
    lista_paises = []

    for x in range(cant_paises):
        pais = (input("Pais: ").capitalize())
        lista_paises.append(pais)

    lista_filtrada = set(lista_paises)

    print(sorted(lista_filtrada))


if __name__ == '__main__':
    main()
