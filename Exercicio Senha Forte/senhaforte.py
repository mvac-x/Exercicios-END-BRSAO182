
def verificarSenha(senha):
    #tamnho da senha
    if len(senha) < 8:
        print("Senha muito curta")
        return False
    #se tem numero 
    if not any(char.isdigit() for char in senha):
        return False
    #se tem letra 
    elif not any(char.isalpha() for char in senha):
        print("Senha deve conter letras")
        return False
    return True

while True:
    senha = input("Digite a senha ou sair: ")

    if senha == "sair":
        print("Saindo...")
        break

    if verificarSenha(senha):
        print("Senha valida")
        break

    else:
        print("Senha invalida")        
