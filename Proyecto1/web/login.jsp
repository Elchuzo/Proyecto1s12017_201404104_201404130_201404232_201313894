<%@page import = "Paquete.Conexion"  %>
<%
    Conexion con = new Conexion();
    String nickname = request.getParameter("usuario");
    String contrasena = request.getParameter("contrasena");
    String empresa = request.getParameter("empresa");
    String departamento = request.getParameter("departamento");
    if (con.logUsuario(nickname, contrasena, empresa, departamento)) {
        session.setAttribute("nickname", nickname);
        //out.println("welcome " + userid);
        //out.println("<a href='logout.jsp'>Log out</a>");
       response.sendRedirect("success.jsp");
      
    } else {
        out.println("Contraseña incorrecta <a href='Inicial.jsp'> intentelo de nuevo</a>");
    }
%>