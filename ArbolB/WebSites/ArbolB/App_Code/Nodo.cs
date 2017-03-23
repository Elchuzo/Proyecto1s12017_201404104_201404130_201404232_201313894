using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

/// <summary>
/// Summary description for Nodo
/// </summary>
public class Nodo
{
    int num;
    public Nodo(int valor)
    {
        Num = valor;
    }

    public int Num
    {
        get
        {
            return num;
        }

        set
        {
            num = value;
        }
    }
}