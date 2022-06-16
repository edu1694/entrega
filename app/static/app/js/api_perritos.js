$("#btn-cargar").click(function(event) {
    event.preventDefault();

    var url = "https://dog.ceo/api/breeds/image/random";
    fetch(url)
        .then(response => response.json())
        .then(data => {
            var $fotito_perro = $("<p><img src='" + data.message + "' width= 400px  height= 400px>");
            $("#info").empty();
            $('#info')
                .append($fotito_perro);
        })
        .catch(error => console.error(error));

});