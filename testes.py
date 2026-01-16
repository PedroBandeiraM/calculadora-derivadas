# equacao = "3x^2 + x - 2x"

# print(equacao)
# equacao = equacao.split("+", "-")

# print(equacao)
# for i in range(len(equacao)):
#     equacao[i] = equacao[i].strip()

# print(equacao)

equacao = ["3x^2", "+", "x", "-", "5"]

equacao_limpa = []

for termo in equacao:
    if termo not in ("+", "-", "*", "/"):
        equacao_limpa.append(termo)

print(equacao_limpa)