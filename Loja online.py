
    
fun=True
f1={"nome":"Harry Potter", "preço":"R$49,00", "estado": "não comprado"}
f2={"nome":"Vingadores", "preço":"R$79,00","estado": "não comprado"}
f3={"nome":"Shrek", "preço":"R$39,00", "estado":"não comprado"}
lista=[f1, f2, f3]




while True:
    print("Bem vindo a loja de filmes online.")
    print("Digite 1 para ver quais são os filmes.")
    print("Digite 2 para ver o preço dos filmes.")
    print("Digite 3 para comprar algum filme.")
    print("Digite 0 para sair.")
    escolha=int(input("O que você quer fazer:  "))

    if escolha==1:
        print("Os filmes que temos são :", f1["nome"], f1["estado"], f2["nome"], f2["estado"], f3["nome"], f3["estado"])
    elif escolha==2:
        esc=input("Qual filme você quer ver o preço.")
        if esc==f1["nome"]:
            print(f1["preço"])
        elif esc==f2["nome"]:
            print(f2["preço"])
        elif esc==f3["nome"]:
            print(f3["preço"])
        else:
            print("Filme não encontrado.")
    elif escolha==3:
        esc=input("Qual filme você quer comprar.")
        if esc==f1["nome"]:
            print("pronto.")
            f1["estado"]="comprado"
        elif esc==f2["nome"]:
            print("pronto.")
            f2["estado"]="comprado"
        elif esc==f3["nome"]:
            print("pronto.")
            f3["estado"]="comprado"
        else:
            print("Filme não encontrado.")
    elif escolha==0:
        print("saindo...")
        break