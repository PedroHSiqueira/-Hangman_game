import random

def pegar_palavra():
    arquivo = open("C:/Users/pedro/OneDrive/Documentos/Github/Jogo_forca/palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip() # usado para remover espaços em branco
        palavras.append(linha)
        
    arquivo.close()
    numero = random.randrange(0, len(palavras)) # Sorteia um número
    palavra_sorteada = palavras[numero].upper()
    return palavra_sorteada

def chute_certo(palavra_sorteada, tentativa, letras_certas):
    index = 0
    for letra in palavra_sorteada:  #verifica se a palavra possui a letra
        if tentativa == letra:
            letras_certas[index] = letra
        index += 1
        
    
#Jogo 
print("=" * 30)
print("Jogo da Forca em pyhon")
print("=" * 30 + "\n")

palavra_sorteada = pegar_palavra()

letra_acertos = ["_" for letra in palavra_sorteada]
perdeu = False
acertou = False
erros = 0

print(f"{letra_acertos}\n")

while (not perdeu and not acertou):
    tentativa = input("Digite uma letra?:  ")
    print()
    tentativa = tentativa.strip().upper()
    
    if tentativa in palavra_sorteada:
        chute_certo(palavra_sorteada, tentativa, letra_acertos)
    else:
        erros += 1
        print(f"Você Errou {erros} de 7 chances!\n")
    
    perdeu = erros == 7
    acertou = "_" not in letra_acertos
    print(letra_acertos)

if (acertou):
    print("Parabéns! acertou a palavra da rodada")
else:
    print("Bah ... Você Perdeu")