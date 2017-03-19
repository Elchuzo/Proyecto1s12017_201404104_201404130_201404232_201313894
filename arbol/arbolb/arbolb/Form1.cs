using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace arbolb
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            arbol d = new arbol();
            for (int x = 0; x < 20; x++) {
                d.insertar(ref d.raiz, new claves(x));
            }
        
            var prueba = (1 <= 5 / 2) ? 5 / 2 : 5 / 2 + 1;
            var encontrado = (3 == 2);
            MessageBox.Show(encontrado.ToString());
        }
    }
}
