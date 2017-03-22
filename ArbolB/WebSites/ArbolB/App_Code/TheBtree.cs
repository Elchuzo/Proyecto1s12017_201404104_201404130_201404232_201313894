using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

/// <summary>
/// Summary description for TheBtree
/// </summary>
public class TheBtree
{
    Pagina pag;
    Pagina derecha = new Pagina();
    Pagina izquierda = new Pagina();

    Nodo aux;
    Pagina page;
    bool esta = false;
    bool emp = false;

    public TheBtree()
    {
        
    }

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
}