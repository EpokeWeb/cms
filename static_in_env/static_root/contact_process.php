<?php

    $to = "franciscampbel@hotmail.com";
    $from = $_REQUEST['contact_email'];
    $name = $_REQUEST['contact_name'];
    $headers = "From: $from";
    $subject = "Message client - Site Web";

    $fields = array();
    $fields{"Nom"} = "contact_name";
    $fields{"Courriel"} = "contact_email";
    $fields{"Site Web"} = "contact_url";
    $fields{"Téléphone"} = "contact_phone";
    $fields{"Comment avez-vous entendu parlé de nous?"} = "learn_seowave";
    $fields{"Intéressé par"} = "interested_in";
    $fields{"Texte"} = "addInfos";

    $body = "Voici le contenu du message:\n\n"; foreach($fields as $a => $b){   $body .= sprintf("%20s: %s\n",$b,$_REQUEST[$a]); }

    $send = mail($to, $subject, $body, $headers);

?>
