<?php

function create_cookies($username,$password,$key) {
    $iv = mcrypt_create_iv (16, MCRYPT_RAND);
    $plain = 'user/pass:' . $username . '/' . $password;

    $session = bin2hex ($iv).bin2hex (mcrypt_encrypt (MCRYPT_RIJNDAEL_128, $key, $plain, MCRYPT_MODE_CBC, $iv));
    setcookie ("session", $session, time () + 60*1000*15);  // cookies are valid for 15 minutes
}

function auth($session, $key) {
    $iv = hex2bin (substr ($session, 0, 32));
    $ciphertext = hex2bin (substr ($session, 32));

    /* Strip the "\0" padding */
    $session = rtrim (mcrypt_decrypt (MCRYPT_RIJNDAEL_128, $key, $ciphertext, MCRYPT_MODE_CBC, $iv), "\0");

    if (strpos($session, ":") > 0 && substr ($session, 0, strlen ('user/pass')) === 'user/pass') {
        $session = explode (":", $session)[1];
        if (strpos ($session, "/") > 0) {
            list($username, $password) = explode("/", $session);
        } else {
            die("The session is corrupted!");
        }
        // user/pass:aaa/bbb
    } else {
        die("The session is  corrupted!");
    }

    if (verify_credentials ($username, $password)) {
        return $username;
    } else {
        die ("Wrong login or password.!");
    }
}

function verify_credentials($username, $password) {
    global $aes_key;
    $pdo = new SQLite3 ('database.db', SQLITE3_OPEN_READONLY);

    $result = $pdo->query("SELECT * FROM users WHERE username='$username' AND password='$password';");

    if($row = $result->fetchArray (SQLITE3_ASSOC)) {
        create_cookies($row['username'], $row['password'], $aes_key);
        $pdo->close();
        return True;
    }
    $pdo->close();
    return False;
}
