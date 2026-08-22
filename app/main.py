from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Cloud Security Dashboard",
    description="Cloud security application for CI/CD deployment",
    version="1.0.0",
)


def current_time():
    return datetime.now(timezone.utc).isoformat()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>Cloud Security Dashboard</title>

        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
            }

            body {
                background: #0f172a;
                color: #f8fafc;
                min-height: 100vh;
            }

            header {
                padding: 25px 50px;
                background: #020617;
                border-bottom: 1px solid #1e293b;
            }

            header h1 {
                font-size: 28px;
            }

            header p {
                color: #94a3b8;
                margin-top: 8px;
            }

            .container {
                max-width: 1200px;
                margin: 40px auto;
                padding: 0 25px;
            }

            .status {
                background: #052e16;
                border: 1px solid #166534;
                border-radius: 12px;
                padding: 20px;
                margin-bottom: 30px;
            }

            .status span {
                color: #4ade80;
                font-weight: bold;
            }

            .cards {
                display: grid;
                grid-template-columns:
                    repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
            }

            .card {
                background: #1e293b;
                border: 1px solid #334155;
                border-radius: 12px;
                padding: 25px;
            }

            .card h2 {
                font-size: 18px;
                margin-bottom: 10px;
            }

            .value {
                font-size: 30px;
                font-weight: bold;
                color: #38bdf8;
            }

            .healthy {
                color: #4ade80;
            }

            footer {
                text-align: center;
                color: #64748b;
                margin-top: 50px;
                padding-bottom: 30px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Cloud Security Dashboard</h1>
            <p>CI/CD deployment demonstration application</p>
        </header>

        <main class="container">

            <div class="status">
                Application Status:
                <span>● ONLINE</span>
            </div>

            <div class="cards">

                <div class="card">
                    <h2>Application</h2>
                    <div class="value">v1.0.0</div>
                </div>

                <div class="card">
                    <h2>Environment</h2>
                    <div class="value">AWS</div>
                </div>

                <div class="card">
                    <h2>CI/CD</h2>
                    <div class="value healthy">ACTIVE</div>
                </div>

                <div class="card">
                    <h2>Security</h2>
                    <div class="value healthy">SECURE</div>
                </div>

            </div>

            <footer>
                Cloud Security CI/CD Project
            </footer>

        </main>

    </body>

    </html>
    """


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "cloud-security-app",
        "timestamp": current_time(),
    }


@app.get("/api/status")
def status():
    return {
        "application": "cloud-security-dashboard",
        "version": "1.0.0",
        "status": "running",
        "timestamp": current_time(),
    }


@app.get("/api/security")
def security_status():
    return {
        "security_status": "secure",
        "https": True,
        "authentication": "enabled",
        "secrets_management": "AWS Secrets Manager",
        "container_security": "enabled",
    }


@app.get("/api/deployment")
def deployment_info():
    return {
        "pipeline": "GitHub Actions",
        "container": "Docker",
        "platform": "AWS",
        "deployment": "automated",
        "status": "successful",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )