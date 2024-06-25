#ano2 = int(input("Digite um ano:"))
#print(f"em 2024 você tera: {2024 - ano2}")

altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))

imc = peso / (altura / 100) ** 2

print(f'O IMC É: {imc}')