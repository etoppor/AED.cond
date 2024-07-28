from Apartamento import Apartamento

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        
    def add(self, ap):
        if self.inicio == None:
            self.inicio = ap
        else:
            if ap.vaga < self.inicio.vaga:
                ap.proximo = self.inicio
                self.inicio = ap
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux != None :
                    if ap.vaga < aux.vaga:
                        ap.proximo = ant.proximo   
                        ant.proximo = ap
                        break
                    else: 
                        ant = aux
                        aux = aux.proximo
                if aux == None and ap.vaga >= ant.vaga:
                    ant.proximo = ap
                    
        self.tamanho += 1
        self.imprimir()
                            
    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            print("Lista de Apartamentos")
            aux = self.inicio
            while aux :
                print( aux )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))
            
    def remover(self, vaga):
        tamAtual = self.tamanho
        if self.inicio == None:
            print("Lista Vazia")
            
           
        elif self.inicio.proximo == None and self.inicio.vaga == vaga:
            self.inicio = None
            self.tamanho = 0
        else:
            if self.inicio.vaga == vaga:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1   
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux :
                    if aux.vaga == vaga:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
        if tamAtual == self.tamanho:
            print("Valor não encontrado")
        self.imprimir()
                
                
            