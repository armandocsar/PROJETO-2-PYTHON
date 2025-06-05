nomes_forca = ['augusto','pitaia','submarino','havan','nataçao']
letras_advinhadas = []
import random
palavra_aleatoria = random.choice(nomes_forca) # ira escolher aleatoriamente uma das palavras
chances = 6 # O maximo qure o usuario pode errrar 

jogo = int(input("Digite 0 para iniciar o JOGO DA FORCA: "))
if jogo == 0:
    print("Jogo iniciado!")
else:
    print("Numero errado!")

while True:
    palavra_mostrada = ''
    for letra in palavra_aleatoria:
        if letra in letras_advinhadas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += '_'
    
    print(f"\nPalavra: {palavra_mostrada}")
    print(f"Letras ja utilizadas: {letras_advinhadas}")
    print(f"Restam: {chances} tentativas. ")

    letra_digita = str(input("Digite uma letra: "))
    if letra_digita in letras_advinhadas:
        print("Voce ja usou essa letra.")
        continue   #AAAAA num sabia desse continue kkkkk descobri pesquisando
    letras_advinhadas.append(letra_digita)

    if palavra_mostrada == palavra_aleatoria:
        print("Voce acertou a palavra. Parabens!")
        break
    
    if chances == 0:
        print("Voce perdeu!")
        break
    if letra_digita not in palavra_aleatoria:
        print("\nLetra incorreta")
        chances -= 1
    else:
        print("\nLetra correta")