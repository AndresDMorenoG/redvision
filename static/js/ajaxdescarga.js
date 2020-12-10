$(document).ready(function(){
    $('#formlogin').on('submit',function(event){
        $('#error').text("").show();
        $('#error').css("transition", "all 500ms ease");
        $.ajax({
                data:{
                    enlace: '/static/imagenes/4.jpg'
            },
            type: 'POST',
            url: '/descargaImg'
        })
        .done(function(response){
            callback(response)
        });
        event.preventDefault();
    });
});