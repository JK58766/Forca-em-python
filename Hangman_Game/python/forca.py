from time import sleep
import os
import random

# Limpa Tela
def cls():
    os.system("cls")
    
# Pula Linha
def brokeLine():
    print("\n")

def title():
    print("*********************\n****Jogo da Forca****\n*********************")

choose = int(input("Escolha a dificuldade (1, 2 ou 3): "))
while choose < 1 or choose >3:
    choose = input("Insira um valor válido! (1, 2 ou 3): ")

def load_hidden_word():
    if choose == 1:
        facil = open(r"Hangman_Game\facil.txt", "r")
        word = []
        
        for line in facil:
            line = line.strip()
            word.append(line)
            
        facil.close()
        
        num = random.randrange(0, len(word))
        hiddenWord = word[num].upper()
        cls()
        brokeLine()
        return(hiddenWord)
    
    elif choose == 2:
        medio = open("Hangman_Game\medio.txt", "r")
        word = []
        
        for line in medio:
            line = line.strip()
            word.append(line)

        medio.close()
        
        num = random.randrange(0, len(word))
        hiddenWord = word[num].upper()
        cls()
        brokeLine()
        return(hiddenWord)
    
    elif choose == 3:
        dificil = open("Hangman_Game\dificil.txt", "r")
        word = []
        
        for line in dificil:
            line = line.strip()
            word.append(line)

        dificil.close()
        
        num = random.randrange(0, len(word))
        hiddenWord = word[num].upper()
        cls()
        brokeLine()
        return(hiddenWord)
    
        
def startCorrectLetter(hiddenWord):
    return["_" for letter in hiddenWord]

def print_loser_message(hiddenWord):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(hiddenWord))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def print_winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def draw(error):
    print("  _______     ")
    print(" |/      |    ")

    if(error == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
# Jogo
def play():
    
    title()
    hiddenWord = load_hidden_word()
    correctLetters = startCorrectLetter(hiddenWord)
    
    lose = False
    win = False
    error = 0
    
    print(correctLetters)
    
    while(not lose and not win):
        
        guess = input("Insira uma letra: ")
        guess = guess.strip().upper()
        
        if(guess in hiddenWord):
            index = 0
            for letter in hiddenWord:
                if(guess == letter):
                    correctLetters[index] = letter
                index += 1 
                
        else: 
            error += 1
            draw(error)
            
        lose = error == 7  
        win = "_" not in correctLetters
        print(correctLetters)
                
        #cls()  
        brokeLine()  
        print("Jogando. . . ")
        
        if(win):
            print_winner_message()
        else:
            if error == 7:
                print_loser_message(hiddenWord)
            
    print(f"Fim de Jogo!!!\nA palavra era {hiddenWord}")
    
if(__name__ == "__main__"):
    play()