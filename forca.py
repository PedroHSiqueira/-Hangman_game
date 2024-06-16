import random
import csv
import os
import time

def pegar_palavra():
    with open("palavras.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        palavras = [palavra for palavra in leitor]
        palavra_sorteada = random.choice(palavras)
        
        if(palavra_sorteada == "Nome"):
            palavra_sorteada = random.choice(palavras)
        
        return palavra_sorteada

def chute_certo(palavra_sorteada, tentativa, letras_certas):
    index = 0
    for letra in palavra_sorteada:  #verifica se a palavra possui a letra
        if tentativa == letra:
            letras_certas[index] = letra
        index += 1
        
def titulo():
    print("-".center(60, "-"))
    print("Bem vindo ao jogo da Forca")
    print("-".center(60, "-"))

def salvar_pontuacao(nome, pontuacao,acertou):
    with open("pontuacao.csv", "a", newline="") as arquivo:
        campus_headers = ["Nome", "Resultado", "Pontos"]
        status = ""
        
        if pontuacao == "pontos":
            pontuacao = 100
        
        if acertou == True :
            status = "Venceu"
        else:
            status = "Perdeu"
            
        escritor = csv.DictWriter(arquivo, campus_headers)
        escritor.writerow({"Nome": nome, "Resultado": status, "Pontos": pontuacao})
    
#Jogo 
def jogar():
    os.system("cls")
    
    titulo()
    nome = input("Digite seu nome: ")
    os.system("cls")

    dados_jogo = pegar_palavra()

    palavra_sorteada = dados_jogo[0].upper()
    pontuacao = dados_jogo[1]

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
            print(f"Você Errou {erros} de 5 chances!\n")
            time.sleep(2)


        perdeu = erros == 5
        acertou = "_" not in letra_acertos
        print(letra_acertos)
        os.system("cls")

    if (acertou):
        print("=".center(60, "="))
        print(f"Parabéns {nome}, você acertou a palavra!")
        print("=".center(60, "="))
        salvar_pontuacao(nome, pontuacao, True)
    else:
        print("=".center(60, "="))
        print("Bah ... Você Perdeu a palavra era: ", palavra_sorteada)
        print("=".center(60, "="))
        salvar_pontuacao(nome, 0, False)


def tabela():
    os.system("cls")
    with open("pontuacao.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)
        print("Tabela de Pontuação")
        print("=".center(60, "="))
        for linha in leitor:
            print(f"{linha['Nome']} - {linha['Resultado']} - {linha['Pontos']}")
        print("=".center(60, "="))
        input("Pressione Enter para voltar ao menu ...")
        os.system("cls")        
    
while True:
    print("Escolha uma opção".center(60, "-"))
    print("1. Jogar Forca")
    print("2. Tabela de Pontuação")
    print("3. Finalizar")
    print("-".center(60, "-"))
    opcao = int(input("Opção: "))
    
    if opcao == 1:
      jogar()
    elif opcao == 2:
      tabela()
    else:
      break