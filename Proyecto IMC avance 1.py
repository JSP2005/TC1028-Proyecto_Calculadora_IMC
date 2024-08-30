"""
Programa sencillo que permite a los usuarios calcular su Índice de Masa Corporal (IMC).
El IMC es una medida utilizada para determinar si una persona tiene un peso saludable en relación con su altura.
"""

print("Bienvenido al programa de la calculadora de IMC (Índice de Masa Corporal).")

# Solicitar datos de entrada (altura, peso)
altura = float(input("\n Porfavor escribe tu altura en m (ejemplo: 1.75).\n "))
peso = float(input("\n Porfavor escribe tu peso en kg (ejemplo: 75).\n "))

# Función para calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return(imc)

# Función para categorizar IMC
def categoria_imc(imc):
    if imc < 18.5:
        categoria = "un bajo peso"
    elif 18.5 <= imc < 24.999:
        categoria = "un peso normal"
    elif 25 < imc < 29.999:
        categoria = "sobre peso"
    else:
        categoria = "obesidad"
    return(categoria)

# Calcular IMC
imc = calcular_imc(peso, altura)

# Mostrar los resultados
print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
print("Tu IMC es de", ("%.2f"%(calcular_imc(peso, altura))))
print("Según tu IMC, tienes", categoria_imc(imc))
print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")



