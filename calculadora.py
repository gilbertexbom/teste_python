# Calculadora simples

while True:

    print("\n\t\t\t -- Calculadora Simples --")

    print("1. Soma")
    print("2. Sair")

    op = int(input("\nOpção: "))

    if op == 1:
        print("\n\t\t\t -- Soma -- \n")

        # Entrada
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))

        # Processamento
        total = n1 + n2

        # Saída
        print("\n\t\t{} + {} = {:.2f}\n".format(n1, n2, total))

    elif op == 2:
        print("\n\nAbraço!!\n\n")
        break
    else:
        print("\n\nOpção {} incorreta!\n\n".format(op))

