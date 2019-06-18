salario= float(input('Informe seu salario por hora:'))
hm= float(input('Informe as horas trabalhadas no mês:'))

SB = (salario*hm)
Ir =  (SB*0.11)
INSS = (SB * 0.08)
SINDICATO = (SB * 0.05)
SALARIOLÍQUIDO = (SB-(Ir+INSS+SINDICATO))

print("Salário Bruto:", SB)
print("Imposto de Renda:", Ir)
print("INSS:", INSS)
print("Sindicato:", SINDICATO)
print("Salário Líquido ", SALARIOLÍQUIDO)