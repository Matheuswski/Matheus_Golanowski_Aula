#Faça um programa que receba uma nota do aluno e se for SUPERIOR ou IGUAL a 7 (sete) apareça mensagem que ele esta APROVADO, se for INFERIOR a 5(cinco) ele esta "nao aprovado/ reprovado direto" e se estiver entre 5(cinco) e 7(sete) apareça mensagem "Não aprovao/Recuperação".
nota = int(input("Qual sua nota "))

if nota >= 7:
    print("Aprovado ")
else:
    if nota >= 5:
      print("Reprovado ")
    else:
     print("Recuperação ")