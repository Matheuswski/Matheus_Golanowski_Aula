pessoas_presentes = ['John Snow','Jesse Pinkman','Aria Stark','Tyrion lannister']
#Quero saber se uma pessoa especifica está presente.
chamada = 'Aria Stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} esta presente'.format(chamada))
        break
    else:
        print('So um print para mostrar que o for passou por essa pessoa:'+str(pessoa))

pessoas_presentes = ['John Snow','Jesse Pinkman','Aria Stark','Tyrion lannister']
#Quero saber se uma pessoa especifica está presente.
chamada = 'Aria Stark'
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print('{} esta presente'.format(chamada))
        break
    else:
        print('So um print para mostrar que o for passou por essa pessoa:'+str(pessoa))
        continue        