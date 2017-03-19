using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace arbolb
{
    class arbol
    {
        public pagina raiz;

        public arbol()
        {
            this.raiz = null;

        }

        int buscarnodo(ref pagina actual, ref claves clave, ref int k) {
            int econtrado;
            // k posicion

            if (clave.clave < actual.clave[1].clave)
            {
                econtrado = 0;
                k = 0;
                return econtrado;

            }
            else {

                k = actual.cuenta;
                while ((clave.clave < actual.clave[k].clave) && (k > 1)) {

                    k--;
                }
                if (clave.clave == actual.clave[k].clave) {
                    econtrado = 1;
                    return econtrado;
                }
            }


            return -1;
        }

        pagina buscar(ref pagina actual, ref claves clv, ref int indice) {
            if (actual == null)
            {

                return null;
            }
            else {
                int esta;
                esta = buscarnodo(ref actual, ref clv, ref indice);
                if (esta == 1)
                {
                    return actual;
                }
                else {
                    return buscar(ref actual.ramas[indice], ref clv, ref indice);
                }
            }



        }

        public void insertar(ref pagina raiz, claves cl) {
            int subearriba=0;
            claves mediana = null;
            pagina p, nd=null;

            empuar(ref raiz, cl, ref subearriba,ref mediana, nd);

            if (subearriba == 1) {
                p = new pagina();

                p.cuenta = 1;
                p.clave[1] = mediana;
                p.ramas[0] = raiz;
                p.ramas[1] = nd;
                raiz = p;
                

            }


        }

        public void empuar(ref pagina actual, claves cl, ref int subearriba, ref claves mediana, pagina nuevo) {
            int k=0;
            if (actual == null)
            {
                subearriba = 1;
                mediana = cl;
                nuevo = null;
            }
            else {

                int esta;
                esta = buscarnodo(ref actual,ref  cl,ref  k);
                if (esta == 1) {
                    Console.WriteLine("clave dupblicada");
                    subearriba = 0;
                    return;
                }

                empuar(ref actual.ramas[k], cl, ref subearriba,ref mediana, nuevo);

                if (subearriba == 1) {

                    if (actual.nodolleno(actual))
                    {
                        dividrNodo(ref actual, mediana, ref nuevo, k, ref mediana, ref nuevo);
                    }
                    else {

                         subearriba = 0;
                         meterhoja(actual, mediana, ref nuevo, k);
                        
                    }
                }
            }
        }

        public void meterhoja(pagina actual, claves cl,ref  pagina rd, int k) {
            int i;
            for ( i = actual.cuenta; i >= k + 1 ; i--){
                actual.clave[i + 1] = actual.clave[i];
                actual.ramas[i + 1] = actual.ramas[i];


            }
            actual.clave[k + 1] = cl;
            actual.ramas[i + 1] = rd;
            actual.cuenta++;
           

        }

        public void dividrNodo(ref pagina actual, claves cl, ref pagina rd, int k, ref claves mediana, ref pagina nuevo) {
            int i;
           

            var posmedia = (k <= 5 / 2) ? 5 / 2 : 5 / 2 + 1;

            nuevo = new pagina();
            for (i = posmedia + 1; i < 5; i++) {
                nuevo.clave[i - posmedia] = actual.clave[i];
                nuevo.ramas[i - posmedia] = actual.ramas[i];
            }
            nuevo.cuenta = (5 - 1) - posmedia;
            actual.cuenta = posmedia;

            if (k <= 5 / 2)
            {
                meterhoja(actual, cl, ref rd, k);
            }
            else {
                meterhoja(nuevo, cl, ref rd, k - posmedia);
            }
            mediana = actual.clave[actual.cuenta];
            nuevo.ramas[0] = actual.ramas[actual.cuenta];
            actual.cuenta--;


            }

        }
    }

