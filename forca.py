from palavra_forca import palavra

letras_usuario = []
chances = 5
ganhou = False

while True:

    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra)
        else:
            print("_", end=" ")
        print("Você tem {chances} chances")
        tentativa = input("Escolha uma letra para advinhar: ")
        letras_usuario.append(tentativa.lower())

        if tentativa.lower() not in palavra.lower():
            chances -= 1

            ganhou = True
            for letra in palavra:
                if letra.lower() not in letras_usuario:
                    ganhou = False

        if chances == 0 or ganhou:
         break

    if ganhou:
        print(f"Parabéns, você ganhou. A palavra era : {palavra}")
    else:
        print(f"Você perdeu! A palavra era : {palavra}")