$(document).ready(function(){
    $('#formlogin').on('submit',function(event){
        $('#error').text("").show();
        $('#error').css("transition", "all 500ms ease");
        $.ajax({
                data:{
                    correo: $('#correo').val(),
                    contraseña: $('#contraseña').val()
            },
            type: 'POST',
            url: '/login'
        })
        .done(function(data){
            if(data.error ==  "1"){
                $('#error').html(`<div class="alert alert-danger" id="borrar" role="alert">
                Correo no registrado
              </div>`);
              $('#contraseña').val("")
              $('#correo').val("")
               // $('#error').text("Contraseña o usuario incorrecto").show();
                //$('#error').css("background-color", "rgba(255, 18, 18, 0.5)");
               // $('#error').css("padding", "10px");
                //$('#error').css("margin", "15px");
              //  $('#error').css("border-radius", "5px");
                //$('#error').css("transition", "all 500ms ease");
                $('.alert').css("transition", "all 500ms ease");
               
            }
            else if(data.error == "2"){
                $('#error').html(`<div class="alert alert-danger" id="borrar" role="alert">
                Contraseña incorrecta
              </div>`);
           
              $('#contraseña').val("")
               // $('#error').text("Contraseña o usuario incorrecto").show();
                //$('#error').css("background-color", "rgba(255, 18, 18, 0.5)");
               // $('#error').css("padding", "10px");
                //$('#error').css("margin", "15px");
              //  $('#error').css("border-radius", "5px");
                //$('#error').css("transition", "all 500ms ease");
                $('.alert').css("transition", "all 500ms ease");
            }
            
            else{
                $(location).attr('href', '/dashboard')
            }
        });
        event.preventDefault();
    });
});

$(document).ready(function() {
    $("#borrar").click(function(event) {
        $("#error").remove();
    });
});

$(document).ready(function() {
    
    $('#BtnIniciar').click(function(event){
        $('#correo').val(""),
        $('#contraseña').val("")
        $('#error').html(``);
        $('#errorRegistro').html(``);
    });
});