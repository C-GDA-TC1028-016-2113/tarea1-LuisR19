def main():
    #escribe tu código abajo de esta línea
    pesoInicial = float(input("Dame el peso inicial: "))
    pesoFinal = float(input("Dame el peso final: "))
    meses = float(input("Dame la cantidad de meses: "))

    metaPeso = (pesoInicial - pesoFinal)/meses

    print(f"Lo que debes bajar por mes es: {metaPeso}" )

if __name__ == '__main__':
    main()
