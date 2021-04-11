class Pilha:
# DECLARANDO O CONSTRUTOR
    def __init__(self):
        self.__valores = []        
        self.__TamMax = 1000
        self.__topo = -1                                # Quando é iniciada ela está vazia, começa com -1

# (c) DECLARAÇÃO DO MÉTODO EMPTY
    def isEmpty(self):
        if(self.__topo == -1):                          # Se topo for igual a -1 então a pilha está vazia, caso contrário...
            print("A pilha está vazia!")
        else:
            print("A pilha não está vazia!")
    
# (d) DECLARAÇÃO DO MÉTODO PUSH
    def Push(self,valor):
        if( len(self.__valores) <= self.__TamMax):      # Verificação importante, caso o valor da pilha seja maior que o tamanho máximo, não será possível inserir.
            self.__valores.append(valor)                # Adicionando o elemento no fim da pilha.
            self.__topo = len(self.__valores) - 1       # Garante que sempre terá o index do último elemento.            
        else:            
            print("A pilha está lotada!")    

# (e) DECLARAÇÃO DO MÉTODO POP
    def Pop(self):
        if (self.__topo > -1):
            self.__valores.pop()                        # Removendo o último elemento da pilha.
            self.__topo = len(self.__valores) - 1       # Topo sempre terá o index para o último elemento.  

# (f) VARIAÇÃO DO MÉTODO POP DENOMINADO SUPERPOP. IRÁ REMOVER A QUANTIDADE X DE ELEMENTOS DA PILHA.
    def superPop(self, total):
        total = int(total)                              # Fazendo o type cast só pra garantir que vai ser um número passado, ainda que por string.        
        if (total > self.__topo):                       # Caso seja passado um valor maior do que a quantidade de elemento da pilha...
            total = self.__topo                         # ...Total recebe a quantidade máxima de elementos da pilha.

        while(total > 0 ):
            self.Pop()
            total = total - 1

# (g) DECLARAÇÃO DO MÉTODO TOP, QUE RETORNA O VALOR DO TOPO DA PILHA SEM MODIFICÁ-LA.
    def Top(self):
        return self.__valores[-1]
     
# Representar o objeto Pilha como uma string, daí, quando der print em uma pilha...
    def __repr__(self):
        return str ("Sua Pilha: ") + str(self.__valores)
