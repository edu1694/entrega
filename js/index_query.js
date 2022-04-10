$('#btn-index').click(function() {
    window.open('https://www.mercadolibre.cl/alimento-leonardo-kitten-para-gato-de-temprana-edad-sabor-mix-en-bolsa-de-75kg/p/MLC17496696?pdp_filters=item_id:MLC946834578#searchVariation=MLC17496696&position=5&search_layout=stack&type=pad&tracking_id=13e8267d-ee1a-4a03-a161-e98636a82c1f');
    return false;
});

$('#btn-contac').click(function resetform() {
    $("form input[type=text] , form textarea").each(function() { this.value = '' });
});