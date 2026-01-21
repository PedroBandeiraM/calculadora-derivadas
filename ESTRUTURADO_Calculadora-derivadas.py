# Calculadora de derivadas: Abre um menu de operações (1 à 5) relacionadas à derivação de funções matemáticas.

import os, time # OS -> Requisições de sistema ("clean") ; TIME -> Funções de tempo ("sleep")

# Declaração/atribuição de variáveis
resp = []
estilo_normal = "\033[m"
estilo_negrito = "\033[1m"
estilo_sublinhado = "\033[4m"
estilo_invertido = "\033[7m"
estilo_sublinhado_invertido = "\033[1;4;7m"

# Área de funções =========================================================================================

def escreva_linha():
        print(f"{estilo_negrito}", "--" * 30, f"{estilo_normal}")

def potencia(num):    
    num = str(num) #Variável que armazena o monômio a ser derivado

    #Separa os elementos (coeficiente e expoente) do monômio
    try:
        if ("x" in num):
            equacao = list(map(int, num.split("x^")))
            multiplicando = equacao[0]
            expoente = equacao[1]
        else:
            return 0
    except:
        posicao_x = num.index("x")
        try:
            multiplicando = int(num[:posicao_x])
        except:
            multiplicando = 1
        try:
            expoente = int(num[(posicao_x + 2):])
        except:
            expoente = 1

    # Processo de derivação sobre a regra da potência
    multiplicando *= expoente
    expoente -= 1

    # Simplifica a visualização dos resultados (não altera os valores matemáticos)
    if (expoente == 0):
        return multiplicando
    elif (expoente == 1):
        return str("{}x".format(multiplicando))
    else:
        return str("{}x^{}".format(multiplicando, expoente))

def soma_sub(sinal, num1, num2): 
    nums = [] # Lista que armazena os monômios derivados
    nums.append(potencia(num1))
    nums.append(potencia(num2))

    return str(f"{nums[0]} {sinal} {nums[-1]}")

def multiplicacao(num1, num2):
    nums = [potencia(num1), num2, num1, potencia(num2)] # Lista que organiza a ordem dos monômios e a derivação        (f' * g + f * g')
    nums_sep = {} # Dicionário que guarda os elementos (coeficiente e expoente) de cada monômio separado
    resp = {} # Dicionário que armazena o resultado final
    cont = 0 # Contador genérico

    # Separa os coeficientes (números que multiplicam as variáveis) e os expoentes da incógnita
    for item in range(len(nums)):
        num = str(nums[item]) # Monômio (1 por vez)

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
        
        nums_sep[f"num[{item}]"] = (multiplicando, expoente) # Adiciona os elementos separados como tupla dentro do dicionário

    # Realiza a multiplicação entre os monômios (multiplicando os coeficientes e somando os expoentes)
    for i in range(0, 4, 2):
        multiplicando = (nums_sep[f"num[{i}]"][0]) * (nums_sep[f"num[{i+1}]"][0])
        expoente = (nums_sep[f"num[{i}]"][1]) + (nums_sep[f"num[{i+1}]"][1])
        resp[f"num[{cont}]"] = (multiplicando, expoente)
        cont += 1

    # IDEIA DE MELHORIA: MELHORAR A SIMPLIFICAÇÃO EM CASOS DE X^0 E X^1

    #Verifica se é possível somar os monômios (expoentes iguais), retornando 2 possíveis casos (com soma e sem soma)
    if (resp["num[0]"][1] == resp["num[1]"][1]):
        multiplicando = (resp["num[0]"][0]) + (resp["num[1]"][0])
        expoente = (resp["num[0]"][1])
        return [multiplicando, expoente]
    else:
        return (resp)

def quociente(num1, num2):
    nums = [potencia(num1), num2, num1, potencia(num2), num2] # Lista que organiza a ordem dos monômios e a derivação  (f' * g - f * g') / g² 
    nums_sep = {} # Dicionário que guarda os elementos (coeficiente e expoente) de cada monômio separado
    numerador = {} # Dicionário que armazena o resultado final
    cont = 0 # Contador genérico

    # Separa os coeficientes (números que multiplicam as variáveis) e os expoentes da incógnita (X)
    for item in range(len(nums)):
        num = str(nums[item]) # Monômio (1 por vez)

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
        
        nums_sep[f"num[{item}]"] = (multiplicando, expoente) # Adiciona os elementos separados como tupla dentro do dicionário
   
    # Realiza a multiplicação entre os monômios do numerador (multiplicando os coeficientes e somando os expoentes)
    for i in range(0, 4, 2):
        multiplicando = (nums_sep[f"num[{i}]"][0]) * (nums_sep[f"num[{i+1}]"][0])
        expoente = (nums_sep[f"num[{i}]"][1]) + (nums_sep[f"num[{i+1}]"][1])
        if (multiplicando == 0):
            expoente = 0
        numerador[f"num[{cont}]"] = (multiplicando, expoente) # Representa os monômios presentes no numerador
        cont += 1

    # Verifica se é possível subtrair os monômios do numerador (expoentes iguais), retornando 2 possíveis casos (com subtração e sem subtração)
    if (numerador["num[0]"][1] == numerador["num[1]"][1]):
        multiplicando = (numerador["num[0]"][0]) - (numerador["num[1]"][0])
        expoente = (numerador["num[0]"][1])
        numerador = [multiplicando, expoente, "COM SUB"]
    else:
        numerador = (numerador, "SEM SUB")
    
    # Calcula o denominador
    if (nums_sep['num[4]'][1] == 0):
        denominador = (pow(nums_sep['num[4]'][0], 2))
    else:
        denominador = (pow(nums_sep['num[4]'][0], 2), (nums_sep['num[4]'][1] * 2))

    # Ideia: Fazer a simplificação do quociente, subtraindo expoentes e dividindo coeficientes
    # if ("COM SUB" in numerador) and (denominador[0] != 0):
    #     numerador[1] = numerador[1] - denominador[1]
    #     denominador[1] = 0

    # Simplifica a visualização do resultado: Numerador
    if ("COM SUB" in numerador):
        if (numerador[1] != 0):
            numerador = f"{numerador[0]}x^{numerador[1]}"
        else:
            numerador = f"{numerador[0]}"
    elif ("SEM SUB" in numerador):
        numerador = f"({numerador[0]["num[0]"][0]}x^{numerador[0]["num[0]"][1]}) - ({numerador[0]["num[1]"][0]}x^{numerador[0]["num[1]"][1]})"

    # Simplifica a visualização do resultado: Denominador
    if (isinstance(denominador, int)):
        denominador = f"{denominador}"
    else:    
        denominador = f"{denominador[0]}x^{denominador[1]}"

    return (numerador, denominador)

# def cadeia():
#     escreva_linha()

# Área de execução ========================================================================================

while True:
    print(f"\n{estilo_negrito}{" CALCULADORA DE DERIVADAS ":=^60}{estilo_normal}") # Título

    # Opções de operações (1 à 5) para escolher
    try:
        operacao = int(input('''
{} - Escolha a operação que deseja calcular: {}                     
    {}[1]{} Potenciação (^)
    {}[2]{} Soma / subtração (+ | -)
    {}[3]{} Multiplicação (*)
    {}[4]{} Quociente (/)
    {}[5]{} Cadeia (composição)
    {}-> {}'''.format(estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal, estilo_negrito, estilo_normal)))
    except:
        operacao = 0 # Caso seja digitado algo que não seja possível converter para número

    # Verifica se a opção escolhida é válida, direcionando ou retornando erro
    match (operacao):
        case 1: # POTENCIAÇÃO
            escreva_linha()

            equacao = input("{} - Digite a função a ser derivada: {}".format(estilo_negrito, estilo_normal))
            pot = f"{estilo_negrito}{potencia(equacao)}{estilo_normal}" 

            print(f"\n •{estilo_sublinhado} A resposta é:{estilo_normal} {estilo_invertido} {pot} {estilo_normal}")

        case 2: # SOMA e SUBTRAÇÃO
            escreva_linha()

            sinal = str(input("{} - Escolha a operação [+/-]: {}".format(estilo_negrito, estilo_normal)))
            num1 = input("{} - Digite o 1º valor: {}".format(estilo_negrito, estilo_normal))
            num2 = input("{} - Digite o 2º valor: {}".format(estilo_negrito, estilo_normal))
            som_sub = soma_sub(sinal, num1, num2)

            print(f" •{estilo_sublinhado} A resposta é:{estilo_normal} {estilo_invertido} {som_sub} {estilo_normal}")

        case 3: # MULTIPLICAÇÃO
            escreva_linha()

            num1 = input("{} - Digite o 1º número: {}".format(estilo_negrito, estilo_normal))
            num2 = input("{} - Digite o 2º número: {}".format(estilo_negrito, estilo_normal))
            mult = multiplicacao(num1, num2)

            # Escreve o resultado na tela de acordo com a possibilidade de somar u não os monômios multiplicados
            if (isinstance(mult, list)): 
                mult = f"{mult[0]}x^{mult[-1]}"
            elif (isinstance(mult, dict)):
                mult = f"{mult["num[0]"][0]}x^{mult["num[0]"][1]} . {mult["num[1]"][0]}x^{mult["num[1]"][1]}"

            print(f" •{estilo_sublinhado} A resposta é:{estilo_normal} {estilo_invertido} {mult} {estilo_normal}")

        case 4: # QUOCIENTE
            escreva_linha()

            num1 = input("{} - Digite o 1º número: {}".format(estilo_negrito, estilo_normal))
            num2 = input("{} - Digite o 2º número: {}".format(estilo_negrito, estilo_normal))
            divi = quociente(num1, num2)
            tamanho_espaco = len(divi[0])
            # f" •{estilo_sublinhado} A resposta é:{estilo_normal} {estilo_invertido} {som_sub} {estilo_normal}"
            print(f"\n {estilo_sublinhado}• A resposta é: {estilo_normal} "
                  f"{estilo_sublinhado} {divi[0]:^{tamanho_espaco}} {estilo_normal}"
                  f"\n {"":^17} {divi[1]:^{tamanho_espaco}}")
            
        # case 5: # CADEIA
        #     escreva_linha()

        case _: # ENTRADA INVÁLIDA
            os.system('cls')
            print("\n{}***Número inválido. Tente novamente {} \n".format(estilo_invertido, estilo_normal))
            continue

# Área de verificação de continuidade =================================================================    
    
    # Verifica se o usuário quer continuar
    continuar = input("\n{} -> Deseja continuar [S/N]? {}". format(estilo_negrito, estilo_normal)).upper()[0]

    if (continuar == "S"):
        os.system('cls')
        continue
    elif (continuar == "N"):
        print("{}\n***Finalizando sistema".format(estilo_invertido), end="", flush=True)
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print(estilo_normal)
        break
    else: 
        os.system('cls')
        print("\n{}***Resposta inválida. Tente novamente. {}\n".format(estilo_invertido, estilo_normal))
        continue 
