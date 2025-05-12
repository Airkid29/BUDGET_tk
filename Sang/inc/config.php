<?php
declare(strict_types=1);

class DBConfig {
    private const HOST = 'localhost';
    private const DBNAME = 'blood_donation_premium';
    private const USER = 'secure_user';
    private const PASS = 'complex_password_123!';
    private const CHARSET = 'utf8mb4';
    private const OPTIONS = [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES => false,
    ];

    public static function getPDO(): PDO {
        $dsn = "mysql:host=".self::HOST.";dbname=".self::DBNAME.";charset=".self::CHARSET;
        return new PDO($dsn, self::USER, self::PASS, self::OPTIONS);
    }
}
?>