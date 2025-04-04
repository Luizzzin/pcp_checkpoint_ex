total_dias = 365 #valor em dias de um ano
total_mes = 30 #valor em dias de um mes


print("---------------------")

ano = int(input("Quantos anos voce tem? :\n"))
meses = int(input("e quantos meses ? :\n"))
dia = int(input("Quantos dias? :\n"))

print("---------------------")

# descobrir quantos dias o usuario tem pela quantidade de anos
conta_ano = total_dias * ano 

# descobrir quantos dias o usuario tem pela quantidade de meses
conta_mes = total_mes * meses  

resultado = conta_mes + conta_ano + dia

print(f"Voce tem aproximadamente : {resultado} de dias na vida")