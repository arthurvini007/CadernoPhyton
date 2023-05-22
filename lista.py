notas = [8, 10 , 8.5]

print(notas[0])

notas.append(9)

notas.sort(reverse=True)

notas.pop()

notas.insert(0,8)

notas.pop(0)

qtd = len(notas)
total = 0 

i = 0 
while i < qtd : 
    total = total + notas[i]
    i = i + 1

print("O total das natas e: ", total)
media = total / qtd
print("A media das notas e: ", media)


#---------------------------------------------    

pessoa = ["Gabriel", 27 , "123456"]

print("O nome e", pessoa[0])
print("Sua idade e ", pessoa[1])

pessoas = [
    ["Gabriel",12],
    ["Lucas",20],
]