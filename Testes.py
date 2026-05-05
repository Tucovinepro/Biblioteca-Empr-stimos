leitores = []
idade_do_leitores = []
tipos_de_livros = ["Romance", "Suspense", "Aventura", "Filosofia", "Literatura brasileira", "Literatura estrangeira", "Livros infantis", ]



def cadastrar_leitores(leitores):
   a = print(input("Qual o nome do novo leitor"))
   leitores.append(a)

def recomendações_para_os_leitores(idade_do_leitor):
   b = print(input('Qual a idade do leitor'))
   idade_do_leitor.append(b)
   if b<=10:
      print("Recomende um livro infantil para um possivel empréstimo")
   elif b<=15:
      print("Recomende livros de suspense, aventura, etc... para um possivel empréstimo")
   else:
      print("Depende do gosto do leitor")
   

def empréstimos(tipos_de_livros):
   c = (input("Qual tipo de livro que o leitor gostaria de adquirir? "))
   if c not in tipos_de_livros:
      print("Não temos esse tipo de livro")
   elif c in tipos_de_livros:
      print("Tipo disponível")

def tempo_de_empréstimo():
  w = int((input("Quanto é o tempo de empréstimo ")))
  if w <= "5":
     print("O leitor deve pagar 10 reais de multa se passar do tempo")
  elif w <= "10":
     print("O leitor deve pagar 20 reais de multa se passar do tempo")
  else:
     print("O leitor paga 45 reais de multa se passar do tempo")
      


      
while True:
   print("\nSeja bem vindo ao menu da biblioteca Kogaguinaoka, escolha uma opção:")
   print("1 - Cadastrar leitor.")
   print("2 - Fazer empréstimo.")
   print("3 - Sair.")
   opcao = input("> ")

   if opcao == "1":
      cadastrar_leitores(leitores)
      recomendações_para_os_leitores(idade_do_leitores)
   elif opcao == "2":
      empréstimos(tipos_de_livros)
      tempo_de_empréstimo()
   elif opcao == "3":
      print("Até mais")
      break
   else:
      print("Opção inválida")
      



    
   


   

      


   