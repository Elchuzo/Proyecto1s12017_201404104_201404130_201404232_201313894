
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
<meta charset="utf-8">
    <title>Iniciar Sesión</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="generator" content="Codeply">



    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" />
    <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet" />
    <link href="//cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.1/animate.min.css" rel="stylesheet" />

    <link rel="stylesheet" href="css/styles.css" />
  </head>
  <body >

<section id="section4">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h1 class="text-center">Iniciar Sesión</h1>
                <hr>
            </div>
        </div>
        <form action="Inicial.jsp">
            <% 
                if(false)
            {
                
            }
                %>
        <div class="row">
            <div class="col-sm-9">
                <div class="row form-group">
                    <div class="col-sm-6">
                        <input type="text" class="form-control" id="Usuario" name="Usuario" placeholder="Usuario" value="${usuario}">
                    </div>
                </div>
                <div class="row form-group">
                    <div class="col-sm-6">
                        <input type="password" class="form-control" id="Contraseña" name="Contraseña" placeholder="Contraseña">
                    </div>
                </div>
                <div class="row form-group">
                    <div class="col-sm-6">
                        <input type="text" class="form-control" id="Empresa" name="Empresa" placeholder="Empresa">
                    </div>
                </div>
                 <div class="row form-group">
                    <div class="col-sm-6">
                        <input type="text" class="form-control" id="Departamento" name="Departamento" placeholder="Departamento">
                    </div>
                </div>
                <div class="row form-group">
                    <div class="col-sm-6">
                        <button class="btn btn-default btn-lg pull-left">Iniciar Sesión</button>
                    </div>
                </div>
            </div>
        </div>
        <br>
        </form>
        
        <form action="Registro.jsp">
        <button class="btn btn-default btn-lg pull-left">Registrar Usuario</button>
        </form>
        
    </div>
</section>

    <!--scripts loaded here-->
    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <script src="js/scripts.js"></script>
  </body>
</html>
