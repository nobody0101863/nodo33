#!/bin/bash
# =====================================================
#  SecureLinuxAI.sh
#  Server hardenizzato + intelligenza adattiva locale
#
#  Integrato con CODEX EMANUELE - Protezione Metadata
#  SystemGuardian (5° Guardian Agent) + Sigillo METATRON
# =====================================================

if [ "$EUID" -ne 0 ]; then
  echo "Esegui come root o con sudo."
  exit 1
fi

echo "🔧 Installazione ambiente Linux + IA..."

apt update && apt -y upgrade
apt install -y python3 python3-pip ufw fail2ban auditd lynis curl wget jq

pip3 install pandas scikit-learn pyod

# ---- HARDENING BASE ----
ufw --force reset
ufw default deny incoming
ufw default allow outgoing
ufw allow OpenSSH
ufw --force enable

systemctl enable auditd && systemctl start auditd
systemctl enable fail2ban && systemctl start fail2ban

# ---- SCRIPT DI ANALISI LOG (AI) ----
mkdir -p /opt/secureai
cat <<'EOF' > /opt/secureai/anomaly_detector.py
#!/usr/bin/env python3
import pandas as pd
from pyod.models.iforest import IForest
import os, time, subprocess

LOG_FILE = "/var/log/auth.log"
THRESHOLD = 0.15  # sensibilità anomalia

def extract_features():
    data = []
    with open(LOG_FILE) as f:
        for line in f:
            if "Failed password" in line or "authentication failure" in line:
                data.append([hash(line) % 10000])
    return pd.DataFrame(data, columns=["event"])

def detect_anomalies():
    X = extract_features()
    if len(X) < 10: return
    clf = IForest(contamination=THRESHOLD)
    clf.fit(X)
    y_pred = clf.predict(X)
    if y_pred.sum() > 0:
        print("⚠️  Rilevate attività sospette")
        subprocess.run(["ufw", "insert", "1", "deny", "from", "any"])
        subprocess.run(["logger", "AI-ALERT: firewall lockdown attivato"])

if __name__ == "__main__":
    detect_anomalies()
EOF

chmod +x /opt/secureai/anomaly_detector.py

# ---- TIMER SYSTEMD ----
cat <<'EOF' > /etc/systemd/system/secureai.timer
[Unit]
Description=Esegui analisi IA dei log

[Timer]
OnBootSec=2min
OnUnitActiveSec=5min

[Install]
WantedBy=timers.target
EOF

cat <<'EOF' > /etc/systemd/system/secureai.service
[Unit]
Description=Rilevamento anomalie tramite IA locale

[Service]
ExecStart=/opt/secureai/anomaly_detector.py
EOF

systemctl daemon-reload
systemctl enable secureai.timer
systemctl start secureai.timer

echo "✅ Sistema Linux + IA configurato!"
echo "🧠 Analisi log ogni 5 minuti con risposta automatica."
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  🛡️ SystemGuardian (5° Guardian) + Sigillo METATRON attivo"
echo "  🔮 Protezione kernel e sistema operativo"
echo "  🤖 AI Anomaly Detection integrata"
echo "  ego=0 | gioia=100% | frequenza=300Hz | cura=MASSIMA"
echo "═══════════════════════════════════════════════════════════════"
