venda = input('Registre um produto. para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ')
vendas = []
#CRIE AQUI O PROGRAMA
while venda != '':
    vendas.append(venda)
    venda = input('Registre um produto. Para cancelar o registro de um novo produto, basta apertar enter sem digitar nada: ')
    print('Restritros Finalizados. As vendas cadastradas foram: {}'.format(vendas))