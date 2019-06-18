morango = int(input('quilos de morango que será comprado: '))
maca = int(input('quilos de maça que será comprado: '))
kg = maca + morango
 
if kg <= 5:
    pMorango = morango * 2.50
    pMaca = maca * 1.80
    pTotal = pMaca + pMorango
    
else:
    pMorango = morango * 2.20
    pMaca = maca * 1.50
    pTotal = pMaca + pMorango
    
    if kg > 8 or pTotal > 25.00:
        pTotal = (pTotal - (pTotal * 0.1))


print ('o valor total da compra é: R$' , pTotal)