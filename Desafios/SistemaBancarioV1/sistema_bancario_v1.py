menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha a opcao: 

"""

saldo = 0
limite_valor_saque = 500
qtd_saques = 3
extrato = ""

while True:
  opcao = input(menu)

  if opcao == "d":
    print("Depósito")
    valor = float(input("Valor: "))
    
    if valor < 0:
      print("Valor inválido!") 
      
    else:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
      print(f"Saldo atual: R$ {saldo:.2f}")

  elif opcao == "s":
    print("Saque")
    valor = float(input("Valor: "))
    
    if valor < 0: print("Valor inválido!") 
      
    elif valor <= 500:
      
      if valor > saldo: print("Saldo insuficiente!")
        
      elif qtd_saques <= 0:
        print("Quantidade de saques atingida!")
        print("Somente 3 saques máximos diários.")
        
      else:
        saldo -= valor
        qtd_saques -= 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Quantidade de saques restantes: {qtd_saques}")
        
    else: print("Saque máximo de R$ 500,00.")

  elif opcao == "e":
    print("Extrato")
    
    if extrato == "": print("Não houve nenhuma transação nessa conta até agora.")
    else: print(extrato)

  elif opcao == "q": break

  else: print("Opção inválida!")
