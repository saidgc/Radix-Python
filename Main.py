import sys

class Nodo:
    def __init__(self):
        self.dato = 0
        self.Apabajo = None
        self.Apderec = None

    def getDato(self):
        return self.dato

    def getApabajo(self):
        return self.Apabajo

    def getApderec(self):
        return self.Apderec

    def setApabajo(self, Apabajo):
        self.Apabajo = Apabajo

    def setDato(self, nuevoDato):
        self.dato = nuevoDato

    def setApderec(self, Apderec):
        self.Apderec = Apderec


class Lista:
    def __init__(self):
        self.inicio = None
        self.tamano = 0

    def esVacia(self):
        return self.inicio == None

    def getTamanio(self):
        return self.tamano

    def agregarAlFinal(self, valor):
        nuevo = Nodo()
        nuevo.setDato(valor)
        if self.esVacia():
            self.inicio = nuevo
        else:
            aux = self.inicio
            while aux.getApabajo() is not None:
                aux = aux.getApabajo()
            aux.setApabajo(nuevo)
        self.tamano += 1

    def insrtarPorPosicion(self, pos, val):
        nuevo = Nodo()
        nuevo.setDato(val)
        aux = self.inicio
        for i in range(pos):
            aux = aux.getApabajo()
        while aux.getApderec() is not None:
            aux = aux.getApderec()
        aux.setApderec(nuevo)

    def getValor(self, pos):
        if pos >= 0 and pos < self.tamano:
            if pos == 0:
                return self.inicio.getDato()
            else:
                aux = self.inicio
                for i in range(pos):
                    aux = aux.getApabajo()
                return aux.getDato()
        else:
            print("No existe posicion")

    def eliminar(self):
        self.inicio = None
        self.tamano = 0

    def listar(self):
        aux = self.inicio
        i = 0
        while aux is not None:
            aux2 = aux
            print(aux.getDato())
            while i is aux.getDato() and aux2.getApderec() is not None:
                aux2 = aux2.getApderec()
                print("\t" + str(aux.getDato()))
            aux = aux.getApabajo()
            i += 1

    def transfier(self):
        nueva = Lista()
        aux = self.inicio
        if not self.esVacia():
            while aux is not None:
                aux2 = aux
                while aux2.getApderec() is not None:
                    aux2 = aux2.getApderec()
                    nueva.agregarAlFinal(aux2.getDato())
                aux = aux.getApabajo()
        return nueva

    def imprimir(self):
        if not self.esVacia():
            aux = self.inicio
            while aux is not None:
                sys.stdout.write(aux.getDato()+"-> ")
                aux = aux.getApabajo()
        sys.stdout.write("null\n")
        sys.stdout.flush()


def ini(lista):
  for y in range(10):
    lista.agregarAlFinal(y)
    
    
def getdgt(num, pos):
    i = 1
    while num > 0:
        x = num % 10
        if i == pos: return x
        num = num / 10
        i = i + 1
    return 0


if __name__ == '__main__':
    maxi = 0
    print("Deme la lista de numeros")
    numeros = Lista()
    lista = Lista()
    ini(lista)
    cadena = input()
    for nm in cadena.split(" "):
        numeros.agregarAlFinal(nm)
        if maxi < len(nm): maxi = len(nm)
    print("Lista de numeros")
    numeros.imprimir()
    for i in range(1,maxi+1):
        for j in range(numeros.getTamanio()):
            num = numeros.getValor(j)
            a = getdgt(int(num), i)
            lista.insrtarPorPosicion(int(a), num)
        numeros = lista.transfier()
        print("lista simple nueva")
        numeros.imprimir()
        lista.eliminar()
        ini(lista)
