$.validator.setDefaults({
    submitHandler: function() {
        $("form input[type=text] , form textarea, form select").each(function() { this.value = '' });
    }
});


$(document).ready(function() {
    $('#formulario_mascota').validate({
        rules: {
            fullname: {
                required: true,
                minlength: 5
            },
            comments: {
                required: true,
                minlength: 20
            },
            email: {
                required: true,
                email: true,
            },

        },
        messages: {
            fullname: {
                required: "Por favor ingresa tu nombre completo",
                minlength: "Tu nombre debe ser de no menos de 5 caracteres"
            },
            comments: {
                required: "Por favor ingresa un comentario",
                minlength: "Tu nombre debe ser de no menos de 20 caracteres"
            },
            email: "Por favor ingresa un correo válido",
        },
        errorElement: "em",
        errorPlacement: function(error, element) {
            error.addClass("help-block");

            if (element.prop("type") === "checkbox") {
                error.insertAfter(element.parent("label"));
            } else {
                error.insertAfter(element);
            }
        },
        highlight: function(element, errorClass, validClass) {
            $(element).parents(".col-sm-10").addClass("has-error").removeClass("has-success");
        },
        unhighlight: function(element, errorClass, validClass) {
            $(element).parents(".col-sm-10").addClass("has-success").removeClass("has-error");
        }
    });
});