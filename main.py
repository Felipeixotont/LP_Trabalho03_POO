from Modules.mod import Pilha

# (h) CRIANDO UMA CLASSE PRINCIPAL E CRIANDO UMA PILHA DENTRO DO MÉTODO MAIN.
class Principal:
    minhaPilha = []

    def main(self):
        self.minhaPilha = Pilha()

        for i in range(1,4):                                # INSERINDO OS VALORES 10, 20 E 30 POR UM LOOP SIMPLES
            self.minhaPilha.Push(i*10)

        self.minhaPilha.superPop(2)
        print('O topo da sua pilha é: '+ str(self.minhaPilha.Top()))
        print(self.minhaPilha)


teste = Principal()
teste.main()