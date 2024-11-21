from Banco import Banco
from ContaCliente import ContaCliente
from ContaComum import ContaComum
from ContaRemunerada import ContaRemunerada

banco1 = Banco(999,"teste")
contacliente1 = ContaCliente (1,0.01,0.1,2000,0.05)
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaremunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adiciona_conta(contacliente1) #(4)
print(f'Conta Cliente 1 adicionada!')
banco1.adiciona_conta(contacomum1) #(5)
print(f'Conta comum 1 adicionada!')
banco1.adiciona_conta(contaremunerada1) #(6)
print(f'Conta Remunerada 1 adicionada!')

print(f'Conta comum 1 adicionada!')
print(f"Cliente: {contacomum1.numero} possui saldo R$ {contacomum1.valor_investido}")
print(f'.......................')
banco1.calcular_rendimento_mensal()#(7)
print(f'O saldo das contas é:')
banco1.imprime_saldo_contas() #(8)imprime_saldo_contas


