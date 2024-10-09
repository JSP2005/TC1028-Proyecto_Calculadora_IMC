"""
Programa sencillo que permite a los usuarios calcular su Índice de Masa Corporal (IMC).
El IMC es una medida utilizada para determinar si una persona tiene un peso saludable en relación con su altura.
"""
# Mensaje introductorio al programa
print("Bienvenido al programa de la calculadora de IMC (Índice de Masa Corporal).")

# Iniciar o terminar el programa
start = int(input(" \n Para comenzar presione la tecla 1 o 0 para terminar el programa. "))

#Variable para reiniciar o terminar programa
inicio_fin = 1

# Ciclo para reiniciar o terminar programa
while inicio_fin == 1:
    # Ciclo para empezar el programa
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
        
        # Matriz de Consejos
        matriz_consejos = [["Considera consultar a un nutriólogo para evaluar tu dieta y asegurarte de que estás recibiendo los nutrientes necesarios.",
                            "Aumenta el consumo de calorías al agregar más alimentos ricos en nutrientes y calorías saludables, como frutos secos, aguacate y granos enteros, a tus comidas diarias.",
                            "Incorpora ejercicios de fuerza en tu rutina para ganar masa muscular de manera saludable."],
                          ["¡Felicidades! Mantén un estilo de vida saludable con una dieta equilibrada y ejercicio regular.",
                           "Mantén una dieta equilibrada al seguir una dieta variada que incluya frutas, verduras, proteínas magras y grasas saludables para mantener tu peso ideal.",
                           "Realiza chequeos médicos de manera rutinaria para asegurarte de que tu salud se mantenga estable y prevenir futuros problemas."],
                          ["Podrías beneficiarte de una dieta más equilibrada y un aumento en la actividad física. Consulta a un profesional de la salud si es necesario.",
                           "Intenta reducir los alimentos procesados, azucarados o ricos en grasas saturadas en tu dieta para ayudar a controlar tu peso.",
                           "Aumenta tu nivel de actividad diaria con caminatas, ciclismo o cualquier ejercicio que disfrutes para quemar más calorías y mejorar tu salud cardiovascular."],
                          ["Es importante que hables con un profesional de la salud para obtener orientación sobre cómo reducir tu peso de manera segura.",
                           "Un nutricionista puede ayudarte a crear un plan de alimentación personalizado y seguro para perder peso de manera gradual y sostenible.",
                           "Comienza con actividades ligeras y ve aumentando gradualmente la intensidad para fortalecer tu cuerpo y mejorar tu resistencia sin poner en riesgo tu salud."]]
       
       # Relacionar categorías con lista de consejos
        def consejos(categoria, matriz_consejos):
            if categoria == "un bajo peso":
                return matriz_consejos[0][0]
            elif categoria == "un peso normal":
                return matriz_consejos[1][0]
            elif categoria == "sobre peso":
                return matriz_consejos[2][0]
            elif categoria == "obesidad":
                return matriz_consejos[3][0]
            
        # Mostrar los resultados
        print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
        print("Tu IMC es de", ("%.2f"%(calcular_imc(peso, altura))))
        print("Según tu IMC, tienes", categoria_imc(imc))
        print(consejos(categoria, matriz_consejos))
        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
        
        # Preguntar por más consejos
        mas_consejos = int(input("Escribe 1 si quieres más consejos o 0 si quieres seguir adelante."))
        if mas_consejos == 1:
            if categoria == "un bajo peso":
                print("\n", matriz_consejos[0][1], "\n \n", matriz_consejos[0][2], "\n")
            elif categoria == "un peso normal":
                print("\n", matriz_consejos[1][1], "\n \n", matriz_consejos[1][2], "\n")
            elif categoria == "sobre peso":
                print("\n", matriz_consejos[2][1], "\n \n", matriz_consejos[2][2], "\n")
            elif categoria == "obesidad":
                print("\n", matriz_consejos[3][1], "\n", matriz_consejos[3][2])
                 
        
        # Reiniciar o terminar programa
        start = int(input("Presione 1 si quiere volver a usar el programa o 0 si ya terminó." ))

    while start != 1:
        if start == 0:
            inicio_fin = 2
            start = 1
        else:
            start = int(input("\n El número que ingreso es incorrecto. \n \n Presione 1 si quiere volver a usar el programa o 0 si ya terminó." ))
            
# Mensaje de despedida del programa
if inicio_fin == 2:
    print(" \n Gracias por usar el programa. Esperamos que te haya sido de utilidad." )
    
