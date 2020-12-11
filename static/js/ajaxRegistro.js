$(document).ready(function(){
    $('#formregistro').on('submit',function(event){
        $.ajax({
                data:{
                    nombre: $('#nombrer').val(),
                    apellido: $('#apellidor').val(),
                    nombreUsuario: $('#usuarior').val(),
                    correo: $('#correor').val(),
                    fecha: $('#fechar').val(),
                    contraseña: $('#contraseñar').val() 
            },
            type: 'POST',
            url: '/crearusuario'
        })
        .done(function(data){
            if(data.error == "1"){
                $('#errorRegistro').html(`<div class="alert alert-danger" id="borrar" role="alert">
                El correo ya se encuentra registrado
                </div>`);
                $('#correor').val("");
            }
            else if(data.error == "2"){
                $('#errorRegistro').html(`<div class="alert alert-danger" id="borrar" role="alert">
                El nombre de usario ya se encuentra en uso
                </div>`);
                $('#usuarior').val("");
                
            }
            
            else{
              
                $('#nombrer').val("");
                $('#apellidor').val("");
                $('#correor').val("");
                $('#usuarior').val("");
                $('#fechar').val("");
                $('#contraseñar').val("");
                swal("Exito", "Registrado Correctamente, revisa tu correo electronico", "success",{
                    button : false
                  });
            }
        });
        event.preventDefault();
    });
});
$(document).ready(function() {
    
    $('#BtnRegistro').click(function(event){
        console.log("elimino")
        $('#nombrer').val("");
                $('#apellidor').val("");
                $('#correor').val("");
                $('#usuarior').val("");
                $('#fechar').val("");
                $('#contraseñar').val("");
                $('#errorRegistro').html(``);
                $('#error').html(``);
                
    });

    
});