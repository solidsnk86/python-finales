# Calculadora IMC
# Índice de Masa Corporal

height = float(input("Ingrese su altura: "))
weight = float(input("Ingrese su peso: "))

imc = weight / (height**2)
print(f"Su IMC es {imc:.2f}")

if imc < 18.5:
    print("Peso bajo")
elif 18.5 <= imc < 24.5:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobre peso")
else:
    print("Obesidad")

