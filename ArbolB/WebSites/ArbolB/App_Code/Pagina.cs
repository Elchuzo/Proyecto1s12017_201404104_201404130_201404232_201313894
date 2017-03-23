using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

/// <summary>
/// Summary description for Pagina
/// </summary>
public class Pagina
{
    Pagina[] ramas = new Pagina[5];
    Nodo[] claves = new Nodo[4];
    int cuenta = 0;

    public Pagina(Nodo clave)
    {
        Claves[0] = clave;
    }

    public Pagina() {
    }

    public Pagina[] Ramas
    {
        get
        {
            return ramas;
        }

        set
        {
            ramas = value;
        }
    }

    public Nodo[] Claves
    {
        get
        {
            return claves;
        }

        set
        {
            claves = value;
        }
    }

    public int Cuenta
    {
        get
        {
            return cuenta;
        }

        set
        {
            cuenta = value;
        }
    }
}