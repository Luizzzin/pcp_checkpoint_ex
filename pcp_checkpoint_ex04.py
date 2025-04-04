total_dias = 365 #valor em dias de um ano
total_mes = 30 #valor em dias de um mes

print("---------------------")

dia = int(input("Quantos dias voce tem? :\n"))

print("---------------------")


#aqui eu to convertendo o tanto de dias para dividir pros meses e pegar os dias tambem
resto_mes = dia % total_dias 

calc_ano = dia // total_dias

calc_mes = resto_mes // total_mes
calc_dias = resto_mes % total_mes


print(f"Voce tem {calc_ano} anos, e tem {calc_mes} meses, e {calc_dias} dias")
