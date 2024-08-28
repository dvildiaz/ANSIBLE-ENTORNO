<?php
// Función para realizar un ping a una dirección IP
function ping($ip) {
    // Ejecuta el comando ping en el sistema operativo
    exec(sprintf('ping -c 4 %s', $ip), $output, $return_var);

    // Comprueba si el ping fue exitoso
    if ($return_var == 0) {
        return "Ping exitoso a $ip\n" . implode("\n", $output);
    } else {
        return "Error al hacer ping a $ip";
    }
}

// Verifica si se envió una dirección IP desde el formulario
if (isset($_POST['ip'])) {
    // Dirección IP ingresada desde el formulario
    $ip = $_POST['ip'];

    // Realiza el ping y obtiene el resultado
    $resultado = ping($ip);
} else {
    // Si no se envió una dirección IP, muestra un mensaje de error
    $resultado = "Por favor, ingrese una dirección IP.";
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado del Ping</title>
</head>
<body>
    <h1>Resultado del Ping</h1>
    <p><?php echo $resultado; ?></p>
    <a href="index.html">Volver al formulario</a>
</body>
</html>
