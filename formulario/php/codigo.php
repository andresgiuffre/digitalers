<?php

//Capturamos las variables
$nombre=$_POST['nombre'];
$email=$_POST['email'];
$consulta=$_POST['consulta'];

echo $nombre;
echo $email;
echo $consulta;

$mensaje="
Nombre: $nombre<br /><br />
Email: $email<br /><br />
Consulta: $consulta<br /><br />
";

echo $mensaje;

//Enviar mail
mail("info@misitio.com", "Consulta Web Site", $mensaje, "From: $nombre <$mail>\nReply-To:$mail\nContent-Type: text/html; charset=iso-8859-1\n");

?>