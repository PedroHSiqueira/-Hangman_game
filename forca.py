import random
import csv
import os
import time



def pegar_palavra():
    with open("palavras.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        palavras = [palavra for palavra in leitor]
        palavra_sorteada = random.choice(palavras)
        return palavra_sorteada

def chute_certo(palavra_sorteada, tentativa, letras_certas):
    index = 0
    for letra in palavra_sorteada:  #verifica se a palavra possui a letra
        if tentativa == letra:
            letras_certas[index] = letra
        index += 1
        
def titulo():
    print("=" * 30)
    print("Jogo da Forca em pyhon")
    print("=" * 30 + "\n")

def salvar_pontuacao(nome, pontuacao,acertou):
    with open("pontuacao.csv", "a") as arquivo:
        status = ""
        
        if acertou == True:
            status = "Ganhou"
        else:
            acertou = "Perdeu"
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, status, pontuacao])
    
#Jogo 
titulo()
nome = input("Digite seu nome: ")
os.system("cls")

dados_jogo = pegar_palavra()

palavra_sorteada = dados_jogo[0].upper()
pontuacao = dados_jogo[1]

print(dados_jogo)

letra_acertos = ["_" for letra in palavra_sorteada]
perdeu = False
acertou = False
erros = 0


while (not perdeu and not acertou):
    titulo()
    print(f"{letra_acertos}\n")
    
    tentativa = input("Digite uma letra?:  ")
    print()
    tentativa = tentativa.strip().upper()
    
    if tentativa in palavra_sorteada:
        chute_certo(palavra_sorteada, tentativa, letra_acertos)
    else:
        erros += 1
        print(f"Você Errou {erros} de 7 chances!\n")
        time.sleep(2)
        
    
    perdeu = erros == 7
    acertou = "_" not in letra_acertos
    print(letra_acertos)
    
    os.system("cls")

if (acertou):
    print("=".center(60, "="))
    print(f"Parabéns {nome}, você acertou a palavra!")
    print("=".center(60, "="))
    salvar_pontuacao(nome, pontuacao, acertou)
else:
    print("=".center(60, "="))
    print("Bah ... Você Perdeu a palavra era: ", palavra_sorteada)
    print("=".center(60, "="))
    salvar_pontuacao(nome, 0, acertou)