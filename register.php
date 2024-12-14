<?php
include 'config.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    if (empty($username) || empty($password)) {
        $error = "Username dan Password tidak boleh kosong.";
    } else {
        // Cek apakah username sudah ada
        $stmt_check = $conn->prepare("SELECT username FROM users WHERE username = ?");
        $stmt_check->bind_param("s", $username);
        $stmt_check->execute();
        $stmt_check->store_result();
        
        if ($stmt_check->num_rows > 0) {
            $error = "Username sudah digunakan.";
        } else {
            // Jika username tersedia, simpan akun ke database
            $hashed_password = password_hash($password, PASSWORD_BCRYPT);
            
            $stmt_insert = $conn->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
            $stmt_insert->bind_param("ss", $username, $hashed_password);
            
            if ($stmt_insert->execute()) {
                header("Location: login.php");  // Redirect ke halaman login setelah sukses
                exit();
            } else {
                $error = "Terjadi kesalahan saat membuat akun.";
            }
            
            $stmt_insert->close();
        }
        
        $stmt_check->close();
    }
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Buat Akun</title>
</head>
<body>
    <h2>Buat Akun</h2>
    <?php if (!empty($error)) echo "<p style='color: red;'>$error</p>"; ?>
    <form method="POST" action="">
        <label>Username:</label><br>
        <input type="text" name="username"><br>
        <label>Password:</label><br>
        <input type="password" name="password"><br>
        <button type="submit">Buat Akun</button>
    </form>
</body>
</html>
