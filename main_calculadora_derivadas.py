import os, time
from functions_calculadora_derivadas import Estilo, Derivada

while True:
    print(f"\n{Estilo.negrito}{" CALCULADORA DE DERIVADAS ":=^60}{Estilo.normal}") # Título

    # Opções de operações (1 à 4) para escolher
    try:
        operacao = int(input('''
{} - Escolha a operação que deseja calcular: {}                     
    {}[1]{} Potenciação, soma e subtração ( ^ | + | - )
    {}[2]{} Multiplicação (*)
    {}[3]{} Quociente (/)
    {}[4]{} Sair
    {}-> {}'''.format(Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal)))
    except:
        operacao = 0 # Caso seja digitado algo inválido (impossível determinar)

    # Verifica se a opção escolhida é válida, direcionando ou retornando erro
    match (operacao):
        case 1: # POTENCIAÇÃO, SOMA E SUBTRAÇÃO
            equacao = input("\n{} - Digite a função a ser derivada: {}".format(Estilo.negrito, Estilo.normal)).strip().lower()

            try:
                equacao_derivada = Derivada(equacao)
                resolucao = equacao_derivada.potencia()
            except ValueError as erro:
                print(f"\n {Estilo.invertido}{erro}{Estilo.normal}")
            else:
                print(f'''    {Estilo.negrito}->{Estilo.normal} {Estilo.sublinhado}Resposta{Estilo.normal}: {resolucao} ''')

        case 2: # MULTIPLICAÇÃO
            equacao = input("\n{} - Digite a função a ser derivada: {}".format(Estilo.negrito, Estilo.normal)).strip().lower()

            try:
                equacao_derivada = Derivada(equacao)
                resolucao = equacao_derivada.multiplicacao("mult")
            except ValueError as erro:
                print(f"\n {Estilo.invertido}{erro}{Estilo.normal}")
            else:
                print(f'''    {Estilo.negrito}->{Estilo.normal} {Estilo.sublinhado}Resposta{Estilo.normal}: {resolucao} ''')

        case 3: # QUOCIENTE
            equacao = input("\n{} - Digite a função a ser derivada: {}".format(Estilo.negrito, Estilo.normal)).strip().lower()

            try:
                equacao_derivada = Derivada(equacao)
                resolucao = equacao_derivada.quociente("divi")
            except ValueError as erro:
                print(f"\n {Estilo.invertido}{erro}{Estilo.normal}")
            except ZeroDivisionError:
                print(f"\n{Estilo.invertido} ***Divisão por zero apresentada. Resultado impossível. {Estilo.normal}")
            else:
                print(f'''    {Estilo.negrito}->{Estilo.normal} {Estilo.sublinhado}Resposta{Estilo.normal}: {resolucao} ''')

        case 4: # SAIR
            print(f"\n{Estilo.invertido}***Finalizando sistema", end="", flush=True)
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            print(Estilo.normal)
            break

        case _: # ENTRADA INVÁLIDA
            os.system('cls')
            print("\n{}***Número inválido. Tente novamente {} \n".format(Estilo.invertido, Estilo.normal))
            continue
    
    # Verifica se o usuário quer continuar
    try:
        continuar = input("\n{} - Deseja continuar [S/N]? {}". format(Estilo.negrito, Estilo.normal)).upper()[0]
    except:
        continuar = 0

    if (continuar == "S"):
        os.system('cls')
        continue
    elif (continuar == "N"):
        print(f"\n{Estilo.invertido}***Finalizando sistema", end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print(Estilo.normal)
        break
    else: 
        os.system('cls')
        print("\n{}***Resposta inválida. Tente novamente. {}\n".format(Estilo.invertido, Estilo.normal))
        continue 
