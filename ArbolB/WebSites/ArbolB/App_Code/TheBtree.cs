using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

/// <summary>
/// Summary description for TheBtree
/// </summary>
public class TheBtree
{
    Pagina pag;     //p
    Pagina derecha = new Pagina();
    Pagina izquierda = new Pagina();

    Nodo aux;  //X
    Pagina page;   //Xr
    bool esta = false;
    bool emp = false;

    public TheBtree()
    {
        
    }

    //INSERTANDO
    public bool Vacio(Pagina raiz) {
        return (raiz == null || raiz.Cuenta == 0);
    }

    public void Insertando(Nodo clave) {
        Insertar(pag, clave);
    }

    public void Insertar(Pagina raiz, Nodo clave) {
        Empujar(raiz, clave);
        if (emp) {
            pag = new Pagina();
            pag.Cuenta = 1;
            pag.Claves[0] = aux;
            pag.Ramas[0] = raiz;
            pag.Ramas[1] = page;
        }
    }

    public void Empujar(Pagina raiz, Nodo clave) {
        int k = 0;
        esta = false;
        if (Vacio(raiz))
        {
            emp = true;
            aux = clave;
            page = null;
        }
        else {
            k = BuscarNodo(raiz, clave);
            if (esta)
            {
                emp = false;
            }
            else {
                Empujar(raiz.Ramas[k], clave);
                if (emp) {
                    if (raiz.Cuenta < 4) {
                        emp = false;
                        MeterHoja(raiz, aux, k);
                    }
                    else {
                        emp = true;
                        Dividir(raiz, aux, k);
                    }
                }
            }
        }
    }

    public int BuscarNodo(Pagina raiz, Nodo clave) {
        int i = 0;
        if (clave.Num < raiz.Claves[0].Num)
        {
            esta = false;
            i = 0;
        }
        else {
            i = raiz.Cuenta;
            while (clave.Num < raiz.Claves[i-1].Num && i>1) {
                --i;
            }
            esta = (clave.Num == raiz.Claves[i - 1].Num);
        }
        return i;
    }

    public void MeterHoja(Pagina raiz, Nodo clave, int k) {
        int i = raiz.Cuenta;
        //desplazar a la derecha los elementos
        while (i != k) {
            raiz.Claves[i] = raiz.Claves[i - 1];
            raiz.Ramas[i + 1] = raiz.Ramas[i];
            --i;
        }
        raiz.Claves[k] = clave;
        raiz.Ramas[k + 1] = page;
        raiz.Cuenta = ++raiz.Cuenta;
    }

    public void Dividir(Pagina raiz, Nodo clave, int k) {
        int i = 0;
        int mediana = 0;
        if (k <= 2)
        {
            mediana = 2;
        }
        else {
            mediana = 3;
        }
        Pagina Posmdna = new Pagina();
        i = mediana + 1;
        while (i != 5) {     //buscando la mediana
            Posmdna.Claves[(i - mediana) - 1] = raiz.Claves[i - 1];
            Posmdna.Ramas[i - mediana] = raiz.Ramas[i];
            ++i;
        }
        Posmdna.Cuenta = 4 - mediana;
        raiz.Cuenta = mediana;
        if (k <= 2)
        {
            MeterHoja(raiz, clave, k);
        }
        else {
            MeterHoja(Posmdna, clave, (k-mediana));
        }
        aux = raiz.Claves[raiz.Cuenta - 1];
        Posmdna.Ramas[0] = raiz.Ramas[raiz.Cuenta];
        raiz.Cuenta = --raiz.Cuenta;
        page = Posmdna;

    }
    //ELIMINANDO
    public void Eliminando(Nodo clave) {
        if (Vacio(pag))
        {
            //No hay elementos en la lista
        }
        else {
            Eliminar(pag, clave);
        }
    }

    public void Eliminar(Pagina raiz, Nodo clave) {
        try
        {
            EliminarRegistro(raiz, clave);
        }
        catch (Exception e)
        {
            esta = false;
        }
        if (!esta) {
            Console.Write("No se encontro el elemento");
        }else
        {
            if (raiz.Cuenta == 0) {
                raiz = raiz.Ramas[0];
            }
            pag = raiz;
            Console.Write("Eliminacion completa");
        }
    }

    public void EliminarRegistro(Pagina raiz, Nodo clave) {
        int pos = 0;
        if (Vacio(raiz))
            esta = false;
        else
        {
            pos = BuscarNodo(raiz, clave);
            if (esta)
            {
                if (Vacio(raiz.Ramas[pos - 1]))
                    Quitar(raiz, pos);
                else
                {
                    Sucesor(raiz, pos);
                    EliminarRegistro(raiz.Ramas[pos], raiz.Claves[pos - 1]);
                }
            }
            else
            {
                EliminarRegistro(raiz.Ramas[pos], clave);
                if ((raiz.Ramas[pos] != null) && (raiz.Ramas[pos].Cuenta < 2))
                    Restablecer(raiz, pos);
            }
        }


    }

    public void Sucesor(Pagina raiz, int k) {
        Pagina aux = raiz.Ramas[k];
        while (!Vacio(aux.Ramas[0]))
            aux = aux.Ramas[0];
        raiz.Claves[k - 1] = aux.Claves[0];
    }

    public void Restablecer(Pagina raiz, int posicion) {
        if (posicion > 0)
        {
            if (raiz.Ramas[posicion - 1].Cuenta > 2)
                MoverDerecha(raiz, posicion);
            else
                Combina(raiz, posicion);
        }
        else
        {
            if (raiz.Ramas[1].Cuenta > 2)
                MoverIzquierda(raiz, 1);
            else
                Combina(raiz, 1);
        }
    }

    public void MoverDerecha(Pagina raiz, int posicion) {
        int i = raiz.Ramas[posicion].Cuenta;
        while (i!=0) {
            raiz.Ramas[posicion].Claves[i] = raiz.Ramas[posicion].Claves[i -1];
            raiz.Ramas[posicion].Ramas[i + 1] = raiz.Ramas[posicion].Ramas[i];
            --i;
        }
        raiz.Ramas[posicion].Cuenta++;
        raiz.Ramas[posicion].Ramas[1] = raiz.Ramas[posicion].Ramas[0];
        raiz.Ramas[posicion].Claves[0] = raiz.Claves[posicion - 1];
        raiz.Claves[posicion - 1] = raiz.Ramas[posicion - 1].Claves[raiz.Ramas[posicion - 1].Cuenta - 1];
        raiz.Ramas[posicion].Ramas[0] = raiz.Ramas[posicion - 1].Ramas[raiz.Ramas[posicion - 1].Cuenta];
        raiz.Ramas[posicion - 1].Cuenta--;
    }

    public void MoverIzquierda(Pagina raiz, int posicion) {
        int i;
        raiz.Ramas[posicion - 1].Cuenta++;
        raiz.Ramas[posicion - 1].Claves[raiz.Ramas[posicion - 1].Cuenta - 1] = raiz.Claves[posicion - 1];
        raiz.Ramas[posicion - 1].Ramas[raiz.Ramas[posicion - 1].Cuenta] = raiz.Ramas[posicion].Ramas[0];
        raiz.Claves[posicion - 1] = raiz.Ramas[posicion].Claves[0];
        raiz.Ramas[posicion].Ramas[0] = raiz.Ramas[posicion].Ramas[1];
        raiz.Ramas[posicion].Cuenta--;
        i = 1;
        while (i != raiz.Ramas[posicion].Cuenta + 1)
        {
            raiz.Ramas[posicion].Claves[i - 1] = raiz.Ramas[posicion].Claves[i];
            raiz.Ramas[posicion].Ramas[i] = raiz.Ramas[posicion].Ramas[i + 1];
            i++;
        }
    }


    public void Combina(Pagina raiz, int posicion) {
        int j;
        derecha = raiz.Ramas[posicion];
        izquierda = raiz.Ramas[posicion - 1];
        izquierda.Cuenta++;
        izquierda.Claves[izquierda.Cuenta - 1] = raiz.Claves[posicion - 1];
        izquierda.Ramas[izquierda.Cuenta] = derecha.Ramas[0];
        j = 1;
        while (j != derecha.Cuenta + 1)
        {
            izquierda.Cuenta++;
            izquierda.Claves[izquierda.Cuenta - 1] = derecha.Claves[j - 1];
            izquierda.Ramas[izquierda.Cuenta] = derecha.Ramas[j];
            j++;
        }
        Quitar(raiz, posicion);

    }

    public void Quitar(Pagina raiz, int posicion) {
        int i = posicion + 1;
        while (i != raiz.Cuenta + 1)
        {
            raiz.Claves[i - 2] = raiz.Claves[i - 1];
            raiz.Ramas[i - 1] = raiz.Ramas[i];
            i++;
        }
        raiz.Cuenta--;
    }

    public void ListarCreciente(Pagina actual) {
       
    }

    public void Graficar() {
        System.IO.StreamWriter archivo = null;
        String contenido;
        try
        {
            archivo = new System.IO.StreamWriter("C:\\Users\\Dinora\\Desktop\\arbolB.txt");


        }
        catch (Exception e)
        {
            Console.WriteLine("Error al escribir en el archivo arbolB.txt" +e);
        }
        finally {
            try
            {
                if (null != archivo) {
                    archivo.Close();
                }
            }
            catch (Exception e2) {
                Console.Write("Error al cerrrar el archivo arbolB.txt" + e2);
            }
        }
        try
        {
            System.Diagnostics.Process.Start("C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe -Tpng C:\\Users\\Dinora\\Desktop\\arbolB.txt C:\\Users\\Dinora\\Desktop\\arbolB.txt -o C:\\Users\\Dinora\\Desktop\\Btree.png");
        }
        catch (Exception ex) {
            Console.Write("Error al generar la imagen para el arbol" + ex);
        }
    }


} 