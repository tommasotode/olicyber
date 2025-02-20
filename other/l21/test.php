<?php

$cipher = "aes-128-cbc";

function create_cookies($username,$password,$key="aaaaaaaaaaaaaaaa") {
    $plain = 'user/pass:' . $username . '/' . $password;

    global $cipher;

    $iv = 'bbbbbbbbbbbbbbbb';
    $session = bin2hex ($iv).bin2hex ( openssl_encrypt($plain, $cipher, $key, $options=0, $iv) );
    setcookie ("session", $session, time () + 60*1000*15);
}

function auth($session, $key="aaaaaaaaaaaaaaaa") {
    $iv = hex2bin (substr ($session, 0, 32));
    $ciphertext = hex2bin (substr ($session, 32));

    global $cipher;

    $session = openssl_decrypt($ciphertext, $cipher, $key, $options=0, $iv);
    var_dump($session);

    if (strpos($session, ":") > 0 && substr ($session, 0, strlen ('user/pass')) === 'user/pass') {
        $session = explode (":", $session)[1];
        if (strpos ($session, "/") > 0) {
            list($username, $password) = explode("/", $session);
        } else {
            die("morto in a");
        }
    } else {
        die("morto in b");
    }
}

if (isset($_POST['username']) && isset($_POST['password']))
{
    create_cookies($_POST['username'], $_POST['password']);
}
if (isset($_POST['c']))
{
    auth($_POST['c']);
}