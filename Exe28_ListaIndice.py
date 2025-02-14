produtos = ['TV', 'Celular', 'Mouse', 'Teclado', 'Tablet']
vendas = [1000, 1500, 350, 270, 900]
print("as vendas de {} foram de {}".format(produtos[2],vendas[2]))

produtos = ['TV', 'Celular', 'Mouse', 'Teclado', 'Tablet']
vendas = [1000, 1500, 350, 270, 900]
i = produtos.index('Mouse')
print('O valor de i é ' + str(produtos[i]))

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'geladeira', 'forno']
estoque = [100,150,100,120,70,180,80]
produto = input('Insira o nome do produto a letra minuscula ')
i = produtos.index(produto)
print(i)

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet', 'geladeira', 'forno']
estoque = [100,150,100,120,70,180,80]
produto = input('Insira o nome do produto a letra minuscula ')
if produto in produtos:

    i = produtos.index(produto)
    qtde_estoque = estoque[i]
    print('Temos {} unidades de {} no estoque'.format(qtde_estoque,produto))
else:
    print("produto não caracterizado")