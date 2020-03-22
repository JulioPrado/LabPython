import math
 
def cls():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

Repetir=True
while Repetir==True:
	cls()
	print("Equação de segundo grau: ax²+bx+c=0")
	a=float(input("Digite o valor de A: "))
	if a==0:
		print("O valor de A não pode ser 0. Programa encerrado.")
		Repetir=False
	else:	
		b=(float(input("Digite o valor de B: ")))
		c=(float(input("Digite o valor de C: ")))
		print()

		delta=b**2-4*a*c

		if delta<0:
			print("Delta:",delta)
			print("esta equação não possui raízes reais")
		elif delta==0:
			x1= (-b+ math.sqrt(delta))/(2*a)
			print("Delta:",delta)
			print("a raiz desta equação é",x1)
		elif delta>0:
			x1= (-b+ math.sqrt(delta))/(2*a)
			x2= (-b- math.sqrt(delta))/(2*a)
			print("Delta:",delta)
			if x1<x2:
				print("as raízes da equação são",x1,"e",x2)
			else:
				print("as raízes da equação são",x2,"e",x1)

		xv=(-b)/(2*a)
		yv=(-delta)/(4*a)

		print("Coordenadas do vértice:")
		print("X:",xv)
		print("Y:",yv)

		Repetir=input("\nRepetir? s/n ")
		if Repetir=="s":
			Repetir=True
		elif Repetir=="n":
			Repetir=False
		else:
			print("\nResposta Inválida! Programa encerrado.\n")
			Repetir=False
