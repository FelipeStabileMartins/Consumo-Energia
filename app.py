# Consumo de energia
# Felipe 

#Entrada
aparelho = input("Digite o nome do Aparelho:")
potencia = float(input("watts:"))
horas_Dia= float(input("tempo medio de uso diario em horas:"))

#Processamento
consumo_mensal = (potencia * horas_Dia * 30) / 1000

custo_estimado = consumo_mensal * 0.75 


#Saida
print(f"Nome do aparelho:{aparelho}")
print(f"consumo mensal:{consumo_mensal:.2f} kWh")
print(f"custo estimado:{custo_estimado:.2f} R$")

if custo_estimado > 30:
    print("temos que economizar")
else:
    print("tudo certo") 


