<?php
include "flag.php";
include "utils.php";
include "session_management.php";

if (isset($_POST['username']) and isset($_POST['password'])) {
    if (isset($_POST['register'])) {
        $message = register($_POST['username'], $_POST['password']);
    } elseif (isset($_POST['login'])) {
        $message = login($_POST['username'], $_POST['password']);
    }
} elseif (isset ($_POST['logout'])) {
    setcookie("session", "", time() - 3600);
    die ('<meta http-equiv="refresh" content="0">');
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>#WebSec Level LevelTwentyOne</title>
    <link rel="stylesheet" href="https://websec.fr/static/bootstrap.min.css" />
    <link rel="stylesheet" href="https://websec.fr/static/websec.css" />

    <script src="../static/jquery.js" defer type="text/javascript"></script>
    <script src="../static/bootstrap.min.js" defer type="text/javascript"></script>
</head>
<body>
<div id="main">
    <div class="container">
        <div class="row">
            <h1>LevelTwentyOne<small> - PatPat</small></h1>
        </div>
        <div class="row">
            <p class="lead">
                For security reason, you're not allowed to register using the letters <code>[admin]</code>.<br>
                You can get the sources of the index <a href="source.php">here</a>,
                the one for sessions management <a href="source1.php">here</a>, and the crypto
                stuff <a href="source2.php">here</a>.<br>
                Many thanks to <mark>icernica</mark> for this level.
            </p>
        </div>
    </div>

    <br>

    <div class="container">
        <?php if (isset ($message)): ?>
        <div class="row">
            <div class="col-md-5 alert alert-<?php echo $message[0]; ?> alert-dismissible" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
                <?php echo $message[1]; ?>
            </div>
        </div>
        <?php endif; ?>


        <div class="row col-md-5">
<?php if (isset ($_COOKIE['session'])) :?>
            <div class="panel panel-default">
                <div class="panel-heading ">
                    <h3 class="panel-title">Welcome <b><?php echo auth($_COOKIE['session'], $aes_key) === "admin"? 'admin': 'user'; ?></b></h3>
                </div>
                <div class="panel-body">
                    <?php if (auth($_COOKIE['session'], $aes_key) === "admin") {
                        echo 'Hello admin, here is your flag: ' . $flag;
                        $pdo = new SQLite3 ('database.db', SQLITE3_OPEN_READWRITE);
                        $stmt = $pdo->prepare('DELETE FROM users WHERE ip = ":ip";');
                        $stmt->bindValue(':ip', $_SERVER['REMOTE_ADDR'], SQLITE3_TEXT);
                        $stmt->execute();
                    } else {
                        echo 'You need to be admin to see the <mark>flag</mark>';
                    }
                    ?>
                </div>
                <div class="panel-footer">
                    <form method="POST">
                        <button class="btn btn-default" name="logout">logout</button>
                    </form>
                </div>

            </div>
<?php else:  // No cookie, the person isn't logged. ?>
            <form class="form-horizontal" method="POST">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" id="username" name="username" placeholder="" class="form-control">
                </div>

                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" placeholder="" class="form-control">
                </div>

                <div class="form-group">
                    <button id="login" class="btn btn-default jsonly" type="submit" name="login">Login</button>
                    <button id="register" class="btn btn-default jsonly" type="submit" name="register">Register</button>
                </div>
            </form>
<?php endif ?>

        </div>
    </div>
</body>
</html>
