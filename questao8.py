quant = 0

pergunta1= input('Telefonou para a vítima? ')
pergunta2= input('esteve no local do crime? ')
pergunta3= input('mora perto da vitima? ')     
pergunta4= input('devia para a vítima? ')
pergunta5= input('ja trabalhou com a vítima? ')

      
if pergunta1 == 's':
    quant = quant+1
    
if pergunta2 == "s":
    quant= quant+1

if pergunta3 == 's':
    quant= quant+1

if pergunta4 == 's':
    quant= quant+1

if pergunta5 == 's':
    quant= quant+1


if quant == 2:
    print ('suspeita')
elif quant >= 3 and quant <= 4:
    print ('cúmplice')
elif quant == 5:
    print ('assassino')
else:
    print ('inocente')