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
        self.equacao_extensa = equacao_extensa
        self.monomios = []
        for i in range(len(self.equacao_extensa)):
            equacao = self.equacao_extensa[i]
            self.monomios.append(self.separador(equacao)
)
        print(self.monomios) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

    @property # Getter
    def equacao_extensa(self):
        return self._equacao_extensa

    @equacao_extensa.setter # Setter
    def equacao_extensa(self, equacao):
        self._equacao_extensa = str(equacao).split()
        equacao_limpa = []
        print(self._equacao_extensa) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        sinal = "+" # Define o sinal positivo caso o primeiro termo não possua sinalização
        # Verifica o sinal, corrige ele no termo correspondente e adiciona à lista equacao_limpa
        for termo in self._equacao_extensa: 
            if (termo == "+"):
                sinal = "+"
            elif (termo == "-"):
                sinal = "-"
            else:
                # Adiciona o coeficiente 1 em caso de não haver coeficiente (oculto)
                if (termo[0] == "x"):
                    termo = f"1{termo}"
                # Adiciona o sinal correto a partir das condições anteriores
                if (sinal == "+"):
                    equacao_limpa.append(f"+{termo}")
                else:
                    equacao_limpa.append(f"-{termo}")

        print(equacao_limpa) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        self._equacao_extensa = equacao_limpa # Atualiza o atributo com os termos (monômios) separados 

    def separador(self, equacao):
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
                coeficiente = int(equacao[:posicao_x])
            except:
                coeficiente = 1
            try:
                expoente = int(equacao[(posicao_x + 2):]) # Considera x^
            except:
                expoente = 1

            return (coeficiente, expoente)
    
    @staticmethod
    def potencia(lista_monomios):
        for item in range(len(lista_monomios)):
            coeficiente, expoente = lista_monomios[item] 
            coeficiente *= expoente
            if (coeficiente != 0):
                expoente -= 1
            else:
                expoente = 0
            lista_monomios[item] = (coeficiente, expoente)
        return lista_monomios

    # REGISTRO - FUNÇÃO ANTIGA
    # def potencia(self):
    #     for i in range(len(self.monomios)):
    #         coeficiente, expoente = self.monomios[i] 
    #         coeficiente *= expoente
    #         if (coeficiente != 0):
    #             expoente -= 1
    #         else:
    #             expoente = 0
    #         self.monomios[i] = (coeficiente, expoente)
    #     return self.monomios

    def multiplicacao(self):
        print("-" * 27) # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        monomios_originais = self.monomios.copy()
        monomios_derivados = Derivada.potencia(self.monomios.copy())

        lista_monomios = [
            Derivada._multiplica_monomios(monomios_derivados[0], monomios_originais[1]),
            Derivada._multiplica_monomios(monomios_derivados[1], monomios_originais[0])
        ]

        # coeficiente = monomios_derivados[0] * monomios_originais[1]
        # expoente = monomios_derivados[0] + monomios_originais[1]
        # lista_monomios.append((coeficiente, expoente))
        
        # coeficiente = monomios_originais[0] * monomios_derivados[1]
        # expoente = monomios_originais[0] + monomios_derivados[1]
        # lista_monomios.append((coeficiente, expoente))

        print(lista_monomios)

    @staticmethod # TESTAR MAISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    def _multiplica_monomios(termo_1, termo_2):
        (coeficiente_1, expoente_1), (coeficiente_2, expoente_2) = termo_1, termo_2
        return (coeficiente_1 * coeficiente_2, expoente_1 + expoente_2)

    def quociente(self):
        pass

    def __str__(self):
        resposta = []
        for (coeficiente, expoente) in self.monomios:
            if (coeficiente < 0):
                sinal = "-"
            else:
                sinal = "+"

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