from Gerar_primo import Gerador_Numero_primo
from Gerar_chave import chaves
from Criptografia import criptografia

# p ganha o valor de um Numero Primo
p = Gerador_Numero_primo()
#ele entra como um objeto e se transforma em um iteravel
numero_p = p.numero_primo
print('\n P :',str(numero_p))
# q ganha o valor de um Numero Primo
q = Gerador_Numero_primo()
#ele entra como um objeto e se transforma em um iteravel
numero_q = q.numero_primo
print('\n Q :',str(numero_q))
#chave ganha o valor de chaves(q e p)
chave = chaves(numero_p, numero_q)
#aqui ele gera as chaves publica e privada
chave.Gerar_chaves()
#chave ganha o valor de criptografia
encripta = chave.encripta_mensagem()
#encriptação de mensagens e descriptografar  
chave.decripta_mensagem(encripta)