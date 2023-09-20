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

def listar_contas():
  if len(contas) == 0:
    print('\nNão há contas cadastradas.')
  else:
    index = 1
    for conta_em_consulta in contas:
      if conta_em_consulta['saldo_conta'] >= 0:
        status = 'Positivo'
      else:
        status = 'Negativo'
      # format string - f string
      print(f"{index} - Número da conta: {conta_em_consulta['numero_conta']} | Saldo da conta: R$ {conta_em_consulta['saldo_conta']:.2f} ({status})")
      index += 1

print(">>> Bem vindo ao sistema Bancário <<<")

while True:
  print("\n### Menu ###")
  print("0 - Sair")
  print("1 - Criar uma nova conta")
  print("2 - Remover uma conta")
  print("3 - Listar todas as contas")
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

  # Operação 3 - Listar todas as contas
  elif numero_operacao == "3":
    listar_contas()

  # Operação inválida
  else:
    print("\nOperação invalida.")