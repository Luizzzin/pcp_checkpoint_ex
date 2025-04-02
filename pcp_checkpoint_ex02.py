print("-------------------")
valor = int(input("Escolha um numero de 0 a 999: \n"))
print("-------------------")

centena = (valor // 100)
dezena = (valor % 100) // 10
unidade = (valor % 100) % 10 // 1

if(valor < 0):
    print("Seu numero tem que ser um valor entre 0 a 999")
elif(valor > 999):
    print("Seu numero tem que ser um valor entre 0 a 999")
else:
    print(f"Seu numero tem: {centena} centena")
    print(f"Seu numero tem: {dezena} dezena")
    print(f"Seu numero tem: {unidade} unidade")
