import re

class Estilo:
    '''
    Agrupa a formatação dos textos
    
    Cada atributo da classe é um estilo diferente no estilo de "escape codes" (ANSI design), com um método que escreve uma linha divisória na tela.
    '''
    normal = "\033[m"
    negrito = "\033[1m"
    sublinhado = "\033[4m"
    invertido = "\033[7m"
    sublinhado_invertido = "\033[1;4;7m"

    @classmethod
    def escreva_linha(cls):
        print(f"{cls.negrito}", "--" * 30, f"{cls.normal}")

class Derivada:
    '''
    Representa a derivação de funções matemáticas.

    A classe recebe uma equação em formato de string, separando os termos entre si e dividindo-os monômios (termos separados) em uma tupla com coeficiente e expoente, sendo utilizados para os cálculos correspondetes, sendo a potêncição, soma e subtração, multiplicação e quociente.

    Atributos:
        _equacao_extensa (list[str]): Lista de termos separados entre si no formato de string correspondente a entrada do usuário, onde cada termo é um monômio a ser dividido em algo legível pelo programa (string -> int).

        monomios (list[tuple[int, int]]): Lista de monômios (composto por sinal, coeficiente, incógnita e expoente) no formato (coeficiente, expoente).
    
    Métodos:

    '''
    def __init__(self, equacao_extensa):
        self.monomios_originais = []
        self.monomios_derivados = []
        self.operadores = []
        self.equacao_extensa = equacao_extensa
        for i in range(len(self.equacao_extensa)):
            equacao = self.equacao_extensa[i]
            self.monomios_originais.append(self.separador_elementos(equacao)
)
        print("3. Monômios divididos: ", self.monomios_originais) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    @property # Getter
    def equacao_extensa(self):
        return self._equacao_extensa

    @equacao_extensa.setter # Setter
    def equacao_extensa(self, equacao):
        self._equacao_extensa = str(equacao).split()
        equacao_limpa = []
        print("1. Equação separada: ", self._equacao_extensa) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        sinal = "+" # Define o sinal positivo para a primeira iteração (se não for especificado)
        # Adiciona os operadores "/" e "*" em <self.operadores> e corrige o sinal em <equacao_extensa>
        for termo in self._equacao_extensa: 
            if (termo == "+"):
                sinal = "+"
            elif (termo == "-"):
                sinal = "-"
            elif (termo in ("*", "/")):
                self.operadores.append(termo)
            elif not re.fullmatch(r"-?\d+(?:\.\d+)?|-?\d*(?:\.\d+)?x(\^-?\d+)?", termo): # Ignora termos não calculáveis
                raise ValueError("***Algum valor incorreto foi encontrado. Verifique a equação e tente novamente.")
            else:
                # Adiciona o coeficiente 1 em caso de não haver coeficiente (oculto)
                if (termo[0] == "x"):
                    termo = f"1{termo}"
                # Adiciona o sinal correto a partir das condições anteriores
                if (sinal == "+"):
                    equacao_limpa.append(f"+{termo}")
                else:
                    equacao_limpa.append(f"-{termo}")

        print("2. Equação sem operadores: ", equacao_limpa) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        self._equacao_extensa = equacao_limpa # Atualiza o atributo com os termos (monômios) separados 

    def separador_elementos(self, equacao):
        try:
            if ("x" in equacao): 
                equacao_sep = list(map(int, equacao.split("x^"))) 
                coeficiente = equacao_sep[0]
                expoente = equacao_sep[1]
                return (coeficiente, expoente)
            else:
                return (0, 0)
        except:
            posicao_x = equacao.index("x") 
            try:
                coeficiente = float(equacao[:posicao_x])
                Derivada._arredondar(coeficiente)
            except:
                coeficiente = 1
            try:
                expoente = float(equacao[(posicao_x + 2):]) # Considera x^
                Derivada._arredondar(expoente)
            except:
                expoente = 1

            return (coeficiente, expoente)
    
    def potencia(self, operacao):
        print("4. Operadores especiais encontrados: ", self.operadores) # AAAAAAAAAAAAAAAAAAAAAAAAAA
        # Confere se a operação solicitada é a realidade 
        if (operacao == "pot_soma_sub") and any(op in ("*", "/") for op in self.operadores):
            raise ValueError("***Operador incorreto encontrado. O usuário escolheu operações não relacionadas à multiplicações e divisões, mas o operador \"*\" ou \"/\" surgiu.")
        elif (operacao == "mult") and not any(op in ("*") for op in self.operadores):
            raise ValueError("***Operador necessário não encontrado. O usuário escolheu operações relacionadas à multiplicações. Tente novamente.")
        elif (operacao == "divi") and not any(op in ("/") for op in self.operadores):
            raise ValueError("***Operador necessário não encontrado. O usuário escolheu operações relacionadas à divisão. Tente novamente.")

        monomios = self.monomios_originais.copy() # Utiliza uma cópia para não modificar os originais
        for item in range(len(monomios)):
            coeficiente, expoente = monomios[item] 
            coeficiente *= expoente
            if (coeficiente != 0):
                expoente -= 1
            else:
                expoente = 0
            monomios[item] = (coeficiente, expoente)
        self.monomios_derivados = monomios # Atribui monômios derivados pela regra da potência
        return self

    def multiplicacao(self):
        if (len(self.monomios_originais) > 2): # MODIFICAR MULTIPLIAÇÃO PARA ACEITAR TERMOS COM OUTRAS OPERAÇÕES 
            pass
        
        originais = self.monomios_originais
        derivados = self.potencia("mult").monomios_derivados

        lista_monomios = [
            Derivada._multiplica_monomios(derivados[0], originais[1]),
            Derivada._multiplica_monomios(originais[0], derivados[1])
        ]

        self.monomios_derivados = Derivada._soma_sub_monomios("+", lista_monomios[0], lista_monomios[1])

        return self

    def quociente(self):
        if (len(self.monomios_originais) > 2): # MODIFICAR MULTIPLIAÇÃO PARA ACEITAR TERMOS COM OUTRAS OPERAÇÕES 
            pass
        
        originais = self.monomios_originais
        derivados = self.potencia("divi").monomios_derivados

        lista_monomios = [
            Derivada._multiplica_monomios(derivados[0], originais[1]),
            Derivada._multiplica_monomios(originais[0], derivados[1])
        ]

        self.monomios_derivados = Derivada._soma_sub_monomios("-", lista_monomios[0], lista_monomios[1])

        (coeficiente_numerador, expoente_numerador) = self.monomios_derivados[0]
        (coeficiente_denominador, (expoente_denominador )) = self.monomios_originais[1]
        coeficiente_denominador **= 2
        expoente_denominador *= 2

        print("- Termos: ", coeficiente_numerador, expoente_numerador, coeficiente_denominador, expoente_denominador)

        coeficiente_final = coeficiente_numerador / coeficiente_denominador
        coeficiente_final = Derivada._arredondar(coeficiente_final)
        expoente_final = expoente_numerador - expoente_denominador

        print("- Termos finais: ", coeficiente_final, expoente_final)

        self.monomios_derivados = [(coeficiente_final, expoente_final)]

        return self

    @staticmethod 
    def _multiplica_monomios(termo_1, termo_2):
        (coeficiente_1, expoente_1), (coeficiente_2, expoente_2) = termo_1, termo_2
        return (coeficiente_1 * coeficiente_2, expoente_1 + expoente_2)

    @staticmethod
    def _soma_sub_monomios(operacao, termo_1, termo_2):
        (coeficiente_1, expoente_1), (coeficiente_2, expoente_2) = termo_1, termo_2
        if (expoente_1 == expoente_2):
            if (operacao == "+"):
                coeficiente_final = coeficiente_1 + coeficiente_2
            else:
                coeficiente_final = coeficiente_1 - coeficiente_2
            return [(coeficiente_final, expoente_1)] # Retorna uma lista com uma tupla da soma final
        else:
            return [termo_1, termo_2] # Retorna os monômios que não puderam ser somados

    @staticmethod
    def _arredondar(num: float):
        if (num.is_integer()):
            return int(num)
        else:
            return round(num, 1)

    # MODIFICAR: RETIRAR O 1 DO X, QUANDO O COEFICIENTE É OCULTO
    def __str__(self):
        resposta = []
        for (coeficiente, expoente) in self.monomios_derivados:
            if (coeficiente < 0):
                sinal = "-"
            else:
                sinal = "+"

            # Se houver coeficiente oculto (1), não escreve. Se não houver, torna-o absolto para eviar conflito no sinal escrito pos string
            if (coeficiente == 1) and (expoente != 0):
                coeficiente = ""
            else:    
                coeficiente = abs(coeficiente)

            if (expoente == 0):
                termo = f"{coeficiente}"
            elif (expoente == 1):
                termo = f"{coeficiente}x"
            else:
                termo = f"{coeficiente}x^{expoente}"

            resposta.append(f"{sinal} {termo}")

        return " ".join(resposta)

# 1 - Menu de opções e continuidade;
# 2 - Método separador: Recebe uma equacao e divide ela em monomios
# 3 - Métodos para cada opereção: Potência, Soma/Sub, Multiplicação e Quociente.