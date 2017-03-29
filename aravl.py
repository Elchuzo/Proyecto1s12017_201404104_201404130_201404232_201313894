#import commands
class hoja(object):
        """docstring for hoja del arbol avl"""
        def __init__(self, dato):
                self.dato =dato
                self.izquierda = None
                self.derecha= None
                self.fe = 0

class rotaciones (object):
        """docstring for rotaciones ; clase encargada de hacer el equilibrios y las rotaciones"""
        def __init__(self, hola):
                self.hola = hola


        def derder(self, n, n1):
                #rotacion derecha derecha
                n.derecha = n1.izquierda
                n1.izquierda = n
                n = n1
                return n

        def izqizq(self, n, n1):
                #rotacion izquierda izquierda
                n.izquierda = n1.derecha
                n1.derecha = n
                n = n1
                return n

        def rderizq(self, n, n1):
                #rotacion derecha izquierda
                n2 = n1.izquierda
                n.derecha = n2.izquierda
                n2.izquierda = n
                n1.izquierda = n2.derecha
                n2.derecha = n1
                n = n2
                return n

        def rizqder(self, n, n1):
                #rotacion izquierda derecha
                #n2 = hoja() #si no funcina quitar la instancia

                n2 = n1.derecha
                n.izquierda = n2.derecha

                n2.derecha = n
                n1.derecha = n2.izquierda
                n2.izquierda = n1
                n = n2
                return n


        def altura(self, raiz):

                if raiz == None:

                        return int(0)
                else:
                        #con esto se verifica si se rompe el factor de equilibrio
                        return int (1) + int(max(self.altura(raiz.izquierda), self.altura(raiz.derecha)))

        def equilibrar(self , raiz):

                if raiz == None:
                        raiz.izquierda = self.equilibrar(raiz.izquierda)
                        raiz.derecha = self.equilibrar (raiz.derecha)
                        tamder = self.altura (raiz.derecha)
                        tamizq = self.altura (raiz.izquierda)
                        fe = int(tamder)- int (tamizq)

                        if int(fe)> int(1) or int (fe)< int(-1):
                                #aca se verifica si se perdio el quilibrio y se empiezan hacer las respectivas rotaciones segun los algoritmos

                                if int(fe)> int(1):
                                        td = self.altura(raiz.derecha.derecha)
                                        ti = self.altura (raiz.derecha.izquierda)
                                        f = int(td) - int(ti) #se calculan si los hijos estan en desequilibrio
                                        if int(f) > int(0):
                                                raiz = self.derder (raiz,raiz.derecha)
                                        else :
                                                raiz = self.rderizq( raiz, raiz.derecha)

                        elif int (fe) < int (-1):

                                td = self.altura( raiz.izquierda.derecha)
                                ti = self.altura (raiz.izquierda.izquierda)
                                f = int(td)- int(ti)
                                if int(f)< int(0):
                                        raiz = self.izqizq(raiz, raiz.izquierda)
                                else :
                                        raiz = self.rizqder(raiz, raiz.izquierda)

                return raiz

class avl(object):
        """docstring for avl estructura del arbol avl"""
        def __init__(self):
                self.raiz = None
                self.balance = rotaciones('s')



        def insertar(self, dato):
                hijo = hoja(dato)
                self.raiz = self.add(hijo, self.raiz)
                self.raiz = self.balance.equilibrar(self.raiz)

        def add(self,hijo, raiz):

                if raiz == None:
                        raiz = hijo
                        return raiz

                if raiz.dato == hijo.dato:
                        #no pasa nada porque los datos son iguales; no se si pasar todo a string o dejarlo asi
                        pass
                if raiz.dato > hijo.dato:
                        raiz.izquierda = self.add(hijo, raiz.izquierda)
                else:
                        raiz.derecha = self.add(hijo, raiz.derecha)

                return raiz

        def preorden(self,raiz):
                a = ''
                if (raiz is not None):
                        print(str(raiz.dato))
                        a = a + raiz.dato + ","
                        self.preorden(raiz.izquierda)
                        self.preorden(raiz.derecha)
                return a.rstrip(",")

        def buscar(self,raiz,dato):
                if raiz == None:

                        return None
                elif raiz.dato == dato:
                        return raiz

                elif raiz.dato > dato:
                        return self.buscar(raiz.izquierda,dato)

                else:
                        return self.buscar(raiz.derecha , dato)

        def obtener(self,raiz, dato):

                return self.buscar(raiz, dato)

        def eliminar(self, dato):

                self.raiz = self.el(dato, self.raiz)
                self.raiz = self.balance.equilibrar(raiz)

        def el(self, dato, nodo):

                if nodo == None:

                        return None
                if nodo.dato == dato:

                        return self.juntar(nodo.izquierda, nodo.derecha)

                if nodo.dato > dato:

                        nodo.izquierda = self.el(dato, nodo.izquierda)

                else:

                        nodo.derecha = self.el(dato, nodo.derecha)

                return nodo

        def juntar(self, izq, der):

                if izq == None:
                        return der

                if der== None:
                        return izq

                mitad = self.juntar(izq.derecha, der.izquierda)
                izq.derecha = mitad
                der.izquierda = izq
                return der

        def graficar(self):
                archi= open('avl.dot','w')
                archi.write('digraph AVL{ \n')
                archi.write('node[shape=record]\n')
                self.ghojas(archi, self.raiz)
                self.enlazes(archi, self.raiz)
                archi.write('} \n')
                archi.close()
                print ('se genero el.dot del arbol')
                #commands.getoutput('dot -Tpng avl.dot -o avl.png')
                #commands.getoutput('xdg-open avl.png')

        def ghojas(self, archi, raiz):
                if raiz != None:
                        archi.write(str(raiz.dato)+'[label="<f0>|<f1> '+str(raiz.dato)+'  |<f2>"]; \n')
                        self.ghojas(archi, raiz.izquierda)
                        self.ghojas(archi, raiz.derecha)


        def enlazes(self, archi, raiz):
                if raiz != None:
                        if raiz.izquierda!= None:
                                archi.write(str(raiz.dato)+':f0->'+str(raiz.izquierda.dato)+' \n')
                        if raiz.derecha !=None:
                                archi.write(str(raiz.dato)+ ':f2->'+str(raiz.derecha.dato)+ '\n')
                        self.enlazes(archi, raiz.izquierda)
                        self.enlazes(archi, raiz.derecha)

       #poner un contador para que no se repitan las hojas?


'''
arbol = avl()
arbol.insertar('hola')
arbol.insertar('vato')
arbol.insertar('cuando')
arbol.insertar('mano')
arbol.insertar('comida')
arbol.insertar('pollofrito')
arbol.insertar('china')
arbol.insertar('arroz')
arbol.insertar('juan')
arbol.insertar('tacos')
arbol.preorden(arbol.raiz)
arbol.graficar()'''
