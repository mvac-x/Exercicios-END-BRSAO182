lista_alunos = ['Ana', 'Bruno', 'Carlos', 'Marcus', 'Zacarias']
indice = 0

def ler_nota(nome, ordem):
    while True:
        entrada = input(f"Digite a {ordem} nota de {nome} ou escreva SAIR para finalizar: ")
        if entrada.strip().upper() == 'SAIR':
            return 'SAIR'
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

while indice < len(lista_alunos):
    nome = lista_alunos[indice]

    nota1 = ler_nota(nome, "primeira")
    if nota1 == 'SAIR':
        break

    nota2 = ler_nota(nome, "segunda")
    if nota2 == 'SAIR':
        break

    media = (nota1 + nota2) / 2

    if media < 7:
        print(f" {nome} está reprovado com média {media:.2f}.")
    else:
        print(f" {nome} está aprovado com média {media:.2f}.")

    indice += 1