<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>OCEAN COMMAND</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f4f7fb;
            color: #1d2939;
        }

        .header {
            background: #0b1f33;
            color: white;
            padding: 22px 35px;
        }

        .header h1 {
            font-size: 30px;
            margin-bottom: 5px;
        }

        .header p {
            color: #b8c7d9;
            font-size: 14px;
        }

        .layout {
            display: flex;
            min-height: calc(100vh - 88px);
        }

        .sidebar {
            width: 220px;
            background: #102a43;
            padding: 25px 15px;
        }

        .sidebar h3 {
            color: white;
            margin-bottom: 25px;
            text-align: center;
        }

        .nav-item {
            color: #d9e2ec;
            padding: 13px 15px;
            margin-bottom: 8px;
            border-radius: 8px;
            cursor: pointer;
        }

        .nav-item:hover {
            background: #1f4568;
        }

        .nav-item.active {
            background: #1f5f8b;
            color: white;
        }

        .content {
            flex: 1;
            padding: 30px;
        }

        .welcome {
            margin-bottom: 25px;
        }

        .welcome h2 {
            font-size: 25px;
            margin-bottom: 6px;
        }

        .welcome p {
            color: #667085;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin-bottom: 30px;
        }

        .card {
            background: white;
            padding: 22px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08);
        }

        .card-title {
            color: #667085;
            font-size: 14px;
            margin-bottom: 12px;
        }

        .card-value {
            font-size: 30px;
            font-weight: bold;
            color: #0b1f33;
        }

        .section {
            background: white;
            padding: 22px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08);
            margin-bottom: 20px;
        }

        .section h3 {
            margin-bottom: 18px;
        }

        .status-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 15px;
        }

        .status {
            padding: 18px;
            border-radius: 10px;
            background: #f7f9fc;
        }

        .status strong {
            display: block;
            font-size: 25px;
            margin-bottom: 5px;
        }

        .status span {
            color: #667085;
            font-size: 14px;
        }

        .online {
            color: #16803c;
        }

        @media (max-width: 900px) {
            .cards {
                grid-template-columns: repeat(2, 1fr);
            }

            .sidebar {
                width: 180px;
            }
        }

        @media (max-width: 650px) {
            .layout {
                flex-direction: column;
            }

            .sidebar {
                width: 100%;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .status-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>

<body>

    <div class="header">
        <h1>⚓ OCEAN COMMAND</h1>
        <p>MERCHANT FLEET CONTROL SYSTEM</p>
    </div>

    <div class="layout">

        <aside class="sidebar">

            <h3>🚢 NAVIGATION</h3>

            <div class="nav-item active">🏠 Dashboard</div>
            <div class="nav-item">🚢 Fleet</div>
            <div class="nav-item">👨‍✈️ Crew</div>
            <div class="nav-item">🌊 Voyages</div>
            <div class="nav-item">📦 Cargo</div>
            <div class="nav-item">⛽ Fuel</div>
            <div class="nav-item">🔧 Maintenance</div>
            <div class="nav-item">📊 Reports</div>

        </aside>

        <main class="content">

            <div class="welcome">
                <h2>Fleet Dashboard</h2>
                <p>Real-time overview of your merchant fleet operations.</p>
            </div>

            <div class="cards">

                <div class="card">
                    <div class="card-title">🚢 TOTAL SHIPS</div>
                    <div class="card-value">5</div>
                </div>

                <div class="card">
                    <div class="card-title">👨‍✈️ CREW MEMBERS</div>
                    <div class="card-value">6</div>
                </div>

                <div class="card">
                    <div class="card-title">🌊 VOYAGES</div>
                    <div class="card-value">5</div>
                </div>

                <div class="card">
                    <div class="card-title">📦 CARGO RECORDS</div>
                    <div class="card-value">5</div>
                </div>

            </div>

            <div class="section">

                <h3>⚓ Fleet Status</h3>

                <div class="status-grid">

                    <div class="status">
                        <strong class="online">3</strong>
                        <span>Active Ships</span>
                    </div>

                    <div class="status">
                        <strong>1</strong>
                        <span>At Port</span>
                    </div>

                    <div class="status">
                        <strong>1</strong>
                        <span>Under Maintenance</span>
                    </div>

                </div>

            </div>

            <div class="section">

                <h3>🌊 System Status</h3>

                <p class="online">● Web Interface Online</p>

            </div>

        </main>

    </div>

</body>

</html>