<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LifeDrop Premium | Don de Sang d'Excellence</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        :root {
            --premium-red: #8b0000;
            --premium-gold: #d4af37;
        }
        
        .hero-section {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                        url('assets/images/blood-donation-hero.jpg');
            background-size: cover;
            height: 100vh;
            color: white;
        }
        
        .stat-card {
            border-left: 4px solid var(--premium-red);
            transition: transform 0.3s;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(139, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <!-- Hero Section -->
    <section class="hero-section d-flex align-items-center">
        <div class="container text-center">
            <h1 class="display-3 fw-bold mb-4">Donnez du sang, <span class="text-premium-gold">sauvez des vies</span></h1>
            <p class="lead mb-5">Rejoignez notre communauté premium de donneurs engagés</p>
            <a href="/user/register.php" class="btn btn-danger btn-lg px-5 py-3">Devenir Donneur</a>
            
            <!-- Stats en temps réel -->
            <div class="row mt-5 g-4">
                <div class="col-md-4">
                    <div class="stat-card bg-white p-4 rounded text-dark">
                        <h3 class="counter" data-target="12453">0</h3>
                        <p>Donneurs actifs</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="stat-card bg-white p-4 rounded text-dark">
                        <h3 class="counter" data-target="876">0</h3>
                        <p>Vies sauvées aujourd'hui</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="stat-card bg-white p-4 rounded text-dark">
                        <h3><span class="counter" data-target="42">0</span>%</h3>
                        <p>Stock O- (Urgent)</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script src="assets/js/counter-animation.js"></script>
</body>
</html>