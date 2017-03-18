import commands
import aravl
from flask import Flask, request, Response
class nododisperso(object):
    """docstring for nododisperso; nodo de la matriz"""
    def __init__(self, x,y,dato):
        self.x = x
        self.y = y
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        self.arriba= None
        self.abajo = None
        self.arbol = aravl.avl()




class listaHo(object):
    """Lista horizontal donde van insertados los nodos de la matriz dispersa"""
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tam = 0

    def insertar(self, elemento):
        self.tam = 0
        if self.primero == None:
            
            self.primero = elemento
            self.ultimo = elemento
        
        elif elemento.x < self.primero.x :
            
            self.primero.anterior = elemento
            elemento.siguiente = self.primero
            self.primero = self.primero.anterior
            
        elif elemento.x > self.ultimo.x :
            
            self.ultimo.siguiente = elemento
            elemento.anterior = self.ultimo
            self.ultimo = self.ultimo.siguiente
            elemento.siguiente = None
            
        else :
            
            temp1 = self.primero
            
            while temp1.x < elemento.x:
                
                temp1 = temp1.siguiente
                
            temp2 = temp1.anterior
            
            temp2.siguiente = elemento
            temp1.anterior = elemento
            elemento.siguiente = temp1
            elemento.anterior = temp2
        self.tam=self.tam+1

    def recorrer(self):
        temporal = self.primero
        #recorrer lista horizontal de los nodos dispersos
        while temporal != None:   
            temporal = temporal.siguiente

class listaVe():
    
    def __init__(self):
        
        self.tam = 0
        self.primero= None
        self.ultimo= None
        
    
    def insertar(self, elemento):
        
        if self.primero == None:
            
            self.primero = elemento
            self.ultimo = elemento
        
        elif elemento.y < self.primero.y :
            
            self.primero.arriba = elemento
            elemento.abajo = self.primero
            self.primero = self.primero.arriba
            
        elif elemento.y > self.ultimo.y :
            
            self.ultimo.abajo = elemento
            elemento.arriba = self.ultimo
            self.ultimo = self.ultimo.abajo
            elemento.abajo = None
            
        else :
            
            temp1 = self.primero
            
            while temp1.y < elemento.y:
                
                temp1 = temp1.abajo
                
            temp2 = temp1.arriba
            
            temp2.abajo = elemento
            temp1.arriba = elemento
            elemento.abajo = temp1
            elemento.arriba = temp2
        self.tam=self.tam+1
            
            
    def recorrer(self):
        
        temporal = self.primero
        #recorrer lista horizontal de los nodos dispersos
        while temporal != None:
            
            temporal = temporal.abajo


#cabeceras xxxxxxxxxxxxxxxxxxxxxxxxxxx

class nodox():
    
    def __init__(self, x):
        self.x = x
        self.listav = listaVe()
        self.siguiente = None
        self.anterior = None
        
class nodoy():
    
    def __init__(self, y):        
        self.y = y
        self.listah = listaHo()
        self.arriba = None
        self.abajo = None

#Lista de cabeceras del eje X
class listax():
    

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tam  =0
    
    def insertar(self, elemento):
        
        if self.primero == None:
            
            self.primero = elemento
            self.ultimo = elemento
        
        elif elemento.x < self.primero.x :
            
            self.primero.anterior = elemento
            elemento.siguiente = self.primero
            self.primero = self.primero.anterior
            
        elif elemento.x > self.ultimo.x :
            
            self.ultimo.siguiente = elemento
            elemento.anterior = self.ultimo
            self.ultimo = self.ultimo.siguiente
            elemento.siguiente = None
            
        else :
            
            temp1 = self.primero
            
            while temp1.x < elemento.x:
                
                temp1 = temp1.siguiente
                
            temp2 = temp1.anterior
            
            temp2.siguiente = elemento
            temp1.anterior = elemento
            elemento.siguiente = temp1
            elemento.anterior = temp2

        self.tam= self.tam+1
            
            
    def recorrer(self):
        
        temporal = self.primero
        #recorrer cabeceras x
        while temporal != None:
            
            temporal = temporal.siguiente
            
            
    def existe(self,x):
        
        if self.primero == None:
            return None
        else:
            temporal = self.primero
            
            while temporal != None :
                
                if temporal.x == x :
                    return temporal
                
                temporal = temporal.siguiente
        return None

#Lista de cabeceras del lado Y eje vertical
class listay():
    
    def __init__(self):
        
        self.primero= None
        self.ultimo= None
        self.tam=0
        
    
    def insertar(self, elemento):
        
        if self.primero == None:
            
            self.primero = elemento
            self.ultimo = elemento
        
        elif elemento.y < self.primero.y :
            
            self.primero.arriba = elemento
            elemento.abajo = self.primero
            self.primero = self.primero.arriba
            
        elif elemento.y > self.ultimo.y :
            
            self.ultimo.abajo = elemento
            elemento.arriba = self.ultimo
            self.ultimo = self.ultimo.abajo
            elemento.abajo = None
            
        else :
            
            temp1 = self.primero
            
            while temp1.y < elemento.y:
                
                temp1 = temp1.abajo
                
            temp2 = temp1.arriba
            
            temp2.abajo = elemento
            temp1.arriba = elemento
            elemento.abajo = temp1
            elemento.arriba = temp2

        self.tam = self.tam +1
            
            
    def recorrer(self):
        
        temporal = self.primero
        while temporal != None:
            print temporal.y
            temporal = temporal.abajo

    def existe(self,y):
        
        if self.primero == None:
            return None
        else:
            temporal = self.primero
            
            while temporal != None :
                
                if temporal.y == y :
                    return temporal
                
                temporal = temporal.abajo
        return None


#-------------- Matriz

class matriz(object):
    """docstring for matriz dispersa"""
    def __init__(self):
        self.ladox= listax()
        self.ladoy= listay()
        
    def verificar(self, x, y):
        nodoyy = self.ladoy.primero
        
        while nodoyy != None:
            temporal = nodoyy.listah.primero
            
            while temporal != None:
                if temporal.x == x and temporal.y == y:
                    return temporal
                        
                temporal = temporal.siguiente
                
            nodoyy = nodoyy.abajo
            
         
        return None

    def insertar(self,x,y,dato):
       
       #si existe no deberia de insertar nada
        if self.verificar(x,y) == None:
            
            cuadro = self.ladox.existe(x)
            if self.ladox.existe(x) == None:
                
                self.ladox.insertar(nodox(x))
           
            if self.ladoy.existe(y)== None:
                
                self.ladoy.insertar(nodoy(y))
                
            temx = self.ladox.existe(x)
            temy = self.ladoy.existe(y)
           
            elemento = nododisperso(x,y,dato)
            
            temx.listav.insertar(elemento)
            temy.listah.insertar(elemento)
            return elemento

    def recorrer(self):

        temp= self.ladoy.primero

        while temp != None :


            temp2= temp.listah.primero
            while temp2!= None:
                print temp2.dato
                print temp2.x               
                temp2 = temp2.siguiente


            temp=temp.abajo

    def graficar(self):
        #metodo de graficar


        archi=open('matri.dot','w')


        archi.write('digraph matriz {\n')
        archi.write('rankdir=UD;\n')       
        archi.write('node [shape=box]; \n \n')

        archi.write('{ \n')
        archi.write('rank=min; \n')
        archi.write('m[label= "matriz"]; \n')

        temporal = self.ladox.primero

        while temporal != None:
            archi.write('nodex'+ str(temporal.x)+ '[label="'+str(temporal.x)+ '",rankdir=LR]; \n')
            temporal = temporal.siguiente

        archi.write('\n}\n')

        temporaly = self.ladoy.primero

        while  temporaly != None:
            archi.write('\n{\n')
            archi.write('rank=same; \n')
            archi.write('nodey'+ str(temporaly.y)+ '[label="'+ str(temporaly.y) + '"]; \n')
            nodoaux = temporaly.listah.primero #graficar los nodos de las listas

            while  nodoaux != None: 
                archi.write('noded'+str(nodoaux.x)+'g'+str(nodoaux.y)+str(nodoaux.dato)+ '[label= "' +str(nodoaux.dato)+ '"]; \n')
                nodoaux = nodoaux.siguiente


            archi.write('\n}')    
            temporaly= temporaly.abajo



        tempx = self.ladox.primero #falta verificar si vienen nulos
        tempy = self.ladoy.primero

        archi.write('\nm')
        contador = 0
        while tempx!= None :
            contador=contador+1
            archi.write('->nodex'+str(tempx.x))
            tempx =tempx.siguiente

        archi.write('; \n')

        temp2=self.ladox.ultimo
        while contador > 0:
            
            if contador > 1:

                archi.write('nodex'+str(temp2.x)+'->')
            else :

                archi.write('nodex'+ str(temp2.x))


            temp2=temp2.anterior
            contador=contador -1


        archi.write(';\n')
        archi.write('m->nodey'+str(tempy.y)+';\n') #verificar si vienen nulos si no no hacer nada de esto

        while tempy!= None:
            
            if tempy.abajo != None:
                archi.write('nodey'+ str(tempy.y)+'->nodey'+str(tempy.abajo.y)+ '[rankdir=UD dir="both"]; \n')

            tempy= tempy.abajo

        #enlazes de y internos

        tempx = self.ladox.primero

        while tempx != None:

            nauxiar = tempx.listav.primero
            archi.write('nodex'+ str(tempx.x))

            while nauxiar != None:
                
                archi.write('->noded'+str(nauxiar.x)+'g'+str(nauxiar.y)+str(nauxiar.dato))
                nauxiar= nauxiar.abajo

            archi.write('[dir="both"];\n')
            tempx = tempx.siguiente


        #enlazeinternos de y-----------------------------------------------------

        

        temporaly= self.ladoy.primero
        while temporaly != None:
            if temporaly.listah.primero != None and temporaly != None :

                xi= temporaly.listah.primero.x
                yi =temporaly.listah.primero.y
                info = temporaly.listah.primero.dato


                archi.write('nodey'+str(temporaly.y)+'->noded'+str(xi)+'g'+str(yi)+ str (info)+'[constraint=false]; \n')
                archi.write('noded'+ str(xi)+'g'+str(yi)+str(info)+'->nodey'+str(temporaly.y)+'[constraint=false]; \n')

            nodoaux = temporaly.listah.primero

            while nodoaux != None:
                if nodoaux.siguiente != None :

                    archi.write('noded'+ str(nodoaux.x)+'g'+str(nodoaux.y) + str(nodoaux.dato)+'->noded'+str(nodoaux.siguiente.x) + 'g'+str(nodoaux.siguiente.y)+ str(nodoaux.siguiente.dato)+str(1)+'[constraint=false,dir="both"];')

                nodoaux = nodoaux.siguiente

                

            temporaly = temporaly.abajo


        archi.write('\n}') #-----------------------------findel archivo


        archi.close()
        print("gmatri")
        commands.getoutput('dot -Tpng matri.dot -o matri.png')
        commands.getoutput('xdg-open matri.png')


mat = matriz()
mat.insertar(1,21,"dato1")
mat.insertar(88,32,"dato2")
mat.insertar(5,11,"dato3")
mat.insertar(9,5,"dato4")
arbol = aravl.avl()
arbol.insertar('se')
arbol.insertar('vato')
arbol.insertar('cuando')
arbol.insertar('mano')
arbol.insertar('comida')
arbol.insertar('pollofrito')
arbol.insertar('fads')
arbol.insertar('rdfasd')
arbol.insertar('juan')
arbol.insertar('tacos')
arbol.preorden(arbol.raiz)
arbol.graficar()

mat.recorrer()
mat.graficar()
 


    









        







            
            

        

        
            


        













        
        