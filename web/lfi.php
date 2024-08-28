<?php
// Directorio donde se encuentran los archivos de ayuda
$directorio_ayuda = "ayuda/";

// Obtener el nombre del archivo de ayuda solicitado
$archivo = $_GET['archivo'];

// Comprobar si el archivo solicitado existe en el directorio de ayuda
if (file_exists($directorio_ayuda . $archivo)) {
    // Mostrar el contenido del archivo de ayuda
    echo "<h1>Contenido de la ayuda:</h1>";
    echo '<a href="./lfi.php?archivo=bot.txt">Ayuda para bots</a>';
    echo "<pre>";
    include($directorio_ayuda . $archivo);
    echo "</pre>";
} else {
    // Mostrar un mensaje de error si el archivo no existe
    echo "<h1>Error: Archivo de ayuda no encontrado.</h1>";
}
?>
