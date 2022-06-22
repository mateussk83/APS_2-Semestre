class criptografia(object):
#Função para cifrar uma mensagem m: m = c mod(n)
    def criptografia(self, m, e, n):
        c = (m**e) % n
        return c
#Função para decifrar uma mensagem c: c mod(n)
    def descriptografia(self, c, d, n):
        m = c**d % n
        return m
    def encripta_mensagem(self):
        s = input("Digite a sua Mensagem: \n")
#como precisavamos de um metodo para utilizar uma variavel local para verificar se
#os dados estavam correto utilizamos um arquivo.txt e em outra
#função puxamos os dados arquivo.txt
        arquivo = open('APS.txt','w')
        arquivo.write(s)
        arquivo.close()
        print('='*20 + ' Digite as chaves públicas: ' + '='*20)
        e = int(input("Chave e: \n"))
        n = int(input("Chave n: \n")) 
#aqui utilizamos a função criptografar para criptografar a mensagem 
        texto_cifrado = ''.join(chr(self.criptografia(ord(x), e, n)) for x in s)
        print("Mensagem Criptografada: {0}\n".format(texto_cifrado))       
        return texto_cifrado    
    def decripta_mensagem(self, s):
        self.s = s
        print('='*20 + ' Digite as chaves privadas: ' + '='*20)
        d = int(input("Chave d: \t"))
        n = int(input("Chave n: \t"))
#aqui utilizamos a função descriptografar para descriptografar a mensagem
        texto = ''.join(chr(self.descriptografia(ord(x), d, n)) for x in s)
        arquivo = open('APS.txt', 'r')
#aqui usamos o arquivo aps.txt para pegar a variavel da função de cima
        for linha in arquivo:
            texto_certo = linha
        arquivo.close()
#aqui verificamos se as chaves estao corretas imprimos na tela oq esta em cima
#se estiverem incorretas aparece a informação que estaoo no bloco else!
        if texto_certo == texto: 
            print("! ATENÇÃO!")
            print("! Área de extrema segurança !")
            return print("Mensagem descriptografada: {0}\n".format(texto))
        else:   
            print("! informação bloqueada área inacessível!")
            return print("!POR QUESTAO DE SEGURANÇA AFASTAR SE A 10 QUILOMETROS!")
