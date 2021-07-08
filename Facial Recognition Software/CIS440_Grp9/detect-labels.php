<?php

require 'vendor/autoload.php';
use Aws\Rekognition\RekognitionClient;

$client = new Aws\Rekognition\RekognitionClient([

    'version' => 'latest',
    'region' => 'us-west-1',
    'credentials' => [
    'key' => 'AKIARRDSN645GR4UJTNU',
    'secret' => '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',

    ]

]);

$result = $client->detectLabels([
    'Image' => [ // Required
        'Bytes' => file_get_contents("1.jpg"),
    ],
    'MaxLabels' => 30, 
    'MinConfidence' => 20,

]);
print_r("test output");
print_r($result);
?>
© 2021 GitHub, Inc.