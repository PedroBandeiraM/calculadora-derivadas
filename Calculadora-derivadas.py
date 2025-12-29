# Calculadora de derivadas: Abre um menu de operações (1 à 5) relacionadas à derivação de funções matemáticas.

import os, time # OS -> Requisições de sistema ("clean") ; TIME -> Funções de tempo ("sleep")

# Declaração/atribuição de variáveis
resp = []
estilo_normal = "\033[m"
estilo_negrito = "\033[1m"
estilo_sublinhado = "\033[4m"
estilo_invertido = "\033[7m"

# Área de funções =========================================================================================

def potencia(equacao):    
    equacao = str(equacao)
    try:
        if ("x" in equacao):
            resp = list(map(int, equacao.split("x^")))
            multiplicando = resp[0]
            expoente = resp[-1]
        else:
            return 0
    except:
        posicao_x = equacao.index("x")
        try:
            multiplicando = int(equacao[:posicao_x])
        except:
            multiplicando = 1
        try:
            expoente = int(equacao[(posicao_x + 2):])
        except:
            expoente = 1

    multiplicando = multiplicando*expoente
    expoente -= 1

    if (expoente == 0):
        return multiplicando
    elif (expoente == 1):
        return str("{}x".format(multiplicando))
    else:
        return str("{}x^{}".format(multiplicando, expoente))

def soma_sub(sinal, num1, num2): 
    resp = []
    resp.append(potencia(num1))
    resp.append(potencia(num2))

    return str(f"{resp[0]} {sinal} {resp[-1]}")

def multiplicacao(num1, num2):
    nums = {}
    resp = [potencia(num1), num2, num1, potencia(num2)]

    # SEPARADOR
    for item in range(len(resp)):
        num = str(resp[item])
        resp_final = {}
        cont = 0

        if ("x" in num):
            posicao_x = num.index("x")
            try:
                multiplicando = int(num[:posicao_x])
            except:
                multiplicando = 1
            try:
                expoente = int(num[(posicao_x + 2):])
            except:
                expoente = 1
        else:
            multiplicando = int(num)
            expoente = 0    
        
        nums[f"num[{item}]"] = (multiplicando, expoente)

    for i in range(0, 4, 2):
        multiplicando = (nums[f"num[{i}]"][0]) * (nums[f"num[{i+1}]"][0])
        expoente = (nums[f"num[{i}]"][1]) + (nums[f"num[{i+1}]"][1])
        resp_final[f"num[{cont}]"] = (multiplicando, expoente)
        cont += 1

    if (resp_final["num[0]"][1] == resp_final["num[1]"][1]):
        multiplicando = (resp_final["num[0]"][0]) + (resp_final["num[1]"][0])
        expoente = (resp_final["num[0]"][1])
        return [multiplicando, expoente]
    else:
        return (resp_final)

# def quociente():
#     print(f"\n{estilo_negrito}", "--" * 27, " {} \n".format(estilo_normal))
    
# def cadeia():
#     print(f"\n{estilo_negrito}", "--" * 27, " {} \n".format(estilo_normal))

# Área de execução ========================================================================================

while True:
    print(f"\n{"{} Calculadora de derivadas {}":=^60}".format(estilo_negrito, estilo_normal)) # Título

    # Opções de operações (1 à 5)
    try:
        operacao = int(input('''
    - Escolha a operação que deseja calcular:                      
        {}[1]{} Potenciação (^)
        {}[2]{} Soma / subtração (+ | -)
        {}[3]{} Multiplicação (*)
        {}[4]{} Quociente (/)
        {}[5]{} Cadeia (composição)
        -> '''.format(estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal)))
    except:
        operacao = 0 # Caso seja digitado algo que não seja possível converter para número

    # Verifica se a opção escolhida é válida, direcionando se sim, e, senão, retornando erro
    match (operacao):
        case 1: # POTENCIAÇÃO
            print(f"\n{estilo_negrito}", "--" * 27, " {} \n".format(estilo_normal))
            equacao = input("{} - Digite a função a ser derivada: {}".format(estilo_negrito, estilo_normal))
            pot = f"{estilo_negrito}{potencia(equacao)}{estilo_normal}"

            print(" •{} A resposta é: {}{}".format(estilo_sublinhado, pot, estilo_normal))

        case 2: # SOMA | SUBTRAÇÃO
            print(f"\n{estilo_negrito}", "--" * 27, " {} \n".format(estilo_normal))

            sinal = str(input("{} - Escolha a operação [+/-]: {}".format(estilo_negrito, estilo_normal)))
            num1 = input("{} - Digite o 1º valor: {}".format(estilo_negrito, estilo_normal))
            num2 = input("{} - Digite o 2º valor: {}".format(estilo_negrito, estilo_normal))
            som_sub = soma_sub(sinal, num1, num2)

            print(" •{} A resposta é: {}{}".format(estilo_sublinhado, som_sub, estilo_normal))

        case 3: # MULTIPLICAÇÃO
            print(f"\n{estilo_negrito}", "--" * 27, " {} \n".format(estilo_normal))

            num1 = input("{} - Digite o 1º número: {}".format(estilo_negrito, estilo_normal))
            num2 = input("{} - Digite o 2º número: {}".format(estilo_negrito, estilo_normal))
            mult = multiplicacao(num1, num2)

            if (isinstance(mult, list)):
                mult = f"{mult[0]}x^{mult[-1]}"
            elif (isinstance(mult, dict)):
                mult = f"{mult["num[0]"][0]}x^{mult["num[0]"][1]} . {mult["num[1]"][0]}x^{mult["num[1]"][1]}"

            print(" •{} A resposta é: {}{}".format(estilo_sublinhado, mult, estilo_normal))

        # case 4: # QUOCIENTE
        #     print(f"\n{estilo_negrito}", "--" * 27, " {} \n".format(estilo_normal))

        # case 5: # CADEIA
        #     print(f"\n{estilo_negrito}", "--" * 27, " {} \n".format(estilo_normal))

        case _: # ENTRADA INVÁLIDA
            os.system('cls')
            print("\n {}***Número inválido. Tente novamente {} \n".format(estilo_invertido, estilo_normal))
            continue

# Área de verificação de continuidade =================================================================    
    
    # Verifica se o usuário quer continuar
    continuar = input("\n ->{} Deseja continuar [S/N]? {}". format(estilo_negrito, estilo_normal)).upper()[0]

    if (continuar == "S"):
        os.system('cls')
        continue
    elif (continuar == "N"):
        print("{}***Finalizando sistema".format(estilo_invertido), end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print(estilo_normal)
        break
    else: 
        os.system('cls')
        print("\n {}***Tentativa inválida. Tente novamente {}\n".format(estilo_invertido, estilo_normal))
        continue 
