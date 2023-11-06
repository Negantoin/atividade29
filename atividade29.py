# Exercício Python 29: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
pesos = []
for i in range(1,6):
    peso = float(input("Digite o seu peso: "))
    pesos.append(peso)
    listapesos = sorted(pesos)
print(f"O menor peso é: {listapesos[0]} e o maior peso é: {listapesos[4]}")