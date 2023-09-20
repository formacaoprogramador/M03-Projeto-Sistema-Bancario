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

def adicionar_saldo_em_conta():
  numero_conta = input('Digite o número da conta:\n>>> ')
  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      valor_credito = float(input('Digite o valor do crédito:\n>>> R$ '))
      if valor_credito < 0:
        print('\nValores negativos não são aceitos. Tente novamente.')
        return
      else:
        conta_em_consulta['saldo_conta'] += valor_credito
        print('\nOperação efetuada com sucesso.')
        return
  print('\nO número da conta não foi encontrado. Tente novamente.')

def remover_saldo_em_conta():
  numero_conta = input('Digite o número da conta:\n>>> ')
  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      valor_debito = float(input('Digite o valor do débito:\n>>> R$ '))
      if valor_debito < 0:
        print('\nValores negativos não são aceitos. Tente novamente.')
        return
      else:
        conta_em_consulta['saldo_conta'] -= valor_debito
        print('\nOperação efetuada com sucesso.')
        return
  print('\nO número da conta não foi encontrado. Tente novamente.')

def transferir_saldo_entre_contas():
  conta_partida = input('Digite o número da sua conta:\n>>> ')
  verificador_etapa = 0
  # Procura a primeira conta
  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == conta_partida:
      verificador_etapa = 1
      conta_destino = input('Digite o número da conta destino:\n>>> ')
      # Verifica se é uma transferencia para a mesma conta
      if conta_destino != conta_partida:
        # Procura a segunda conta
        for conta_destino_em_consulta in contas:
          if conta_destino_em_consulta['numero_conta'] == conta_destino:
            verificador_etapa = 3
            valor_transferencia = float(input('Digite o valor da transferência:\n>>> R$ '))
            # Verifica se o valor é negativo
            if valor_transferencia < 0:
              print('\nNão é possível transferir um valor negativo.')
              break
            # Verifica se o saldo é suficiente
            elif valor_transferencia > conta_em_consulta['saldo_conta']:
              print('\nNão é possível transferir um valor maior que o seu saldo.')
              break
            else:
              conta_em_consulta['saldo_conta'] -= valor_transferencia
              conta_destino_em_consulta['saldo_conta'] += valor_transferencia
              print('\nOperação efetuada com sucesso.')
              break

        print()
      else:
        verificador_etapa = 2
        break

  if verificador_etapa == 0:
    print('\nA sua conta não foi encontrada. Tente novamente.')
  elif verificador_etapa == 1:
    print('\nA conta de destino não foi encontrada. Tente novamente.')
  elif verificador_etapa == 2:
    print('\nNão é possível transferir dinheiro para a mesma conta.')

def consultar_saldo_de_conta():
  numero_conta = input('Digite o número da conta para consultar o saldo:\n>>> ')
  for conta_em_consulta in contas:
    if conta_em_consulta['numero_conta'] == numero_conta:
      if conta_em_consulta['saldo_conta'] >= 0:
        status = 'Positivo'
      else:
        status = 'Negativo'
      print(f"\nO saldo é: R$ {conta_em_consulta['saldo_conta']:.2f} ({status})")
      return
  print('\nO número da conta não foi encontrado. Tente novamente.')

print(">>> Bem vindo ao sistema Bancário <<<")

while True:
  print("\n### Menu ###")
  print("0 - Sair")
  print("1 - Criar uma nova conta")
  print("2 - Remover uma conta")
  print("3 - Listar todas as contas")
  print("4 - Adicionar saldo (creditar)")
  print("5 - Remover saldo (debitar)")
  print("6 - Transferir valor entre contas")
  print("7 - Consultar saldo de uma conta")
  numero_operacao = input('Selecione a operação que deseja realizar:\n>>> ')

  if numero_operacao == "0":
    print('\nSistema encerrado.')
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

  # Operação 4 - Adicionar saldo
  elif numero_operacao == "4":
    adicionar_saldo_em_conta()

  # Operação 5 - Remover saldo
  elif numero_operacao == "5":
    remover_saldo_em_conta()

  # Operação 6 - Transferir valor entre contas
  elif numero_operacao == "6":
    transferir_saldo_entre_contas()

  # Operação 7 - Consultar saldo de uma conta
  elif numero_operacao == "7":
    consultar_saldo_de_conta()

  # Operação inválida
  else:
    print('\nOperação inválida.')