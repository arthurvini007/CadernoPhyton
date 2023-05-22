def calcular_conta(consumo , taxa_de_servico, desconto_fidelidade):
    servico = consumo * taxa_de_servico
    desconto = consumo * desconto_fidelidade
    valor = consumo + servico
    valor = valor - desconto
    return valor

    
valor = calcular_conta(consumo=100, taxa_de_servico=0.15, desconto_fidelidade=0.1)
print("O valor final e :", valor)

"""""
consumo = 100 
servico = consumo * taxa_servico
desconto = consumo * deconto_fidelidade

valor = consumo + servico 
valor = valor - desconto 

"""""