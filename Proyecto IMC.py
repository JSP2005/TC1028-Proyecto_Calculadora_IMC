"""
Programa sencillo que permite a los usuarios calcular su Índice de Masa Corporal (IMC).
El IMC es una medida utilizada para determinar si una persona tiene un peso saludable en relación con su altura.
"""

print("Bienvenido al programa de la calculadora de IMC (Índice de Masa Corporal).")
start = int(input(" \n Para comenzar presione la tecla 1 o 0 para terminar el programa. "))

inicio_fin = 1

while inicio_fin == 1:
    while start == 1:
        # Solicitar datos de entrada (altura, peso)
        altura = float(input("\n \n Porfavor escribe tu altura en m (ejemplo: 1.75).\n "))
        peso = float(input("\n Porfavor escribe tu peso en kg (ejemplo: 75).\n "))

        # Función para calcular IMC
        def calcular_imc(peso, altura):
            imc = peso / (altura * altura)
            return imc

        # Función para categorizar IMC
        def categoria_imc(imc):
            if imc < 18.5:
                categoria = "un bajo peso"
            elif 18.5 <= imc < 25:
                categoria = "un peso normal"
            elif 25 <= imc < 30:
                categoria = "sobre peso"
            else:
                categoria = "obesidad"
            return categoria

        # Calcular IMC
        imc = calcular_imc(peso, altura)

        # Función para agregar consejos
        categoria = categoria_imc(imc)
        
        # Lista de Consejos
        lista_consejos = ["Considera consultar a un nutriólogo para evaluar tu dieta y asegurarte de que estás recibiendo los nutrientes necesarios.",
                          "¡Felicidades! Mantén un estilo de vida saludable con una dieta equilibrada y ejercicio regular.",
                          "Podrías beneficiarte de una dieta más equilibrada y un aumento en la actividad física. Consulta a un profesional de la salud si es necesario.",
                          "Es importante que hables con un profesional de la salud para obtener orientación sobre cómo reducir tu peso de manera segura."]
        
        def consejos(categoria, lista_consejos):
            if categoria == "un bajo peso":
                return lista_consejos[0]
            elif categoria == "un peso normal":
                return lista_consejos[1]
            elif categoria == "sobre peso":
                return lista_consejos[2]
            elif categoria == "obesidad":
                return lista_consejos[3]
            
        # Mostrar los resultados
        print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
        print("Tu IMC es de", ("%.2f"%(calcular_imc(peso, altura))))
        print("Según tu IMC, tienes", categoria_imc(imc))
        print(consejos(categoria, lista_consejos))
        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
        
        start = int(input("Presione 1 si quiere volver a usar el programa o 0 si ya terminó." ))

    while start != 1:
        if start == 0:
            inicio_fin = 2
            start = 1
        else:
            start = int(input("\n El número que ingreso es incorrecto. \n \n Presione 1 si quiere volver a usar el programa o 0 si ya terminó." ))

if inicio_fin == 2:
    print(" \n Gracias por usar el programa. Esperamos que te haya sido de utilidad." )
