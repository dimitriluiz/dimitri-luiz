
# Cálculo do IMC
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Fórmula do IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")