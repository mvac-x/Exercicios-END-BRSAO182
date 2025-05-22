senha = input("Digite a senha ou sair: ")




def verificarSenha(senha):
    #tamnho da senha
    if len(senha) < 8:
        print("Senha muito curta")
        return False

    #se tem numero 
    if not any(char.isdigit() for char in senha):
        return False
    return True
