"""
Programa sencillo que permite a los usuarios calcular su Índice de Masa Corporal (IMC).
El IMC es una medida utilizada para determinar si una persona tiene un peso saludable en relación con su altura.
"""

altura = float(input("Porfavor escribe tu altura en m."))
peso = float(input("Porfavor escribe tu peso en kg."))

imc = peso / (altura * altura)

if imc < 18.5:
    categoria = "un bajo peso"
elif 18.5 <= imc < 24.999:
    categoria = "un peso normal"
elif 25 < imc < 29.999:
    categoria = "sobre peso"
else:
    categoria = "obesidad"

print("Tu IMC es de", ("%.3f"%(imc)))
print("Tienes", categoria)



