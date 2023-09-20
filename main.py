print(">>> Bem vindo ao sistema Bancário <<<")

programa_ativo = True

while programa_ativo == True:
  print("\n### Menu ###")
  print("0 - Sair")
  numero_operacao = input("Selecione a operação que deseja realizar:\n>>> ")

  if numero_operacao == "0":
    print("\nSistema encerrado.")
    programa_ativo = False

  else:
    print("\nOperação invalida.")