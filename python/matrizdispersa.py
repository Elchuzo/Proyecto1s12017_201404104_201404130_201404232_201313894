#import commands
import aravl
from flask import Flask, request, Response
app = Flask("Proyecto1")
class nododisperso(object):
    """docstring for nododisperso; nodo de la matriz"""
    def __init__(self, x,y,nombre, nombreusuario, contrasena):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.nombreusuario = nombreusuario
        self.contrasena = contrasena
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
            print (temporal.y)
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

    def verificar(self, x, y): #verifica si existe un nodo en la matriz
        nodoyy = self.ladoy.primero

        while nodoyy != None:
            temporal = nodoyy.listah.primero

            while temporal != None:
                if temporal.x == x and temporal.y == y:
                    return temporal

                temporal = temporal.siguiente

            nodoyy = nodoyy.abajo

        return None

    def insertar(self,x,y,nombre, nombreusuario, contrasena):

       #si existe no deberia de insertar nada
        if self.verificar(x,y) == None:

            cuadro = self.ladox.existe(x)
            if self.ladox.existe(x) == None:

                self.ladox.insertar(nodox(x))

            if self.ladoy.existe(y)== None:

                self.ladoy.insertar(nodoy(y))

            temx = self.ladox.existe(x)
            temy = self.ladoy.existe(y)

            elemento = nododisperso(x,y,nombre, nombreusuario, contrasena)


            temx.listav.insertar(elemento)
            temy.listah.insertar(elemento)

            return elemento

    def recorrer(self): #recorre la matriz -->>>>>>>>>>>>>>ESTEEE RECORRE LA MATRIZ
        temp= self.ladoy.primero
        while temp != None :
            temp2= temp.listah.primero
            while temp2!= None:
                print (temp2.nombre)
                print (temp2.x)
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
                archi.write('noded'+str(nodoaux.x)+'g'+str(nodoaux.y)+str(nodoaux.nombre)+ '[label= "' +str(nodoaux.nombre)+ '"]; \n')
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

                archi.write('->noded'+str(nauxiar.x)+'g'+str(nauxiar.y)+str(nauxiar.nombre))
                nauxiar= nauxiar.abajo

            archi.write('[dir="both"];\n')
            tempx = tempx.siguiente


        #enlazeinternos de y-----------------------------------------------------



        temporaly= self.ladoy.primero
        while temporaly != None:
            if temporaly.listah.primero != None and temporaly != None :

                xi= temporaly.listah.primero.x
                yi =temporaly.listah.primero.y
                info = temporaly.listah.primero.nombre


                archi.write('nodey'+str(temporaly.y)+'->noded'+str(xi)+'g'+str(yi)+ str (info)+'[constraint=false]; \n')
                archi.write('noded'+ str(xi)+'g'+str(yi)+str(info)+'->nodey'+str(temporaly.y)+'[constraint=false]; \n')

            nodoaux = temporaly.listah.primero

            while nodoaux != None:
                if nodoaux.siguiente != None :

                    archi.write('noded'+ str(nodoaux.x)+'g'+str(nodoaux.y) + str(nodoaux.nombre)+'->noded'+str(nodoaux.siguiente.x) + 'g'+str(nodoaux.siguiente.y)+ str(nodoaux.siguiente.nombre)+str(1)+'[constraint=false,dir="both"];')

                nodoaux = nodoaux.siguiente



            temporaly = temporaly.abajo


        archi.write('\n}') #-----------------------------findel archivo


        archi.close()
        print("gmatri")
        #commands.getoutput('dot -Tpng matri.dot -o matri.png')
        #commands.getoutput('xdg-open matri.png')

    def buscarpornombre(self, nombreusuario): #busca los usuarios por su nombre
        nodoyy = self.ladoy.primero

        while nodoyy != None:
            temporal = nodoyy.listah.primero

            while temporal != None:
                if temporal.nombreusuario == nombreusuario:
                    return temporal

                temporal = temporal.siguiente

            nodoyy = nodoyy.abajo

    def insertaractivos(self, nombreusuario, idactivo, nombreactivo, descripactivo): #insertar los activos en el avl

        nodo = self.buscarpornombre (nombreusuario)
        if nodo!= None:
            nodo.arbol.insertar(idactivo, nombreusuario, descripactivo)
            #nodo.arbol.graficar()

    def eliminaractivo(self, nombreusuario, idactivo): #elimina los activos del avl
        nodo = self.buscarpornombre(nombreusuario)
        if nodo!= None:
            nodo.arbol.eliminar(idactivo)

            nodo.arbol.graficar()

    def modificaractivo(self, nombreusuario, idactivo, nuevadescripcion): #modifica la descripcion de los activos del avl
        nodo = self.buscarpornombre(nombreusuario)
        if nodo!= None:
            activo = nodo.arbol.obtener(nodo.arbol.raiz,idactivo)

            if activo != None:
                activo.descripcion = nuevadescripcion

        nodo.arbol.graficar()

    def obtenerdatosdellog(self): #obtiene los datos para el inicio de secion

        nodoyy = self.ladoy.primero
        superstring=str('')

        while nodoyy != None:
            temporal = nodoyy.listah.primero

            while temporal != None:

                superstring=str(superstring)+str(temporal.nombreusuario)+','+str(temporal.contrasena)+','+str(temporal.x)+','+str(temporal.y)+','
                temporal = temporal.siguiente

            nodoyy = nodoyy.abajo



        return str(superstring.rstrip(','))



        #x es el las empresas
        #y los departamentos

    def verificarlog(self, usuario, contrasena, empresa , departamentos): #verifica si el log es correcto

        nodo = self.buscarpornombre(usuario) #si existe el nodo con ese id verifico los demas datos
        if nodo!= None:
            if nodo.contrasena== contrasena and nodo.x == empresa and nodo.y== departamentos:
                return 'true'

        return 'false'



mat = matriz()
#x,y, nombre, nombreusuario, contrasena
mat.insertar('conta','meso',"dato1", "queso", "2")
mat.insertar('telefono','banrural','nombre','id','20')
mat.insertar('banco','claro',"dato4","queso","3")

mat.insertaractivos('queso',"nuebo",'nombre', 'descripcion1')
mat.insertaractivos('queso',"maje",'nombre', 'descripcion2')
mat.insertaractivos('queso',"orga",'nombre', 'descripcion3')
mat.insertaractivos('queso',"lala",'nombre', 'descripcion4')
mat.insertaractivos('queso',"lalao",'nombre', 'descripcion5')
mat.insertaractivos('queso',"lalai",'nombre', 'descripcion6')
mat.insertaractivos('queso',"lalaf",'nombre', 'descripcion7')

mat.insertaractivos('queso',"orga1",'nombre', 'descripcion8')
mat.insertaractivos('queso',"orga10",'nombre', 'descripcion9')
mat.insertaractivos('queso',"orga3",'nombre', 'descripcion10')
mat.modificaractivo('queso','orga','esta es una nueva describcion')
mat.graficar()

print(str(mat.verificarlog('queso','3','banco','claro')))

@app.route('/usuario/login',methods=['POST']) #Metodo para login o registrar usuario
def iniciar():
    nickname = str(request.form['nickname'])
    contrasena = str(request.form['contrasena'])
    nombre = str(request.form['nombre'])
    empresa = str(request.form['empresa'])
    departamento = str(request.form['departamento'])
    operacion = str(request.form['operacion'])
    if(operacion=="crear"):
        mat.insertar(empresa,departamento,nombre,nickname,contrasena)
        print("usuario creado")
        return "usuario creado"
    else:
        if(mat.obtenerdatosdellog(nickname,contrasena, empresa, departamento)):
            print("else1")
            return "login correcto"
        else:
            print("else2")
            return "datos invalidos"
    mat.graficar()
@app.route('/usuario/operaciones/aniadir',methods=['POST']) #Metodo para añadir activos
def aniadir():
    usuario = str.request.form['nickname']
    nombreactivo = str.request.form['nombreactivo']
    #operacion = str(request.form['operacion'])
    mat.insertaractivos(usuario, idactivo, nombre, descripcion)

@app.route('/usuario/operaciones/eliminar',methods=['POST']) #Metodo para eliminar activos
def eliminar():
    usuario = str.request.form['nickname']
    idactivo = str.request.form['idactivo']
    #operacion = str(request.form['operacion'])
    mat.eliminaractivo(nombre, idactivo)

@app.route('/usuario/operaciones/activos',methods=['POST']) #Metodo para obtener los activos a mostrar en el combobox
def activos():
    usuario = str.request.form['nickname']
    obj = mat.buscarpornombre(usuario)
    cadena = obj.arbol.preorden
    return cadena
    #operacion = str(request.form['operacion'])

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
