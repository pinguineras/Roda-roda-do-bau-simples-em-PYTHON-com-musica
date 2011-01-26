import random
import time

#
global roleta, indicePrimarioFunc, indiceSecundarioFunc, player
roleta = [100, 200, 300, 450, "PASSA A VEZ", 600, 1000, 2000, 2500, "PASSA A VEZ", "PERDE TUDO", 100, 200, 300, 450, "PASSA A VEZ", 600, 1000, "PASSA A VEZ", 2000, 2500, "PASSA A VEZ"]
#roleta = ["PASSA A VEZ", "PASSA A VEZ"]


#
def palavraJogo():
	arquivoPalavras = file("palavras.txt").read()
	separaPalavras = arquivoPalavras.split(",")
	quantidadePalavras = len(separaPalavras)
	sorteiaPalavra = random.randrange(0, quantidadePalavras)
	return separaPalavras[sorteiaPalavra]
	
def nomedosJogadores(numberOfPlayers) :
	indicePrimarioFunc = 0
	indiceSecundarioFunc = []
	player = []
	while indicePrimarioFunc < numberOfPlayers :
		indiceSecundarioFunc = raw_input("Digite o nome do jogador \""+str(indicePrimarioFunc+1)+"\": ")
		player.append(indiceSecundarioFunc)
		indicePrimarioFunc = indicePrimarioFunc + 1
	return player
	
def rodaRoleta ():
	indicePrimarioFunc = 0
	valordaRoleta = random.randint(0, (len(roleta)-1))
	time.sleep(2)
	print "\n\n\nRoda, roda ... RODANDO !! Maoee , IHIII !!!"
	while indicePrimarioFunc < 5 :
		time.sleep(0.5)
		print (indicePrimarioFunc+1)*"."
		indicePrimarioFunc = indicePrimarioFunc + 1
	return roleta[valordaRoleta]

