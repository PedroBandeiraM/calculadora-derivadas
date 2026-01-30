import re
from typing import Self

class Estilo:
    '''
    Agrupa a formatação dos textos
    
    Cada atributo de classe é um estilo diferente no estilo de "escape codes" (ANSI design).
    '''
    normal = "\033[m"
    negrito = "\033[1m"
    sublinhado = "\033[4m"
    invertido = "\033[7m"

class Derivada:
    '''
    Representa a derivação de funções matemáticas.

    A classe recebe uma equação em formato de string, separando os termos entre si e dividindo-os monômios (termos separados) em uma tupla com coeficiente e expoente, sendo utilizados para os cálculos correspondetes, sendo a potêncição, soma e subtração, multiplicação e quociente.

    Atributos:
        monomios_originais (list[tuple[int | float, int | float]]): 
            Lista de monômios em formato de tupla, onde o primeiro item é o coefiente original e o segundo é o expoente original do mônomio em questão.
    
        monomios_derivados (list[tuple[int | float, int | float]]): 
            Lista de monômios em formato de tupla, onde o primeiro item é o coefiente derivado e o segundo é o expoente derivado do mônomio em questão.

        operadoes (list[str]): 
            Lista que armazena os operadores (+, -, * e /) para verificar as operações.

        equacao_extensa (list[str]): 
            Lista de monômios sem coeficiente e expoente separados, onde estes termos em formato de string e com operadores unários alocados corretamente de acordo com o input do usuário.

    Métodos:
        separador_elementos():
            Recebe a equação_extensa e separa cada termo em um monômio real, retornando uma tupla com o formato (coeficiente e expoente)

        potencia():
            Recebe um monômio já separado por <separador_elementos> e deriva, onde o coeficiente é multiplicado pelo expoente e o expoente é subtraído por 1, adicionando uma tupla no mesmo formato com os novos valores em <monomios_derivados> e retornando self.

        multiplicao():
            Deriva e aplica as operações aos termos respectivamente (f'g + fg'), armazena a multiplicação entre as funções (f e g) em <lista_monomios> e atualiza <monomios_derivados> pela subtração dos termos multiplicados, retornando self.

        quociente():
            Deriva e aplica as operações aos termos respectivamente ((f'g - fg')/g^2), armazena a multiplicação entre as funções (f e g) em <lista_monomios>, cria <numerador> com a subtração dos termos multiplicados, cria <denominador> com (g^2) e atualiza <monomios_derivados> com a divisão entre numerador e denominador, retornando self.

        _multiplica_monomios():
            Recebe dois monômios e retorna uma tupla com produto entre os termos.

        _soma_sub_monomios():
            Recebe dois monômios e retorna uma lista com a soma/subtração entre os termos (se for possível).
        
        _arredondar():
            Recebe um número e converte para inteiro se sua parte decimal for 0, retornando o valor.
    '''
    def __init__(self, equacao_extensa: str):
        self.monomios_originais: list[tuple] = []
        self.monomios_derivados: list[tuple] = []
        self.operadores: list[str] = []
        self.equacao_extensa = equacao_extensa
        for item in range(len(self.equacao_extensa)):
            monomio = self.equacao_extensa[item]
            self.monomios_originais.append(self.separador_elementos(monomio))

    @property
    def equacao_extensa(self):
        return self._equacao_extensa

    @equacao_extensa.setter
    def equacao_extensa(self, equacao: str):
        equacao_limpa: list[str] = []
        sinal: str = "+" # Define o sinal positivo (padrão inicial)
        self._equacao_extensa = equacao.split()

        # Adiciona os operadores "/" e "*" em <self.operadores> e corrige o sinal em <equacao_extensa>
        for termo in self._equacao_extensa: 
            if (termo == "+"):
                sinal = "+"
            elif (termo == "-"):
                sinal = "-"
            elif (termo in ("*", "/")):
                self.operadores.append(termo)
                sinal = "+"
            elif not re.fullmatch(r"-?\d+(?:\.\d+)?|-?\d*(?:\.\d+)?x(?:\^-?\d+)?", termo): # Retorna erro ao encontrar caracteres inválidos
                raise ValueError("*** Algum valor inválido foi encontrado. Verifique a equação e tente novamente.")
            else:
                # Adiciona o coeficiente 1 caso não haja coeficiente (oculto)
                if (termo[0] == "x"):
                    termo = f"1{termo}"
                # Adiciona o sinal de forma legível
                if (sinal == "+"):
                    equacao_limpa.append(f"+{termo}")
                else:
                    equacao_limpa.append(f"-{termo}")

        self._equacao_extensa = equacao_limpa 

    def separador_elementos(self, equacao: str) -> tuple:
        try:
            # Converte coeficiente e expoente em inteiros
            if ("x" in equacao): 
                equacao_sep = list(map(int, equacao.split("x^"))) 
                coeficiente = equacao_sep[0]
                expoente = equacao_sep[1]
                return (coeficiente, expoente)
            else:
                return (0, 0) # Se não há variável (x), é uma constante, resultando em 0
        except:
            # Converte coeficiente ou expoente em inteiro
            posicao_x = equacao.index("x") 
            try:
                coeficiente = float(equacao[:posicao_x])
                coeficiente = Derivada._arredondar(coeficiente)
            except:
                coeficiente = 1
            try:
                expoente = float(equacao[(posicao_x + 2):]) # Considera x^
                expoente = Derivada._arredondar(expoente)
            except:
                expoente = 1

            return (coeficiente, expoente)
    
    def potencia(self) -> Self:
        monomios = self.monomios_originais.copy()
        for item in range(len(monomios)):
            coeficiente, expoente = monomios[item] 
            coeficiente *= expoente
            if (coeficiente != 0):
                expoente -= 1
            else:
                expoente = 0
            resultado = (coeficiente, expoente)
            self.monomios_derivados.append(resultado)
        return self

    def multiplicacao(self, operacao) -> Self:
        # Verifica se a operação solicitada corresponde ao operador presente
        if (operacao == "mult") and ("*" not in self.operadores):
            raise ValueError("***Operador necessário não encontrado. O usuário escolheu operações relacionadas à multiplicações. Tente novamente.")
    
        originais = self.monomios_originais
        derivados = self.potencia().monomios_derivados

        # Representa: f'g e fg'
        lista_monomios = [
            Derivada._multiplica_monomios(derivados[0], originais[1]),
            Derivada._multiplica_monomios(originais[0], derivados[1])
        ]

        self.monomios_derivados = Derivada._soma_sub_monomios("+", lista_monomios[0], lista_monomios[1])

        return self

    def quociente(self, operacao) -> Self:
        # Verifica se a operação solicitada corresponde ao operador presente
        if (operacao == "divi") and ("/" not in self.operadores):
            raise ValueError("*** Operador necessário não encontrado. O usuário escolheu operações relacionadas à divisão. Tente novamente.")
        
        originais = self.monomios_originais
        derivados = self.potencia().monomios_derivados

        # Representa f'g e fg'
        lista_monomios = [
            Derivada._multiplica_monomios(derivados[0], originais[1]),
            Derivada._multiplica_monomios(originais[0], derivados[1])
        ]

        numerador = Derivada._soma_sub_monomios("-", lista_monomios[0], lista_monomios[1])[0]
        denominador = self.monomios_originais[1]

        (coeficiente_numerador, expoente_numerador) = numerador
        (coeficiente_denominador, expoente_denominador) = denominador

        coeficiente_denominador **= 2
        expoente_denominador *= 2

        coeficiente_final = Derivada._arredondar(coeficiente_numerador / coeficiente_denominador)
        expoente_final = expoente_numerador - expoente_denominador

        self.monomios_derivados = [(coeficiente_final, expoente_final)]

        return self

    @staticmethod 
    def _multiplica_monomios(monomio_1: tuple, monomio_2: tuple) -> tuple:
        (coeficiente_1, expoente_1), (coeficiente_2, expoente_2) = monomio_1, monomio_2
        return (coeficiente_1 * coeficiente_2, expoente_1 + expoente_2)

    @staticmethod
    def _soma_sub_monomios(operacao: str, monomio_1: tuple, monomio_2: tuple) -> list[tuple]:
        (coeficiente_1, expoente_1), (coeficiente_2, expoente_2) = monomio_1, monomio_2
        # Verifica se é possível somar/subtrair (expoentes devem ser iguais)
        if (expoente_1 == expoente_2):
            if (operacao == "+"):
                coeficiente_final = coeficiente_1 + coeficiente_2
            else:
                coeficiente_final = coeficiente_1 - coeficiente_2
            return [(coeficiente_final, expoente_1)] # Retorna a soma
        # Se não for possível, então a equação apresentou uma quantidade não permitida de monômios
        else:
            raise ValueError("***Este programa não aceita mais de 2 monômios em operações de multilplicação e quociente. Tente outra equação.")

    @staticmethod
    def _arredondar(num: float) -> int | float:
        if (num.is_integer()):
            return int(num)
        else:
            return round(num, 1)

    def __str__(self) -> str:
        resposta = []
        for (coeficiente, expoente) in self.monomios_derivados:
            if (coeficiente >= 0):
                sinal = "+"
            else:
                sinal = "-"

            # Oculta o coeficiente 1 ou retira seu sinal para seguir com a formatação dos sinais 
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
