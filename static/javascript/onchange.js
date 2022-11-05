$( document ).ready(function() {

    // Resetea el valor de país de origen cada vez que se recarga la página
    $("#paisOrigen").val('');

    // Cada vez que cambia el país de origen...
    $("#paisOrigen").on("change", function () {

        let ciudadOrigen = "<option>Elija ...</option>";
        let paisDestino = "<option>Elija ...</option>";
        let selected = document.getElementById("paisOrigen").value;

        if (selected != "Elija ..."){ 
            ciudadOrigen+= "<option>" + paisCapital.get(selected) + "</option>";
            for (const key of paisCapital.keys()){
                if (key != selected){
                    paisDestino += "<option>" + key + "</option>";
                }
            }
        }
        document.getElementById("ciudadOrigen").innerHTML = ciudadOrigen;
        document.getElementById("paisDestino").innerHTML = paisDestino;
        document.getElementById("ciudadDestino").innerHTML = "<option>Elija ...</option>";
        
    });

    // Cada vez que cambia el país de destino...
    $("#paisDestino").on("change", function () {

        let ciudadDestino = "<option>Elija ...</option>";
        let selected = document.getElementById("paisDestino").value;

        if (selected != "Elija ..."){
            ciudadDestino += "<option>" + paisCapital.get(selected) + "</option>";
        }
        document.getElementById("ciudadDestino").innerHTML = ciudadDestino;

    });

});