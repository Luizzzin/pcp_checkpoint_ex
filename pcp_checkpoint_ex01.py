dolar = 0.18
euro = 0.1631
arg = 189
libra = 0.1361
iene = 26.29

print("---------------------")
real = float(input("Quantos Reais voce tem? :\n"))

print("---------------------")

condolar = dolar * real
coneuro = euro * real
conarg = arg * real
conlibra = libra * real
coniene = iene * real

print(f"Em dolar Voce tem: {condolar:.2f}")
print(f"Em euro Voce tem: {coneuro:.2f}")
print(f"Em peso argentino Voce tem: {conarg:.2f}")
print(f"Em libra Voce tem: {conlibra:.2f}")
print(f"Em iene Voce tem: {coniene:.2f}")
