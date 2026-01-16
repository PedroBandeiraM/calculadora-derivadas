import os, time
from POO_functions_Calculadora_derivadas import *

resp = []

while True:
    print(f"\n{Estilo.negrito}{" CALCULADORA DE DERIVADAS ":=^60}{Estilo.normal}") # Título

    # Opções de operações (1 à 5) para escolher
    try:
        operacao = int(input('''
{} - Escolha a operação que deseja calcular: {}                     
    {}[1]{} Potenciação (^)
    {}[2]{} Soma / subtração (+ | -)
    {}[3]{} Multiplicação (*)
    {}[4]{} Quociente (/)
    {}[5]{} Cadeia (composição)
    {}-> {}'''.format(Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal, Estilo.negrito, Estilo.normal)))
    except:
        operacao = 0 # Caso seja digitado algo que não seja possível converter para número

    # Verifica se a opção escolhida é válida, direcionando ou retornando erro
    match (operacao):
        case 1: # POTENCIAÇÃO
            equacao = input("{} - Digite a função a ser derivada: {}".format(Estilo.negrito, Estilo.normal))

            equacao_derivada = Derivada(equacao)
            # equacao_derivada.potencia()

        case 2: # SOMA e SUBTRAÇÃO
            pass

        case 3: # MULTIPLICAÇÃO
            pass

        case 4: # QUOCIENTE
            pass

        case _: # ENTRADA INVÁLIDA
            os.system('cls')
            print("\n{}***Número inválido. Tente novamente {} \n".format(Estilo.invertido, Estilo.normal))
            continue

# Área de verificação de continuidade =================================================================    
    
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
