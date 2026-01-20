import os, time
from POO_functions_Calculadora_derivadas import Estilo, Derivada

resp = []

while True:
    print(f"\n{Estilo.negrito}{" CALCULADORA DE DERIVADAS ":=^60}{Estilo.normal}") # Título

    # Opções de operações (1 à 5) para escolher
    try:
        operacao = int(input('''
{} - Escolha a operação que deseja calcular: {}                     
    {}[1]{} Potenciação, soma e subtração ( ^ | + | - )
    {}[2]{} Multiplicação (*)
    {}[3]{} Quociente (/)
    {}[4]{} Cadeia (composição)
    {}-> {}'''.format(Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal)))
    except:
        operacao = 0 # Caso seja digitado algo que não seja possível converter para número

    # Verifica se a opção escolhida é válida, direcionando ou retornando erro
    match (operacao):
        case 1: # POTENCIAÇÃO, SOMA E SUBTRAÇÃO
            equacao = input("{} - Digite a função a ser derivada: {}".format(Estilo.negrito, Estilo.normal)).strip().lower()

            equacao_derivada = Derivada(equacao)
            Derivada.potencia(equacao_derivada.monomios)
            print(equacao_derivada)

        case 2: # MULTIPLICAÇÃO
            equacao = input("{} - Digite a função a ser derivada: {}".format(Estilo.negrito, Estilo.normal)).strip().lower()

            equacao_derivada = Derivada(equacao)
            equacao_derivada.multiplicacao()
            # print(equacao_derivada)

        case 3: # QUOCIENTE
            pass

        case _: # ENTRADA INVÁLIDA
            os.system('cls')
            print("\n{}***Número inválido. Tente novamente {} \n".format(Estilo.invertido, Estilo.normal))
            continue

# Área de verificação de continuidade =======================================================================================================   
    
    # Verifica se o usuário quer continuar
    continuar = input("\n{} -> Deseja continuar [S/N]? {}". format(Estilo.negrito, Estilo.normal)).upper()[0]

    if (continuar == "S"):
        os.system('cls')
        continue
    elif (continuar == "N"):
        print("{}\n***Finalizando sistema".format(Estilo.invertido), end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print(Estilo.normal)
        break
    else: 
        os.system('cls')
        print("\n{}***Resposta inválida. Tente novamente. {}\n".format(Estilo.invertido, Estilo.normal))
        continue 
