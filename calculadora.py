# Calculadora simples

while True:

    print("\n\t\t\t -- Calculadora Simples --")
#deixar sair por ultimo pfvr
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação") 
    print("4. Divisão")
    print("5. Modulo")
    print("6. Sair")
    

    op = int(input("\nOpção: "))

    if op == 1:
        print("\n\t\t\t -- Soma -- \n")

        # Entrada
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))

        # Processamento
        total = n1 + n2
        print("\n\t\t{} + {} = {:.2f}\n".format(n1, n2, total)) 
        
    elif op == 2: # usar elif tbm
        print("\n\t\t\t -- Subtração --\n")

        n1 = float(input("informe N1: "))
        n2 = float(input("informe N2: "))

        total = n1 - n2 

        print("\n\t\t{} - {} = {}\n" .format(n1,n2,total))

    elif op == 3: 
        print("\n\t\t -- Multiplicação -- \n")

        n1 = float(input("informe N1: "))   
        n2 = float(input("informe N2: ")) 

        total = n1 * n2 

        print("\n\t\t{} x {} = {}\n" .format(n1,n2,total))

    elif op == 4:
        print("\n\t\t -- Divisão -- \n")
        
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))
    
        if n2 == 0:
            print("\n\t -- Erro: Não é possível dividir por 0! -- \n")
            continue
        
    
        total = n1/n2
        
        print("\n\t\t{} / {} = {:.2f}\n".format(n1, n2, total))

    elif op == 5:
        print("\n\t\t -- Modulo -- \n")
        
        n1 = float(input("Informe N1: "))
        n2 = float(input("Informe N2: "))
        
        total = n1 % n2
        
        print("\n\t\t{} % {} = {}\n".format(n1,n2,total))

        

    elif op == 6:
        print("\n\nAbraço!!\n\n")
        break
    else:
        print("\n\nOpção {} incorreta!\n\n".format(op))

