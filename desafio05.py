def inverter_string(text):
    resultado = ''
    for caracter in text:
        resultado = caracter + resultado
    return resultado

string = str(input("Digite um texto à ser invertido: "))
print(inverter_string(string))