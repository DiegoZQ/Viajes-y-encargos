// Cada vez que se haga click a un elemento clickable-row, 
// la ventana se cambia al link asociado al elemento de la clase clickable-row.
$( document ).ready(function() {
    $(".clickable-row").click(function () {
        window.location = $(this).attr('href');
    });
});