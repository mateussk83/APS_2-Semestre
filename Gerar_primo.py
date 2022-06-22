from random import randrange, getrandbits
class Gerador_Numero_primo:
    def __init__(self):
        self.numero_primo = self.gerar_numero_primo()
#O teste Miller-Rabin é um teste probabilístico da primitividade de um dado 
#número n. Se um número n não passar pelo teste, n com certeza é um número composto (ou seja, não-primo).
#Numeros primos são numeros que são só divisiveis por 1 e ele mesmo!
    def teste_miller_rabin(self,n, k=150):
#excessao para uma regra entre os numeros do 0 ao 6 os numeros 2,3,5 entra como excessão a regra!
        if n < 6:
            return [False, False, True, True, False, True][n]
        if n <= 1 or n % 2 == 0:
            return False
        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
# O operador // é conhecido como floor division pois retorna apenas a parte inteira da divisão entre os numeros
            r = r // 2
        for _ in range(1, k):
#Dentro da biblioteca random temos uma função chamada randrange para gerar numeros inteiros entra 2 e n!
            a = randrange(2, n)
#A função pow é uma função q utiliza parametros para executar uma formula Ex: pow(4,3,5):
#Retorne o valor de 4 à potência de 3, módulo(O resto da divisão) por 5 (o mesmo que (4 * 4 * 4) % 5):
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True
#length = comprimento
    def tentativa_de_numero(self,length):
#getrandbits = Retorna um número inteiro Python com bits aleatórios k. 
#logo getrandbits(length) é o comprimento do bit aleatorio k
        self.numero_primo = getrandbits(length)
        self.numero_primo = self.numero_primo | (1 << length - 1) | 1
        return self.numero_primo
    def gerar_numero_primo(self,length=5):
        self.numero_primo  = 4
        while not self.teste_miller_rabin(self.numero_primo, 150):
            self.numero_primo  = self.tentativa_de_numero(length)
        return self.numero_primo 