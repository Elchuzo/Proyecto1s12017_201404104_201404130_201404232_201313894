using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace arbolb
{
    class pagina
    {
        public int m;
        public claves[] clave;
        public pagina[] ramas;
        public int cuenta;

        public pagina() {
            this.m = 5;
            this.clave = new claves[m];
            this.ramas = new pagina[m];
            this.cuenta = 0;

        }

        public bool nodolleno(pagina actual) {

            return actual.cuenta == m -1;
        }

        public  bool nodosemivacillo(pagina actual)
        {
            return actual.cuenta < (m / 2);

        }
        public void escribenodo(pagina actual){
            Console.WriteLine(" Nodo:");
            for (int k = 1; k <= actual.cuenta; k++) {
                Console.WriteLine(actual.clave[k]);

            }

         }

        
    }
}
