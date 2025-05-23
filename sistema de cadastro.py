class Estudante:
    def __init__(self, nome, cidade, transporte): 
        self.nome = nome
        self.cidade = cidade
        self.transporte = transporte
        
    def __str__(self):
         return f"Nome: {self.nome}, Cidade: {self.cidade}, Transporte: {self.transporte}"
def adicionar_cadastro():
    nome_user = input("digite seu nome:\n")
    moradia_user = input("onde você mora?\n")
    transporte_user = input("você tem tansporte pra vir a escola?\n").lower()
    if transporte_user =="sim":
        transporte_tipo = input("qual o tipo de transporte?\n")
        estudante_obj = Estudante(nome_user, moradia_user, transporte_tipo)
        informacoes.append(estudante_obj) 
        print("Obrigado por responder o questionario")
    elif transporte_user == "nao":
        print("Obrigado por responder o questionario, iremos providenciar transporte pra sua região o mais rapido possivel")
        estudante_obj = Estudante(nome_user, moradia_user, "sem transporte")
        informacoes.append(estudante_obj)
    else:
        print("resposta invalida")

        
def conferir_cadastros():
    if informacoes == []:
        print("A lista esta vazia")
    else:
        for estudante in informacoes:
            print(estudante)
            
informacoes = []
while True:
   
    print("-------------------------")
    print("||1. cadastrar pessoa  ||")
    print("||2. conferir cadastros||")
    print("||3. sair              ||")
    print("-------------------------")
    res = input("oque deseja fazer?\n")
    if res == "1":
        adicionar_cadastro()
    elif res == "2":
        conferir_cadastros()
    elif res == "3":
        print("saindo....")
        break
    else:
        print("Opção inválida")