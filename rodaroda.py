# Componentes do GRupo SHORYUKEN FROM HELL
# Leandro de Castilho RA: 6210018
# Vinicius Eduardo Cursi RA: 6310098
# Rodrigo Passos da Cunha RA: 6310082
# Ronaldo RA:6310083
# Julio Cesar RA:6310048
# Talita Monica RA:6310087
# Hebeny Rafaela RA:6310036
# Bruno Bennati RA:6310006
# Melksedeque Silva RA:6310062
# Matheus RA: 6310059
# Michel RA:6310063

#Importa bibliotecas ao sistema
import random
import funcoes
import string
import time

import pygame
pygame.init()

from pygame.mixer import Sound
audio = pygame.mixer.Sound("maoe.ogg")
audio.play()



#Variaveis do programa
global indicePrimario, indiceSecundario, indiceTerceario, nomeJogadores, pontosJogadores, valorJogadorRoleta, desejoJogador, segundoDesejoJogador, arriscaPalavra, arriscaLetra, pegaPalavra, tabelaPalavra, fimPrograma
quantidadeJogadores = 0



#Pega a palavra do jogo
pegaPalavra = funcoes.palavraJogo()
indicePrimario = 0
tabelaPalavra = []
while indicePrimario < len(pegaPalavra) :
	tabelaPalavra.append("_")
	indicePrimario = indicePrimario + 1


#Bem vindo ao programa
time.sleep(0.5)
print "\n\n\n\n\n***************************************************\n** Bem vindo ao programa do Roda Roda do Bau !!! **\n***************************************************"
time.sleep(1)
quantidadeJogadores = int(raw_input("\n\nDigite o numero de jogadores: (numero inteiro): "))

#Define pontos iniciais dos Jogadores
indicePrimario = 0
pontosJogadores = []
while indicePrimario < quantidadeJogadores:
	pontosJogadores.append(0)
	indicePrimario = indicePrimario + 1


#Pega o nome dos jogadores
nomeJogadores = funcoes.nomedosJogadores(quantidadeJogadores)

#Printa o nome dos jogadores na tela
print "\n\n\nSilvio Santos: E o nome dos Jogadores sao:"
indicePrimario = 0
while indicePrimario < len(nomeJogadores):
	print "Player \""+str(indicePrimario+1)+"\": %s" % nomeJogadores[indicePrimario]
	indicePrimario = indicePrimario + 1
	
#Imprime a palavra ? NAO
time.sleep(3)
print "\n\n\n\nA palavra do jogo Roda roda contem \""+str(len(pegaPalavra))+"\" letras :"
#print pegaPalavra
print tabelaPalavra
print "\n\n\n\n\n\n\n"
time.sleep(3)
#Inicia Jogo
indicePrimario = 0
fimPrograma = 0
while fimPrograma < len(pegaPalavra):
	while indicePrimario < quantidadeJogadores :
		indiceTerceario = ""
		#Ve se o jogador quer jogar
		print "\n\n\n\nA Palavra: "
		print tabelaPalavra
		print "\n\n\""+str(nomeJogadores[indicePrimario])+"\" voce possui ate agora R$ %s em barras de ouro" % pontosJogadores[indicePrimario]
		desejoJogador = raw_input("O Jogador \""+str(nomeJogadores[indicePrimario])+"\" deseja rodar a roleta ? (S/N) : ")
		# Caso o jogador queira jogar
		if desejoJogador.upper() == "S":
			print "\n\n\n\nMuito bem, muito bem .. temos um corajoso aqui nao e \""+str(nomeJogadores[indicePrimario])+"\""
			#Roda a roleta
			valorRoleta = funcoes.rodaRoleta()
			#Caso a roleta nao passe a vez ou perca tudo
			if valorRoleta != "PASSA A VEZ" and valorRoleta != "PERDE TUDO":
				print "\n\nValendo R$ %s em barras de ouro" % valorRoleta
				segundoDesejoJogador = raw_input("\""+str(nomeJogadores[indicePrimario])+"\", voce deseja arriscar uma palavra ou uma letra ? (palavra/letra) ")
				# Arriscando palavra
				if segundoDesejoJogador.upper() == "PALAVRA":
					arriscaPalavra = raw_input("Digite a palavra que deseja arriscar: ")
					if arriscaPalavra == pegaPalavra :
						time.sleep(2)
						print "\n\n****************************************************\n****************************************************\nMaooehh !! IHII !!! Voce acertou a palavra senhor/senhora \""+str(nomeJogadores[indicePrimario])+"\""
						print "A palavra e: %s" % pegaPalavra
						pontosJogadores[indicePrimario] = pontosJogadores[indicePrimario] + valorRoleta
						print "Voce acaba de ganha R$ %s em barras de ouro que valem mais do que dinheiro !!!\n****************************************************\n****************************************************" % pontosJogadores[indicePrimario]
						time.sleep(1)
						print "\n\n****************************************************\n****************************************************\n*** PARABENS \""+str(nomeJogadores[indicePrimario])+"\" VOCE GANHOU O RODA RODA DO BAU ** \n****************************************************\n****************************************************"
						indicePrimario = quantidadeJogadores
						fimPrograma = 1000
					else :
						time.sleep(2)
						print "\n\n\n\nAi, ai .. mas que pena meu amigo !! Voce errou !!!\nVolta pra la, volta pra la, agora vamos ver se o outro jogador sabe a palavra !!\n\n\n\n\n\n"
						time.sleep(1)
				#
				elif segundoDesejoJogador.upper() == "LETRA":
					arriscaLetra = raw_input("Digite a letra que deseja arriscar?: ")
					indiceSecundario = 0
					while indiceSecundario < len(pegaPalavra):
						if arriscaLetra == pegaPalavra[indiceSecundario]:
							tabelaPalavra[indiceSecundario] = pegaPalavra[indiceSecundario]
							print "OK"
							pontosJogadores[indicePrimario] = pontosJogadores[indicePrimario] + valorRoleta
							fimPrograma = fimPrograma + 1
						indiceSecundario = indiceSecundario + 1
			elif valorRoleta != "PERDE TUDO" and valorRoleta == "PASSA A VEZ":
				time.sleep(1)
				print "\n\n\nMaoooee !! Quase quase meu amigo, mas voce perdeu a vez\n\n\n"
				time.sleep(3)
			elif valorRoleta == "PERDE TUDO" and valorRoleta != "PASSA A VEZ":
				pontosJogadores[indicePrimario] = 0
				print "Ai ai, ihiii !! que mal sorte em rapaz/senhora, voce acaba de perde tudo \""+str(nomeJogadores[indicePrimario])+"\""
				time.sleep(4)
		# Caso o jogador nao queira jogar
		else :
			print "\n\nMaoooeee !! Ihii, \""+str(nomeJogadores[indicePrimario])+"\", voce e uma banana, voce e uma banana senhor/senhora \""+str(nomeJogadores[indicePrimario])+"\" !! IHIII\n\n\n\n"
		indicePrimario =  indicePrimario + 1
	if fimPrograma == 0 :
		fimPrograma = 0
		indicePrimario = 0
	elif fimPrograma == len(pegaPalavra):
		print "\n\n****************************************************\n****************************************************\n*** PARABENS VOCE GANHOU O RODA RODA DO BAU ** \n****************************************************\n****************************************************"
	else :
		indicePrimario = 0
