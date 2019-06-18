numero = int(input('informe um número: '))
quant = 1

if numero >= 1 and numero <=10:
    while quant <= 10:
        tab = numero * quant
        print ("%i X %i = %i" % (numero, quant, tab))
        quant = quant + 1

else:
    print ('Erro. Apenas valores de 1 a 10')