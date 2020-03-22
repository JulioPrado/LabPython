'''
Você conhece o jogo do NIM? Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
Objetivo

Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa"
Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

'''

def computador_escolhe_jogada(n,m):
	if n<m:
		print("\nComputador retira",n,"peças.")
		return n		
	elif n%(m+1)>0:
		print("\nComputador retira",(n%(m+1)),"peças.")
		return (n%(m+1))
	else:
		print("\nComputador retira",m,"peças.")
		return m

def usuario_escolhe_jogada(n,m):
	jogadaValida=False
	
	while(not jogadaValida):
		jogada=int(input("\nQuantas peças você deseja retirar? "))
		
		if jogada<1 or jogada>m:
			print("\nJogada inválida! Selecione um número entre 1 e",m,",inclusive.")
		else:
			jogadaValida=True
			print("Jogador retira",jogada,"peças.")
			return jogada

def partida():

	n=int(input("Quantas peças serão usadas no jogo?: "))
	m=int(input("Qual o máximo de peças retiradas por turno?: "))
	
	if n%(m+1)==0:
		print("\nVocê começa!\n")
		while (n>0):
			n=n-usuario_escolhe_jogada(n,m)
			print("Peças restantes:",n)
			if n==0: vencedor="Jogador"
			else:
				n=n-computador_escolhe_jogada(n,m)
				print("Peças restantes:",n)
				if n==0: vencedor="Computador"
	else:
		print("\nComputador começa.")
		while (n>0):
			n=n-computador_escolhe_jogada(n,m)
			print("Peças restantes:",n)
			if n==0: vencedor="Computador"
			else:	
				n=n-usuario_escolhe_jogada(n,m)
				print("Peças restantes:",n)
				if n==0: vencedor="Jogador"

	print("\nFim do jogo! O",vencedor," ganhou!")
	return vencedor

def campeonato():
	campeonato=[]
	print("Você escolheu um campeonato!")
	print("\n\n*** Rodada 1 ***\n")
	campeonato.append(partida())
	print("\n\n*** Rodada 2 ***\n")
	campeonato.append(partida())
	print("\n\n*** Rodada 3 ***\n")
	campeonato.append(partida())
	print("Fim do campeonato!\nPlacar: Você 0 X 3 Computador")
	#print(campeonato)


def main():
	opc=int(input("Bem-vindo ao jogo do NIM! Escolha: \n 1- Partida isolada \n 2- Campeonato\n\n"))
	if opc==1: partida()
	elif opc==2: campeonato()
	else: print("Opção inválida!")

main()
