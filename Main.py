from Torre import Torre
from Apartamento import Apartamento
from Fila import Fila
from Lista import Lista

def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar Apartamento na Fila")
    print("2. Remover Apartamento da Fila e Adicionar na Lista")
    print("3. Imprimir Lista de Apartamentos")
    print("4. Imprimir Fila de Espera")
    print("5. Sair")

def main():
    t1 = Torre("Torre A", "Rua A, 100")
    t2 = Torre("Torre B", "Rua B, 200")

    ap1 = Apartamento("1-A", t1)
    ap2 = Apartamento("2-A", t1)
    ap3 = Apartamento("1-B", t2)
    ap4 = Apartamento("3-A", t1)
    ap5 = Apartamento("2-B", t2)

    semVagas = Fila()
    apsComVaga = Lista()

    semVagas.add(ap1)
    semVagas.add(ap2)
    semVagas.add(ap3)
    semVagas.add(ap4)
    semVagas.add(ap5)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            num = input("Número do apartamento: ")
            torre_nome = input("Nome da torre: ")
            torre = next((t for t in [t1, t2] if t.nome == torre_nome), None)
            if torre:
                apartamento = Apartamento(num, torre)
                semVagas.add(apartamento)
            else:
                print("Torre não encontrada!")

        elif opcao == "2":
            pos = int(input("Digite a posição do apartamento a ser removido da fila: "))
            ap = semVagas.remover(pos)
            if ap:
                apsComVaga.add(ap)

        elif opcao == "3":
            apsComVaga.imprimir()

        elif opcao == "4":
            semVagas.imprimir()

        elif opcao == "5":
            print("Saindo...")
            break

if __name__ == "__main__":
    mostrar_menu()
    main()