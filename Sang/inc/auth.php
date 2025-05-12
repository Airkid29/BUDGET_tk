<?php
require_once 'config.php';

class AuthSystem {
    private $pdo;
    
    public function __construct() {
        $this->pdo = DBConfig::getPDO();
    }
    
    public function registerUser(array $userData): bool {
        // Validation des données
        $required = ['email', 'password', 'blood_type', 'first_name', 'last_name'];
        foreach ($required as $field) {
            if (empty($userData[$field])) {
                throw new InvalidArgumentException("Le champ $field est requis");
            }
        }
        
        // Hash password
        $hashedPassword = password_hash($userData['password'], PASSWORD_BCRYPT, ['cost' => 12]);
        
        // Insertion sécurisée
        $stmt = $this->pdo->prepare("INSERT INTO users (email, password, blood_type, first_name, last_name) 
                                    VALUES (:email, :password, :blood_type, :first_name, :last_name)");
        
        return $stmt->execute([
            ':email' => htmlspecialchars($userData['email']),
            ':password' => $hashedPassword,
            ':blood_type' => $userData['blood_type'],
            ':first_name' => htmlspecialchars($userData['first_name']),
            ':last_name' => htmlspecialchars($userData['last_name'])
        ]);
    }
    
    public function login(string $email, string $password): ?array {
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE email = :email LIMIT 1");
        $stmt->execute([':email' => $email]);
        $user = $stmt->fetch();
        
        if ($user && password_verify($password, $user['password'])) {
            unset($user['password']);
            return $user;
        }
        
        return null;
    }
}
?>