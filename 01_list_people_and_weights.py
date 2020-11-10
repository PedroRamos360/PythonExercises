class Pessoa:
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso
        
    def __repr__(self): 
        return "nome:%s peso:%s" % (self.__nome, self.__peso)

    def get_nome(self): 
        return self.__nome

    def get_peso(self): 
        return self.__peso


pessoas = []
while True:
    nome = input('Nome: ').strip().title()
    peso = int(input('Peso [Kg]: '))
    pessoa = Pessoa(nome, peso)
    pessoas.append(pessoa)
    continuar = input('Continuar? [s/n]').strip().lower()
    if continuar == 'n':
        break

print("Problema A:")
print(len(pessoas))

print("Problema B:")
pessoas_decrescente = sorted(pessoas, key = Pessoa.get_peso, reverse=True)
for i in range(3):
    print(pessoas_decrescente[i])

print("Problema C:")
pessoas_crescente = sorted(pessoas, key = Pessoa.get_peso)
for i in range(3):
    print(pessoas_crescente[i])

