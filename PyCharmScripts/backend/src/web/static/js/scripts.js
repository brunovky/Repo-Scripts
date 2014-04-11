function salvarUsuario() {

}

function logar() {
    var msg;
    $('.required').each(function() {
       if ($(this).val() == '') {
           msg = msg + $(this).prev().text() + '\n';
       }
    });
    if (msg != undefined) {

    }
}
