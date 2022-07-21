<?php

// Update the path below to your autoload.php, 
// see https://getcomposer.org/doc/01-basic-usage.md 
require_once '/path/to/vendor/autoload.php';

use Twilio\Rest\Client;

$sid    = "AC42f446ae9255bf244378a329d76991a3";
$token  = "[Redacted]";
$twilio = new Client($sid, $token);

$message = $twilio->messages
  ->create(
    "whatsapp:+917701822620", // to 
    array(
      "from" => "whatsapp:+14155238886",
      "body" => "Your Twilio code is 1238432"
    )
  );

print($message->sid);
