#TRANSFORMA APENAS A PRIMEIRA LETRA DE UMA STRING EM MAIUSCULA
nome = "matheus"
print(nome.capitalize(),"\n")

#TRANSFORMA TODAS AS LETRAS EM MINUSCULA
nome = "MATHEUS"
print(nome.casefold(),"\n")

#CONTA O NUMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING
nome = "MatheusGolanowski@gmail.com"
print(nome.count('a'),"\n")

#RESTORNA true (verdadeiro) OU false (falso) PARA UM TESTE se A STRING TERMINA COM UMA STRING ESPESCIFICA
nome = "MatheusGolanowski@gmail.com"
print(nome.endswith('gmail.com'),"\n")

#ENCONTRA A POSIÇÂO DO TERMO PROCURADO. LEMBRE-SE COMEÇA DO zero
nome = "MatheusGolanowski@gmail.com"
print(nome.find('@'),"\n")

#VERIFICA SE O TEXTO É todo FEITO COM LETRAS
nome = "Matheus"
print(nome.isalpha(),"\n")

#VERIFICA SE O TEXTO É FEITO COMnumeros.
nome = "123"
print(nome.isnumeric(),"\n")

#SUBISTITUI UM CARACTERE ESCOLHIDO POR OUTRO 
nome = "Matheus"
print(nome.replace('t','a'),"\n")

#SEPARA O TEXTO string BASEADO EM ALGUM CARACTERE INDICADO
nome = "Matheus @ Paula Fernandes"
print(nome.split('@'),"\n")

#COLOCAR TODAS AS LETRAS INICIAIS EM maiuscula
nome = "matheus golanowski"
print(nome.title(),"\n")

#RETIRA OS CARACTERES INDESEJADOS< COMO POR EXEMPLO espaços QUE NÂO AGREGAM VALOR
nome = "  matheus golanowski"
print(nome.strip(),"\n")

#RETORNA true Ou false PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO
nome = "matheus 2009"
print(nome.startswith("ser"),"\n")
print(nome.startswith("Ser"),"\n")