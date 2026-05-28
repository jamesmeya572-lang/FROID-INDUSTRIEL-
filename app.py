from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>CryoExpert</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <style>
        body { background:#0a0f1e; color:white; font-family:Arial; text-align:center; padding:20px; }
        h1 { color:#60a5fa; font-size:28px; }
        p { color:#94a3b8; }
        .btn { background:#1e40af; color:white; padding:15px 30px; border:none; border-radius:10px; font-size:16px; margin:10px; }
    </style>
</head>
<body>
    <h1>❄️ CryoExpert</h1>
    <p>Application de Froid Industriel</p>
    <p>Diagnostic • Réparation • Apprentissage</p>
    <button class="btn">🔍 Démarrer le diagnostic</button>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
