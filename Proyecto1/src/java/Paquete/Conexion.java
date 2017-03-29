package Paquete;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import com.opencsv.*;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;
import java.util.logging.Level;

public class Conexion {
    public static OkHttpClient webClient = new OkHttpClient();

    public String getActivos() throws FileNotFoundException, IOException {
        String nombre = "Marco";
        RequestBody formBody = new FormEncodingBuilder()
                .add("dato", nombre)
                .add("dato2", "4")
                .build();
        String r = getString("/usuario/operaciones/activos", formBody);
        CSVReader lector = new CSVReader(new FileReader(r));
        List valores = lector.readAll();
        return null; //cambiar
    }
    
    public boolean logUsuario(String nickname, String contraseña,String nombre, String empresa) throws FileNotFoundException, IOException {
        RequestBody formBody = new FormEncodingBuilder()
                .add("nickname", nickname)
                .add("contraseña",contraseña)
                .add("nombre",nombre)
                .add("empresa",empresa)
                .build();
        String r = getString("/usuario/login", formBody);
        if (r.equals("login correcto"))
        {
         return true;   
        }
        else
        {
         return false;
        }
    }
 
     public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Paquete.Conexion.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Paquete.Conexion.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
