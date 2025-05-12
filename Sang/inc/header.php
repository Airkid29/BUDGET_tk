<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $pageTitle ?? 'Don de Sang'; ?></title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">
    
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    
    <!-- CSS -->
    <link rel="stylesheet" href="assets/css/style.css">
    
    <!-- Slick Slider -->
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>

    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
    <link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css"/>

    
</head>
<body>
    <!-- Navigation 3.0 -->
    <nav class="modern-nav">
        <div class="nav-container">
            <a href="index.php" class="nav-logo">
                <!--<img src="assets/images/logo.svg" alt="BloodDon">-->
                <span>LifeSaver</span>
            </a>
            
            <div class="nav-menu">
                <ul class="nav-links">
                    <li><a href="index.php" class="active">Accueil</a></li>
                    <li><a href="about.php">À propos</a></li>
                    <li><a href="centers.php">Centres</a></li>
                    <li><a href="faq.php">FAQ</a></li>
                </ul>
                
                <div class="nav-actions">
                    <?php if (isset($_SESSION['user_id'])): ?>
                        <a href="dashboard.php" class="nav-button">
                            <i class="fas fa-user"></i>
                            <span>Mon compte</span>
                        </a>
                    <?php else: ?>
                        <a href="login.php" class="nav-button outline">
                            <i class="fas fa-sign-in-alt"></i>
                            <span>Connexion</span>
                        </a>
                        <a href="register.php" class="nav-button blood">
                            <i class="fas fa-heart"></i>
                            <span>Devenir donneur</span>
                        </a>
                    <?php endif; ?>
                </div>
            </div>
            
            <button class="nav-toggle">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>
    
    <main>