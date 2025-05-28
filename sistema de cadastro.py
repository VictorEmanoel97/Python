class Estudante:
    def __init__(self, nome, cidade, transporte): 
        self.nome = nome
        self.cidade = cidade
        self.transporte = transporte
        
    def __str__(self):
         return f"Nome: {self.nome}, Cidade: {self.cidade}, Transporte: {self.transporte}"
def adicionar_cadastro():
    respostas_validas = ["no", "nao", "n", "não"]
    resposta_transporte = input("você tem tansporte pra vir a escola?(sim/não)\n").lower()
    if resposta_transporte =="sim":
        print("Não é possivel cadastrar alguem que ja tenha transporte")
        
    elif resposta_transporte in respostas_validas:
        nome_user = input("digite seu nome:\n")
        moradia_user = input("onde você mora?\n")
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
