$('#btn-index').click(function() {
    window.open('https://www.mercadolibre.cl/alimento-leonardo-kitten-para-gato-de-temprana-edad-sabor-mix-en-bolsa-de-75kg/p/MLC17496696?pdp_filters=item_id:MLC946834578#searchVariation=MLC17496696&position=5&search_layout=stack&type=pad&tracking_id=13e8267d-ee1a-4a03-a161-e98636a82c1f');
    return false;
});

$('#btn-contac').click(function resetform() {
    let nombre = $('#fname').val();
    let apellido = $('#lname').val();
    let message = $('#message').val();
    if (nombre.length < 3) {
        alert('El nombre debe tener minimo 3 caracterres y es obligatorio');
        return false;
    }
    if (apellido.length < 3) {
        alert('El apellido debe tener minimo 3 caracterres y es obligatorio');
        return false;
    }
    if ($("#email").val().indexOf('@', 0) == -1 || $("#email").val().indexOf('.', 0) == -1) {
        alert('El correo electrónico introducido no es correcto.');
        return false;
    }
    if (message.length < 10) {
        alert('La descipcion debe tener minimo 10 caracterres y es obligatorio');
        return false;
    }
    alert('Sus datos se han guardado conrrectamente');
    $("form input[type=text] , form textarea").each(function() { this.value = '' });
});