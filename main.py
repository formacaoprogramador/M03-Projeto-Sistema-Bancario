contas = []

def criar_conta():
  verificador_conta_existe = False
  dados_nova_conta = {}
  dados_nova_conta['numero_conta'] = input('Digite o número da nova conta:\n>>> ')

  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == dados_nova_conta['numero_conta']:
      verificador_conta_existe = True
      break

  if verificador_conta_existe == True:
    print('\nO número da conta já existe. Tente novamente.')
  else:
    dados_nova_conta['saldo_conta'] = float(input('Digite o saldo da nova conta:\n>>> '))
    contas.append(dados_nova_conta)
    print('\nOperação efetuada com sucesso.')

def remover_conta():
  numero_conta = input('Digite o número da conta para remover:\n>>> ')
  conta_encontrada = False
  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      conta_encontrada = True
      contas.remove(conta_em_consulta)
      print('\nOperação efetuada com sucesso.')
      break
  if not conta_encontrada:
    print('\nO número da conta não existe. Tente novamente.')

print(">>> Bem vindo ao sistema Bancário <<<")

while True:
  print("\n### Menu ###")
  print("0 - Sair")
  print("1 - Criar uma nova conta")
  print("2 - Remover uma conta")
  numero_operacao = input("Selecione a operação que deseja realizar:\n>>> ")

  if numero_operacao == "0":
    print("\nSistema encerrado.")
    break

  # Operação 1 - Criar uma nova conta
  elif numero_operacao == "1":
    criar_conta()

  # Operação 2 - Remover uma conta
  elif numero_operacao == "2":
    remover_conta()

  # Operação inválida
  else:
    print("\nOperação invalida.")