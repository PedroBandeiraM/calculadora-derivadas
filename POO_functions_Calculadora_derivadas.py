class Estilo:
    normal = "\033[m"
    negrito = "\033[1m"
    sublinhado = "\033[4m"
    invertido = "\033[7m"
    sublinhado_invertido = "\033[1;4;7m"

    @classmethod
    def escreva_linha(cls):
        print(f"{cls.negrito}", "--" * 30, f"{cls.normal}")

class Derivada:
    def __init__(self, equacao_extensa):
        self.monomios = []
        self.equacao_extensa = equacao_extensa
        for i in range(len(self.equacao_extensa)):
            self.equacao = self.equacao_extensa[i]
            self.monomios.append(self.separador(self.equacao)
)
        del self.equacao
        print(self.monomios)

    @property
    def equacao_extensa(self):
        return self._equacao_extensa

    @equacao_extensa.setter
    def equacao_extensa(self, equacao):
        self._equacao_extensa = str(equacao).split()
        equacao_limpa = []

        for termo in self._equacao_extensa:
            if (termo not in ("+", "-", "*", "/")):
                equacao_limpa.append(termo)

        self._equacao_extensa = equacao_limpa

    def separador(self, equacao):
        try:
            if ("x" in equacao): # TORNAR MAIS FLEXÍVEL -> QUALQUER LETRA
                equacao_sep = list(map(int, equacao.split("x^"))) # TORNAR MAIS FLEXÍVEL -> QUALQUER LETRA
                multiplicando = equacao_sep[0]
                expoente = equacao_sep[1]
                return (multiplicando, expoente)
            else:
                return (0, 0)
        except:
            posicao_x = equacao.index("x") # TORNAR MAIS FLEXÍVEL -> QUALQUER LETRA
            try:
                multiplicando = int(equacao[:posicao_x])
            except:
                multiplicando = 1
            try:
                expoente = int(equacao[(posicao_x + 2):])
            except:
                expoente = 1

            return (multiplicando, expoente)
    
    def potencia(self, monomio):
        

    def soma_subtracao(self, monomios):
        pass

# 1 - Menu de opções e continuidade;
# 2 - Método separador: Recebe uma equacao e divide ela em monomios
# 3 - Métodos para cada opereção: Potência, Soma/Sub, Multiplicação e Quociente.