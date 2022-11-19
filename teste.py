import random


'''parâmetros: frequência / gosto / saudável (se n]ao for,)-> frequência de comidas ruins'''

opcoes = ["china in box", "burguer king", "poke", "sushi", "mexicano", "macarrão", "pizza"]
junk = [ "burguer king", "pizza"]
excluir = input("Coloque aqui opções que você NÃO quer, uma de cada vez: ")

while excluir != "fim":
    if excluir in opcoes:                   #remove quaisquer opções que o usuário não queira
        opcoes.remove(excluir)
    excluir = str(input("Coloque aqui opções que você NÃO quer, uma de cada vez: "))
    

def parametros():
    freq_saudavel = int(input("há quantos dias você comeu besteira?"))
    gosto = (input("Você está com vontade de comer algo? se sim o que?(uma opção apenas): " ))

    if gosto in ("burguer king", "pizza"):
        if freq_saudavel < 7 :
            if gosto in opcoes:
                for i in junk:
                    if i in opcoes:
                        opcoes.remove(i)
                print("O jantar será: " + random.choice(opcoes) )
        else:
            print("O jantar será: " + gosto)
    else:
        print("O jantar será: " + random.choice(opcoes) )
            

parametros()
