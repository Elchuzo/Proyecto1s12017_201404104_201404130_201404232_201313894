<%@page import = "Paquete.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nickname = request.getParameter("usuario");
    String contrasena = request.getParameter("contrasena");
    String nombre = request.getParameter("nombre");
    String empresa = request.getParameter("empresa");
    String departamento = request.getParameter("departamento");
    
    if (con.crearUsuario(nickname, contrasena, nombre, empresa, departamento)){

        response.sendRedirect("exito.jsp");
    } else {
        out.println("Invalid password <a href='index.jsp'>try again</a>");
    }
%>