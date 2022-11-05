function mostrarPaisesOrigen(){
    document.write("<label for='paisOrigen'>País de origen:</label>")
    document.write("<select class='form-control' id='paisOrigen' name='pais-origen'>");
    document.write("<option selected>Elija ...</option>");
    for (const key of paisCapital.keys()) {
        document.write("<option>" + key + "</option>");
      }
     document.write("</select>\n");
}

function mostrarEspacio(string){
  let string1 = "espacio-" + string;
  let string2 = "Espacio " + string;
  document.write("<label for='" + string1 + "'>" + string2 + ":</label>")
  document.write("<select class='form-control' id='" + string1 + "' name='" + string1 + "'>")
  document.write("<option selected>Elija ...</option>")
  document.write("<option>10x10x10</option>")
  document.write("<option>20x20x20</option>")
  document.write("<option>30x30x30</option>")
  document.write("</select>\n");
}

function mostrarKilos(string){
  let string1 = "kilos-" + string;
  let string2 = "Kilos " + string; 
  document.write("<label for='" + string1 + "'>" + string2 + ":</label>")
  document.write("<select class='form-control' id='" + string1 + "' name='" + string1 + "'>")
  document.write("<option selected>Elija ...</option>")
  document.write("<option>500 gr</option>")
  document.write("<option>800 gr</option>")
  document.write("<option>1 kg</option>")
  document.write("<option>1.5 kg</option>")
  document.write("<option>2 kg</option>")
  document.write("</select>\n");
}
