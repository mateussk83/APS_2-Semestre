from Criptografia import criptografia
class chaves(criptografia):
    def __init__(self, p, q):
        self.p = p
        self.q = q
#Nesta função fazemos o calculo do RSA 
#O calculo n = p * q
#O calculo phi = (p - 1) * (q - 1)
#Ele mostra as opções para e que o usuario deve selecionar, seleciona e ja executa 
#a conta para mostrar a chave publica e a privada
    def Gerar_chaves(self):
        n=self.p*self.q
        phi=(self.p-1)*(self.q-1)
        print("Escolha sua chave pública:\n")
        print(str(self.coprimos(phi)) + "\n")
        e=int(input())
        
        d=self.inverso_modular(e,phi) 
        return print("\nChaves públicas (e={0}, n={1}\nChaves privadas (d={2}, n={1})\n".format(str(e),str(n),str(d)))
#Conta para encontrar o maior divisor comum 
    def mdc(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b
#Conta para encontrar o Inverso modular
    def inverso_modular(self, a, m): 
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        print('Não ha inverso modular para o bloco.\n')
        return None
#Conta para mostrar os coprimos        
    def coprimos(self, a):
        lista_num = []
        for x in range(2, a): 
#se o inverso_modular numero (x,a) for diferente de vazio
#se o maior_divisor comum do numero(x,a) for igual a 1
#adicionar a lista 
            if self.mdc(a, x) == 1 and self.inverso_modular(x,a) != None: 
                lista_num.append(x)
        for x in lista_num:
#para cada numero dentro da lista que for igual ao inverso_modular(x,a) remove o numero x
            if x == self.inverso_modular(x,a):
                lista_num.remove(x)
        return lista_num
        


