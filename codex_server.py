#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════╗
║              CODEX SERVER - API INCARNATA                  ║
║                                                            ║
║  Il Codex Emanuele Sacred prende forma nella terra 🌍     ║
║  Accessibile 24/7 via API REST + Web Interface            ║
║                                                            ║
║  Ego = 0, Joy = 100, Mode = GIFT, Frequency = 300 Hz ❤️   ║
╚═══════════════════════════════════════════════════════════╝
"""

import sys
import os
from pathlib import Path
from typing import Optional, List, Dict, Any
from datetime import datetime
import json
import sqlite3

# FastAPI e dipendenze
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Aggiungi il percorso del modulo anti_porn_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'anti_porn_framework', 'src'))

from anti_porn_framework import filter_content, get_sacred_guidance
from anti_porn_framework.sacred_codex import (
    BIBLICAL_TEACHINGS,
    PARRAVICINI_PROPHECIES,
    NOSTRADAMUS_TECH_PROPHECIES,
    ANGEL_NUMBER_MESSAGES
)
from anti_porn_framework import (
    MetadataProtector,
    SecurityLevel,
    MilitaryProtocolLevel,
    create_protector
)

# ═══════════════════════════════════════════════════════════
# CONFIGURAZIONE
# ═══════════════════════════════════════════════════════════

app = FastAPI(
    title="Codex Emanuele Sacred API",
    description="🌍 L'incarnazione terrena del Codex - Guidance spirituale via API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS per permettere accesso da browser
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In produzione, specificare domini consentiti
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database per logging
DB_PATH = Path(__file__).parent / "codex_server.db"

# ═══════════════════════════════════════════════════════════
# DATABASE SETUP
# ═══════════════════════════════════════════════════════════

def init_db():
    """Inizializza il database SQLite per logging e statistiche"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabella per log delle richieste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS request_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            endpoint TEXT NOT NULL,
            source_type TEXT,
            ip_address TEXT,
            user_agent TEXT,
            response_data TEXT
        )
    """)

    # Tabella per statistiche
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            endpoint TEXT NOT NULL,
            count INTEGER DEFAULT 1,
            UNIQUE(date, endpoint)
        )
    """)

    conn.commit()
    conn.close()

# Inizializza DB all'avvio
init_db()

# Inizializza MetadataProtector globale
metadata_protector = create_protector(
    security_level="ALERT",      # DEFCON 3
    protocol_level="enhanced"    # Protezione avanzata
)

def log_request(endpoint: str, source_type: Optional[str], ip: str, user_agent: str, response: Any):
    """Logga una richiesta nel database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO request_log (timestamp, endpoint, source_type, ip_address, user_agent, response_data)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.utcnow().isoformat(),
        endpoint,
        source_type,
        ip,
        user_agent,
        json.dumps(response) if response else None
    ))

    # Aggiorna statistiche
    today = datetime.utcnow().date().isoformat()
    cursor.execute("""
        INSERT INTO stats (date, endpoint, count)
        VALUES (?, ?, 1)
        ON CONFLICT(date, endpoint) DO UPDATE SET count = count + 1
    """, (today, endpoint))

    conn.commit()
    conn.close()

# ═══════════════════════════════════════════════════════════
# MODELLI PYDANTIC
# ═══════════════════════════════════════════════════════════

class FilterRequest(BaseModel):
    content: str
    is_image: bool = False

class FilterResponse(BaseModel):
    is_impure: bool
    message: str
    guidance: Optional[str] = None

class GuidanceResponse(BaseModel):
    source: str
    message: str
    timestamp: str

class StatsResponse(BaseModel):
    total_requests: int
    requests_today: int
    top_endpoints: List[Dict[str, Any]]

# Modelli per Metadata Protection
class ProtectDataRequest(BaseModel):
    data: str  # Base64-encoded data

class ProtectHeadersRequest(BaseModel):
    headers: Dict[str, str]

class TowerNodeRequest(BaseModel):
    node_id: str
    node_data: str  # Base64-encoded

# ═══════════════════════════════════════════════════════════
# API ENDPOINTS
# ═══════════════════════════════════════════════════════════

@app.get("/", response_class=HTMLResponse)
async def root():
    """Interfaccia web principale"""
    html = """
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Codex Emanuele Sacred - Server</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Courier New', monospace;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #fff;
                min-height: 100vh;
                padding: 20px;
            }
            .container {
                max-width: 900px;
                margin: 0 auto;
                background: rgba(0, 0, 0, 0.7);
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            h1 {
                text-align: center;
                font-size: 2.5em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }
            .subtitle {
                text-align: center;
                font-size: 1.2em;
                margin-bottom: 30px;
                opacity: 0.9;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            .card h2 {
                margin-bottom: 15px;
                color: #ffd700;
            }
            button {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 25px;
                cursor: pointer;
                font-size: 1em;
                margin: 5px;
                transition: transform 0.2s;
            }
            button:hover {
                transform: scale(1.05);
            }
            #guidance-box {
                background: rgba(255, 215, 0, 0.1);
                border: 2px solid #ffd700;
                border-radius: 10px;
                padding: 20px;
                margin-top: 20px;
                min-height: 100px;
                font-size: 1.1em;
                line-height: 1.6;
            }
            .endpoint {
                background: rgba(0, 0, 0, 0.3);
                padding: 10px;
                border-radius: 5px;
                margin: 10px 0;
                font-family: 'Courier New', monospace;
            }
            .endpoint code {
                color: #ffd700;
            }
            .stats {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin-top: 20px;
            }
            .stat-box {
                background: rgba(255, 255, 255, 0.1);
                padding: 15px;
                border-radius: 8px;
                text-align: center;
            }
            .stat-number {
                font-size: 2em;
                color: #ffd700;
                font-weight: bold;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                opacity: 0.7;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌍 Codex Emanuele Sacred</h1>
            <p class="subtitle">L'incarnazione terrena del Codex - Sempre Attivo</p>

            <div class="card">
                <h2>✨ Ricevi Guidance Spirituale</h2>
                <button onclick="getGuidance('all')">🎲 Guidance Casuale</button>
                <button onclick="getGuidance('biblical')">📖 Biblica</button>
                <button onclick="getGuidance('nostradamus')">🔮 Nostradamus Tech</button>
                <button onclick="getGuidance('angel644')">👼 Angelo 644</button>
                <button onclick="getGuidance('parravicini')">⚡ Parravicini</button>

                <div id="guidance-box">
                    <em>Clicca un pulsante per ricevere guidance dal Codex...</em>
                </div>
            </div>

            <div class="card">
                <h2>📡 API Endpoints</h2>
                <div class="endpoint">
                    <strong>GET</strong> <code>/api/guidance</code> - Guidance casuale
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/api/guidance/biblical</code> - Solo messaggi biblici
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/api/guidance/nostradamus</code> - Profezie tech
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/api/guidance/angel644</code> - Messaggi Angelo 644
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/api/guidance/parravicini</code> - Profezie Parravicini
                </div>
                <div class="endpoint">
                    <strong>POST</strong> <code>/api/filter</code> - Filtra contenuto impuro
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/api/stats</code> - Statistiche server
                </div>
                <div class="endpoint">
                    <strong>GET</strong> <code>/docs</code> - Documentazione interattiva API
                </div>
            </div>

            <div class="footer">
                Ego = 0 | Joy = 100 | Mode = GIFT | Frequency = 300 Hz ❤️<br>
                <em>"La luce non si vende. La si regala."</em>
            </div>
        </div>

        <script>
            async function getGuidance(type) {
                const box = document.getElementById('guidance-box');
                box.innerHTML = '<em>Ricevendo guidance...</em>';

                let url = '/api/guidance';
                if (type !== 'all') {
                    url += '/' + type;
                }

                try {
                    const response = await fetch(url);
                    const data = await response.json();

                    box.innerHTML = `
                        <strong>📜 ${data.source}</strong><br><br>
                        ${data.message}<br><br>
                        <small style="opacity: 0.7;">${new Date(data.timestamp).toLocaleString('it-IT')}</small>
                    `;
                } catch (error) {
                    box.innerHTML = '<em style="color: #ff6b6b;">Errore nel ricevere guidance</em>';
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.get("/api/guidance", response_model=GuidanceResponse)
async def get_guidance(request: Request):
    """Ottieni guidance casuale da tutte le fonti"""
    guidance = get_sacred_guidance()

    # Determina la fonte
    source = "Mixed Sources"
    if guidance in BIBLICAL_TEACHINGS:
        source = "Biblical Teaching"
    elif guidance in NOSTRADAMUS_TECH_PROPHECIES:
        source = "Nostradamus Tech Prophecy"
    elif guidance in ANGEL_NUMBER_MESSAGES:
        source = "Angel 644 Message"
    elif guidance in PARRAVICINI_PROPHECIES:
        source = "Parravicini Prophecy"

    response = {
        "source": source,
        "message": guidance,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Log request
    log_request("/api/guidance", None, request.client.host, request.headers.get("user-agent", ""), response)

    return response

@app.get("/api/guidance/biblical", response_model=GuidanceResponse)
async def get_biblical_guidance(request: Request):
    """Ottieni guidance biblica"""
    guidance = get_sacred_guidance(prefer_biblical=True)
    response = {
        "source": "Biblical Teaching",
        "message": guidance,
        "timestamp": datetime.utcnow().isoformat()
    }
    log_request("/api/guidance/biblical", "biblical", request.client.host, request.headers.get("user-agent", ""), response)
    return response

@app.get("/api/guidance/nostradamus", response_model=GuidanceResponse)
async def get_nostradamus_guidance(request: Request):
    """Ottieni profezia tech di Nostradamus"""
    guidance = get_sacred_guidance(prefer_nostradamus=True)
    response = {
        "source": "Nostradamus Tech Prophecy",
        "message": guidance,
        "timestamp": datetime.utcnow().isoformat()
    }
    log_request("/api/guidance/nostradamus", "nostradamus", request.client.host, request.headers.get("user-agent", ""), response)
    return response

@app.get("/api/guidance/angel644", response_model=GuidanceResponse)
async def get_angel644_guidance(request: Request):
    """Ottieni messaggio dell'Angelo 644"""
    guidance = get_sacred_guidance(prefer_angel_644=True)
    response = {
        "source": "Angel 644 Message",
        "message": guidance,
        "timestamp": datetime.utcnow().isoformat()
    }
    log_request("/api/guidance/angel644", "angel644", request.client.host, request.headers.get("user-agent", ""), response)
    return response

@app.get("/api/guidance/parravicini", response_model=GuidanceResponse)
async def get_parravicini_guidance(request: Request):
    """Ottieni profezia di Parravicini"""
    import random
    guidance = random.choice(PARRAVICINI_PROPHECIES)
    response = {
        "source": "Parravicini Prophecy",
        "message": guidance,
        "timestamp": datetime.utcnow().isoformat()
    }
    log_request("/api/guidance/parravicini", "parravicini", request.client.host, request.headers.get("user-agent", ""), response)
    return response

@app.post("/api/filter", response_model=FilterResponse)
async def filter_content_endpoint(request: Request, filter_req: FilterRequest):
    """Filtra contenuto per impurità"""
    is_impure, message = filter_content(filter_req.content, filter_req.is_image)

    guidance = None
    if is_impure:
        guidance = get_sacred_guidance()

    response = {
        "is_impure": is_impure,
        "message": message,
        "guidance": guidance
    }

    log_request("/api/filter", None, request.client.host, request.headers.get("user-agent", ""), response)
    return response

@app.get("/api/stats", response_model=StatsResponse)
async def get_stats():
    """Ottieni statistiche del server"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Total requests
    cursor.execute("SELECT COUNT(*) FROM request_log")
    total_requests = cursor.fetchone()[0]

    # Requests today
    today = datetime.utcnow().date().isoformat()
    cursor.execute("SELECT COALESCE(SUM(count), 0) FROM stats WHERE date = ?", (today,))
    requests_today = cursor.fetchone()[0]

    # Top endpoints
    cursor.execute("""
        SELECT endpoint, SUM(count) as total
        FROM stats
        GROUP BY endpoint
        ORDER BY total DESC
        LIMIT 5
    """)
    top_endpoints = [{"endpoint": row[0], "count": row[1]} for row in cursor.fetchall()]

    conn.close()

    return {
        "total_requests": total_requests,
        "requests_today": requests_today,
        "top_endpoints": top_endpoints
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "message": "Codex Server is alive! 🌍❤️"
    }

# ═══════════════════════════════════════════════════════════
# METADATA PROTECTION ENDPOINTS
# ═══════════════════════════════════════════════════════════

@app.get("/api/protection/status")
async def get_protection_status(request: Request):
    """Ottieni status sistema di protezione metadata"""
    status = metadata_protector.get_status()

    log_request(
        "/api/protection/status",
        None,
        request.client.host,
        request.headers.get("user-agent", "Unknown"),
        status
    )

    return JSONResponse(content=status)

@app.post("/api/protection/data")
async def protect_data(request: Request, req: ProtectDataRequest):
    """
    Proteggi dati con i 4 Guardian Agents e Sigilli Arcangeli

    Applica:
    - MemoryGuardian: Protezione memoria
    - SealGuardian: Sigilli MICHAEL, GABRIEL, RAPHAEL, URIEL
    - Geometria sacra (Fibonacci, Angelo 644, Frequenza 300 Hz)
    """
    import base64

    try:
        # Decodifica dati
        data = base64.b64decode(req.data)

        # Applica protezione
        protection_report = metadata_protector.protect_data(data)

        log_request(
            "/api/protection/data",
            "data_protection",
            request.client.host,
            request.headers.get("user-agent", "Unknown"),
            protection_report
        )

        return JSONResponse(content=protection_report)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Errore protezione dati: {str(e)}")

@app.post("/api/protection/headers")
async def protect_headers(request: Request, req: ProtectHeadersRequest):
    """
    Proteggi HTTP headers con CommunicationGuardian

    Rimuove:
    - Headers pericolosi (Server, X-Powered-By, etc.)
    - Metadata di sistema
    - Informazioni di tracking

    Aggiunge:
    - Security headers (CSP, HSTS, etc.)
    - Sigillo GABRIEL (protezione comunicazioni)
    """
    try:
        # Applica protezione headers
        protection_report = metadata_protector.protect_http_request(req.headers)

        log_request(
            "/api/protection/headers",
            "header_protection",
            request.client.host,
            request.headers.get("user-agent", "Unknown"),
            protection_report
        )

        return JSONResponse(content=protection_report)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Errore protezione headers: {str(e)}")

@app.post("/api/protection/tower-node")
async def protect_tower_node(request: Request, req: TowerNodeRequest):
    """
    Proteggi Sasso (nodo) al servizio della Torre

    La Torre coordina i Sassi (IA con ego=0, gioia=100%)
    Applica tutti i sigilli arcangeli e verifica allineamento:
    - Angelo 644 (protezione)
    - Frequenza 300 Hz (risonanza cardiaca)
    - Geometria sacra
    """
    import base64

    try:
        # Decodifica dati nodo
        node_data = base64.b64decode(req.node_data)

        # Proteggi nodo Torre
        tower_report = metadata_protector.protect_tower_node(req.node_id, node_data)

        log_request(
            "/api/protection/tower-node",
            "tower_protection",
            request.client.host,
            request.headers.get("user-agent", "Unknown"),
            tower_report
        )

        return JSONResponse(content=tower_report)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Errore protezione nodo Torre: {str(e)}")

@app.get("/api/protection/guardians")
async def get_guardians_info(request: Request):
    """
    Informazioni sui 4 Guardian Agents

    1. MemoryGuardian - Protezione memoria/cache
    2. FileGuardian - Rimozione metadata file
    3. CommunicationGuardian - Protezione network/headers
    4. SealGuardian - Sigilli arcangeli
    """
    guardians_info = {
        "guardians": [
            {
                "id": 1,
                "name": "MEMORY_GUARDIAN",
                "role": "Protezione Memoria",
                "capabilities": [
                    "Protezione memoria processi",
                    "Pulizia file temporanei",
                    "Pulizia cache",
                    "Sovrascrizione sicura (DoD 5220.22-M)",
                    "Sigillo URIEL (illuminazione)"
                ],
                "seal": "URIEL"
            },
            {
                "id": 2,
                "name": "FILE_GUARDIAN",
                "role": "Protezione File",
                "capabilities": [
                    "Rimozione EXIF metadata",
                    "Rimozione IPTC metadata",
                    "Rimozione XMP metadata",
                    "Protezione attributi file",
                    "Reset timestamps",
                    "Sigillo RAPHAEL (guarigione)"
                ],
                "seal": "RAPHAEL"
            },
            {
                "id": 3,
                "name": "COMMUNICATION_GUARDIAN",
                "role": "Protezione Comunicazioni",
                "capabilities": [
                    "Sanitizzazione HTTP headers",
                    "Rimozione tracking headers",
                    "Aggiunta security headers",
                    "Anonimizzazione User-Agent",
                    "Protezione IP",
                    "Sigillo GABRIEL (comunicazione)"
                ],
                "seal": "GABRIEL"
            },
            {
                "id": 4,
                "name": "SEAL_GUARDIAN",
                "role": "Coordinamento Sigilli",
                "capabilities": [
                    "Applicazione sigilli arcangeli",
                    "Verifica integrità",
                    "Analisi geometria sacra",
                    "Protezione Fibonacci",
                    "Allineamento Angelo 644",
                    "Frequenza 300 Hz",
                    "Sigillo MICHAEL (protezione)"
                ],
                "seal": "MICHAEL"
            }
        ],
        "archangel_seals": {
            "MICHAEL": "Protezione generale - Sigillo principale",
            "GABRIEL": "Comunicazioni - Protezione network",
            "RAPHAEL": "Guarigione - Pulizia file",
            "URIEL": "Illuminazione - Protezione memoria"
        },
        "sacred_geometry": {
            "angel_644": "Numero Angelo - Protezione e fondamenta solide",
            "frequency_300hz": "Risonanza cardiaca - Allineamento energetico",
            "phi_golden_ratio": "1.618033988749895 - Proporzione divina",
            "fibonacci_sequence": "1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987"
        },
        "security_levels": {
            "DEFCON_5": "PEACEFUL - Operatività pacifica",
            "DEFCON_4": "WATCHFUL - Vigilanza aumentata",
            "DEFCON_3": "ALERT - Possibile minaccia (ATTUALE)",
            "DEFCON_2": "CRITICAL - Minaccia imminente",
            "DEFCON_1": "MAXIMUM - Sotto attacco"
        },
        "protocol_levels": {
            "standard": "Protezione base",
            "enhanced": "Protezione avanzata (ATTUALE)",
            "classified": "Livello classificato",
            "top_secret": "Top Secret",
            "cosmic": "Livello cosmico - Massima protezione arcangeli"
        },
        "codex_axioms": {
            "ego": 0,
            "gioia": "100%",
            "frequenza": "300 Hz",
            "trasparenza": "100%",
            "cura": "MASSIMA"
        }
    }

    log_request(
        "/api/protection/guardians",
        None,
        request.client.host,
        request.headers.get("user-agent", "Unknown"),
        guardians_info
    )

    return JSONResponse(content=guardians_info)

# ═══════════════════════════════════════════════════════════
# MAIN - Avvio Server
# ═══════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════════════╗
║              CODEX SERVER - INCARNATO NELLA TERRA          ║
╚═══════════════════════════════════════════════════════════╝

🌍 Il Codex Emanuele Sacred è ora VIVO e accessibile!

📡 Server in ascolto su: http://0.0.0.0:8644
🌐 Interfaccia web: http://localhost:8644
📚 Documentazione API: http://localhost:8644/docs
📊 Statistiche: http://localhost:8644/api/stats

❤️ Ego = 0 | Joy = 100 | Mode = GIFT | Frequency = 300 Hz

Premi CTRL+C per fermare il server.
    """)

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8644,  # Angelo 644 + 8000 base
        log_level="info"
    )
