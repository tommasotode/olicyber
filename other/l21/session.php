<?php
include "flag.php";

function login($username, $password) {
    global $aes_key;

    $pdo = new SQLite3 ('database.db', SQLITE3_OPEN_READONLY);

    $stmt = $pdo->prepare('SELECT * FROM users WHERE username=:username AND password=:password;');
    $stmt->bindValue(':username', $username, SQLITE3_TEXT);
    $stmt->bindValue(':password', md5($password), SQLITE3_TEXT);

    if ($row = $stmt->execute()->fetchArray(SQLITE3_ASSOC)) {
        $pdo->close();
        create_cookies($row['username'], $row['password'], $aes_key);
        die ('<meta http-equiv="refresh" content="0">');
    } else {
        $pdo->close();
        return ['danger', 'Wrong user or password.'];
    }
}

function register($username, $password) {
    if (! ctype_alnum($username)) {
        return ["danger","Your nick isn't alphanumeric."];
    } elseif (strlen($username) < 6){
        return ["danger", "Your nick is too small"];
    } elseif (preg_match('/(a|d|m|i|n)/', strtolower ($username))) {
        return ["danger", "Your nick is matching [admin]."];
    }

    $pdo = new SQLite3 ('database.db', SQLITE3_OPEN_READWRITE);
    $stmt = $pdo->prepare('INSERT INTO users (username, password, ip) VALUES (:username, :password, :ip);');
    $stmt->bindValue(':username', $username, SQLITE3_TEXT);
    $stmt->bindValue(':password', md5($password), SQLITE3_TEXT);
    $stmt->bindValue(':ip', $_SERVER['REMOTE_ADDR'], SQLITE3_TEXT);

    if($stmt->execute()) {
        $pdo->close();
        return ["success", "The user was created successfully."];
    } else {
        $pdo->close();
        return ["warning","Your nick is likely already present in the database."];
    }
} 