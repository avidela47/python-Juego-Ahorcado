import random


def obtener_palabra_secreta() -> str:
    palabras = [
        "python",
        "javascript",
        "java",
        "react",
        "angular",
        "tyoescript",
        "git",
        "flask",
        "django",
        "Mmongoose",
    ]
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tenes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), "La cantidad de letras de la palabra es:", len(palabra_secreta))
    
    while not juego_terminado and intentos > 0:
        adivinanza = input("Ingresa una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Ingresa una letra valida")
        elif adivinanza in letras_adivinadas:
            print("Letra repetida, proba con otra")
        else:
             letras_adivinadas.append(adivinanza)
             if adivinanza in palabra_secreta:
                 print(f"Muy bien la letra '{adivinanza}' esta en la palabra")
             else:
                 intentos -= 1
                 print(f"La letra '{adivinanza}' no esta en la palabra, te quedan {intentos} intentos")
                 
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)   
        
        if'_' not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(f"Felicidades, has adivinado la palabra secreta: '{palabra_secreta}'")     
            
    if intentos == 0:
        palabra_secreta = palabra_secreta.capitalize()
        print(f"Perdiste, la palabra secreta era: '{palabra_secreta}'")
        
juego_ahorcado()
        
