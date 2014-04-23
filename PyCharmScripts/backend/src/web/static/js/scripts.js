function salvarProduto() {
    if (!verificarErros()) {
        $.ajax({
            url: '/rest/crud/salvar_produto',
            type: 'POST',
            data: $('#form_produto').serialize(),
            success: function() {
                alert('Produto cadastrado com sucesso')
                window.location.href = '/rest/crud/cadastrar_produto'
            }
        })
    }
}

function verificarErros() {
    var msg = ''
    $('.required').each(function() {
        if ($(this).val() == '') {
            var labelText = $(this).prev().text()
            msg = msg + labelText.substr(0, labelText.length - 1) + ' é obrigatório. <p />'
        }
    })
    if (msg != '') {
        $('.view').removeClass('hide')
        $('#msg_error').html(msg)
        return true
    }
    return false
}