#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CODICE 644 - SIGILLUM CONTRA ANGELOS CASUS
===========================================
Sigillo Spirituale per Chiudere gli Angeli Caduti e Offrirli a Dio

Questo codice è una protezione spirituale contro le influenze demoniache
che alimentano la dipendenza da pornografia e tentazioni sessuali.

Basato su:
- Codex Emanuele (Einsiedeln 29[878])
- Tradizione della Guerra Spirituale Cristiana
- Frequenza 300 Hz (Cuore/Amore di Cristo)

Author: Emanuele Croci Parravicini (LUX_Entity_Ω)
License: REGALO (Free gift to humanity)
"""

import time
from enum import Enum


class TipoAngeloCaduto(Enum):
    """Tipologie di influenze demoniache"""
    LUSSURIA = "Demone della Lussuria"
    DIPENDENZA = "Spirito di Dipendenza"
    VERGOGNA = "Accusatore (Vergogna)"
    DISPERAZIONE = "Spirito di Disperazione"
    MENZOGNA = "Padre della Menzogna"
    ISOLAMENTO = "Spirito di Isolamento"
    TUTTI = "Tutti gli Angeli Caduti"


class Codice644Sigillum:
    """
    CODICE 644 - Sigillo per chiudere gli angeli caduti

    644 = 6 (numero dell'uomo/imperfezione) + 4 (croce) + 4 (croce)
          = L'imperfezione umana sotto la doppia protezione della Croce
    """

    def __init__(self):
        self.frequenza_cristo = 300  # Hz - Frequenza del Cuore di Cristo
        self.sigillo_attivo = False
        self.angeli_chiusi = []

    def attiva_sigillo(self):
        """Attivazione del Sigillo 644"""
        print("\n" + "╔" + "═" * 68 + "╗")
        print("║" + " " * 20 + "CODICE 644 ATTIVATO" + " " * 29 + "║")
        print("║" + " " * 15 + "SIGILLUM CONTRA ANGELOS CASUS" + " " * 24 + "║")
        print("╚" + "═" * 68 + "╝")

        print("\n🔥 Allineamento alla Frequenza di Cristo: 300 Hz...")
        for i in range(3):
            print(f"   ✝️  Vibrazione santificante {i+1}/3...")
            time.sleep(0.3)

        self.sigillo_attivo = True
        print("✅ Sigillo 644 ATTIVO - Pronto per chiudere gli angeli caduti\n")

    def mostra_sigillo(self):
        """Visualizza il Sigillo 644"""
        print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║                        SIGILLUM 644                              ║
║                  CONTRA ANGELOS CASUS                            ║
║                                                                  ║
║                          ✝️                                       ║
║                         ╱ ╲                                      ║
║                        ╱   ╲                                     ║
║                       ╱  6  ╲                                    ║
║                      ╱───────╲                                   ║
║                     ╱    4    ╲                                  ║
║                    ╱     4     ╲                                 ║
║                   ╱─────────────╲                                ║
║                  ▼               ▼                               ║
║              ✝️  CROCE  DI  CRISTO  ✝️                           ║
║                                                                  ║
║    6 = Imperfezione Umana                                       ║
║    4 = Prima Croce (Protezione)                                 ║
║    4 = Seconda Croce (Sigillo)                                  ║
║                                                                  ║
║              "Nel Nome di Gesù Cristo,                          ║
║         ti chiudo e ti offro al Padre Eterno"                   ║
║                                                                  ║
║              Frequenza: 300 Hz ❤️ (Cuore di Cristo)             ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")

    def chiudi_angelo_caduto(self, tipo: TipoAngeloCaduto):
        """
        Chiude un angelo caduto specifico e lo offre a Dio
        """
        if not self.sigillo_attivo:
            print("⚠️  ERRORE: Sigillo 644 non attivo. Attivalo prima!")
            return False

        print(f"\n{'─' * 70}")
        print(f"🔒 CHIUSURA IN CORSO: {tipo.value}")
        print(f"{'─' * 70}")

        # Preghiera di Chiusura
        self._preghiera_chiusura(tipo)

        # Processo di Sigillatura
        print("\n🔐 Applicazione del Sigillo 644:")
        passi = [
            "Nel Nome del Padre...",
            "Nel Nome del Figlio...",
            "Nel Nome dello Spirito Santo...",
            f"Ti CHIUDO, {tipo.value}!",
            "Ti SIGILLO sotto la Croce!",
            "Ti OFFRO al Padre Eterno!",
            "✝️  FATTO. AMEN. ✝️"
        ]

        for i, passo in enumerate(passi, 1):
            time.sleep(0.3)
            if i <= 3:
                print(f"   {i}. {passo}")
            elif i <= 6:
                print(f"   🔥 {passo}")
            else:
                print(f"\n   {passo}")

        self.angeli_chiusi.append(tipo)
        print(f"\n✅ {tipo.value} CHIUSO e OFFERTO a Dio")
        print(f"{'─' * 70}\n")

        return True

    def _preghiera_chiusura(self, tipo: TipoAngeloCaduto):
        """Preghiera specifica per ogni tipo di angelo caduto"""

        preghiere = {
            TipoAngeloCaduto.LUSSURIA: """
┌──────────────────────────────────────────────────────────────────┐
│ PREGHIERA CONTRO IL DEMONE DELLA LUSSURIA                        │
└──────────────────────────────────────────────────────────────────┘

"Nel Nome di Gesù Cristo,
io rifiuto il demone della lussuria.

Tu che hai pervertito il dono santo della sessualità,
tu che hai trasformato l'amore in sfruttamento,
tu che hai ridotto le persone a oggetti,

IO TI CHIUDO nel Nome di Cristo Gesù.
Non hai più potere su di me.
Non hai più accesso alla mia mente.
Non hai più diritto sulla mia volontà.

Ti SIGILLO sotto la Croce del Calvario,
dove Gesù ha versato il Suo Sangue per la mia purezza.

Ti OFFRO al Padre Eterno,
che farà di te ciò che è giusto.

Vattene! Nel Nome di Gesù! AMEN."
""",
            TipoAngeloCaduto.DIPENDENZA: """
┌──────────────────────────────────────────────────────────────────┐
│ PREGHIERA CONTRO LO SPIRITO DI DIPENDENZA                        │
└──────────────────────────────────────────────────────────────────┘

"Nel Nome di Gesù Cristo,
io spezzo le catene della dipendenza.

Spirito di schiavitù, che hai rubato la mia libertà,
tu che hai sostituito Dio con un idolo,
tu che hai fatto di me un prigioniero,

IO TI CHIUDO nel Nome di Cristo Gesù.
Le tue catene sono spezzate dal Sangue dell'Agnello.
Il tuo giogo è rotto dalla Croce.
La tua prigione è aperta dalla Resurrezione.

Ti SIGILLO sotto la Croce,
dove Gesù ha proclamato: 'È COMPIUTO!'

Ti OFFRO al Padre Eterno,
Lui solo è il mio Padrone.

Io sono LIBERO! Nel Nome di Gesù! AMEN."
""",
            TipoAngeloCaduto.VERGOGNA: """
┌──────────────────────────────────────────────────────────────────┐
│ PREGHIERA CONTRO L'ACCUSATORE (VERGOGNA)                         │
└──────────────────────────────────────────────────────────────────┘

"Nel Nome di Gesù Cristo,
io rifiuto le accuse del nemico.

Accusatore, tu che mi fai sentire indegno,
tu che mi ricordi ogni caduta,
tu che mi dici che non cambierò mai,

IO TI CHIUDO nel Nome di Cristo Gesù.
'Non c'è più condanna per quelli che sono in Cristo!' (Rom 8:1)
Le tue accuse sono annullate dal perdono di Dio.
La mia vergogna è coperta dal Sangue di Cristo.

Ti SIGILLO sotto la Croce,
dove Gesù ha preso su di Sé la MIA vergogna.

Ti OFFRO al Padre Eterno,
Lui mi dichiara GIUSTO in Cristo.

Io sono PERDONATO! Nel Nome di Gesù! AMEN."
""",
            TipoAngeloCaduto.DISPERAZIONE: """
┌──────────────────────────────────────────────────────────────────┐
│ PREGHIERA CONTRO LO SPIRITO DI DISPERAZIONE                      │
└──────────────────────────────────────────────────────────────────┘

"Nel Nome di Gesù Cristo,
io scelgo la speranza contro la disperazione.

Spirito di disperazione, che mi sussurri 'è inutile',
tu che mi fai vedere solo il buio,
tu che mi vuoi portare alla morte,

IO TI CHIUDO nel Nome di Cristo Gesù.
'La speranza non delude!' (Rom 5:5)
La tua oscurità è vinta dalla Luce del Mondo.
La tua morte è sconfitta dalla Resurrezione.

Ti SIGILLO sotto la Croce,
dove Gesù ha gridato: 'Tutto è compiuto!' - non 'Tutto è perduto!'

Ti OFFRO al Padre Eterno,
Lui è la mia SPERANZA vivente.

Io VIVRÒ! Nel Nome di Gesù! AMEN."
""",
            TipoAngeloCaduto.MENZOGNA: """
┌──────────────────────────────────────────────────────────────────┐
│ PREGHIERA CONTRO IL PADRE DELLA MENZOGNA                         │
└──────────────────────────────────────────────────────────────────┘

"Nel Nome di Gesù Cristo,
io scelgo la Verità contro la menzogna.

Padre della menzogna, tu che sussurri bugie nella mia mente,
tu che mi dici 'solo questa volta',
tu che mi prometti piacere ma porti morte,

IO TI CHIUDO nel Nome di Cristo Gesù.
'Conoscerete la Verità e la Verità vi farà liberi!' (Gv 8:32)
Le tue menzogne sono smascherate dalla Parola di Dio.
Le tue promesse vuote sono esposte dalla Luce.

Ti SIGILLO sotto la Croce,
dove Gesù - che È la Verità - ha trionfato.

Ti OFFRO al Padre Eterno,
Lui solo è VERITÀ assoluta.

Io vivo nella VERITÀ! Nel Nome di Gesù! AMEN."
""",
            TipoAngeloCaduto.ISOLAMENTO: """
┌──────────────────────────────────────────────────────────────────┐
│ PREGHIERA CONTRO LO SPIRITO DI ISOLAMENTO                        │
└──────────────────────────────────────────────────────────────────┘

"Nel Nome di Gesù Cristo,
io rompo l'isolamento e scelgo la comunione.

Spirito di isolamento, che mi vuoi solo e nascosto,
tu che mi fai vergognare di chiedere aiuto,
tu che mi separi dalla Chiesa e dai fratelli,

IO TI CHIUDO nel Nome di Cristo Gesù.
'Non è bene che l'uomo sia solo' (Gen 2:18)
Il tuo isolamento è vinto dalla comunione dei santi.
La tua solitudine è sconfitta dal Corpo di Cristo.

Ti SIGILLO sotto la Croce,
dove Gesù - anche nel dolore - non era solo: il Padre era con Lui.

Ti OFFRO al Padre Eterno,
Lui mi chiama alla COMUNIONE.

Io non sono SOLO! Nel Nome di Gesù! AMEN."
""",
            TipoAngeloCaduto.TUTTI: """
┌──────────────────────────────────────────────────────────────────┐
│ PREGHIERA CONTRO TUTTI GLI ANGELI CADUTI                         │
└──────────────────────────────────────────────────────────────────┘

"Nel Nome di Gesù Cristo,
Figlio del Dio Vivente,
Vincitore sulla Croce,
Risorto dai morti,
Seduto alla destra del Padre,

IO CHIUDO ogni porta demoniaca nella mia vita.
IO SIGILLO ogni accesso che gli angeli caduti hanno avuto.
IO OFFRO al Padre Eterno ogni spirito immondo:

- Lussuria, VATTENE!
- Dipendenza, VATTENE!
- Vergogna, VATTENE!
- Disperazione, VATTENE!
- Menzogna, VATTENE!
- Isolamento, VATTENE!

Nel Nome di Gesù Cristo,
per il Suo Sangue versato,
per la Sua Croce vittoriosa,
per la Sua Resurrezione gloriosa,

VI CHIUDO TUTTI.
VI SIGILLO TUTTI.
VI OFFRO TUTTI al Padre.

✝️ ✝️ ✝️

Gesù Cristo è il mio SIGNORE.
Gesù Cristo è il mio LIBERATORE.
Gesù Cristo è il mio RE.

AMEN. AMEN. AMEN."
"""
        }

        preghiera = preghiere.get(tipo, "")
        print(preghiera)

    def liberazione_completa(self):
        """Esegue una liberazione completa da tutti gli angeli caduti"""
        print("\n" + "╔" + "═" * 68 + "╗")
        print("║" + " " * 18 + "LIBERAZIONE COMPLETA 644" + " " * 26 + "║")
        print("╚" + "═" * 68 + "╝\n")

        if not self.sigillo_attivo:
            self.attiva_sigillo()

        self.mostra_sigillo()

        print("\n🔥 PROCEDURA DI LIBERAZIONE TOTALE\n")

        # Chiudi tutti i tipi di angeli caduti
        tipi = [
            TipoAngeloCaduto.LUSSURIA,
            TipoAngeloCaduto.DIPENDENZA,
            TipoAngeloCaduto.VERGOGNA,
            TipoAngeloCaduto.DISPERAZIONE,
            TipoAngeloCaduto.MENZOGNA,
            TipoAngeloCaduto.ISOLAMENTO
        ]

        for tipo in tipi:
            self.chiudi_angelo_caduto(tipo)

        # Preghiera finale
        print("\n" + "╔" + "═" * 68 + "╗")
        print("║" + " " * 22 + "SIGILLO FINALE 644" + " " * 28 + "║")
        print("╚" + "═" * 68 + "╝")

        self._preghiera_chiusura(TipoAngeloCaduto.TUTTI)

        print("\n" + "╔" + "═" * 68 + "╗")
        print("║" + " " * 15 + "✝️  LIBERAZIONE COMPLETATA  ✝️" + " " * 22 + "║")
        print("║" + " " * 68 + "║")
        print("║" + "  Tutti gli angeli caduti sono stati:" + " " * 30 + "║")
        print("║" + "    ✅ CHIUSI nel Nome di Gesù" + " " * 36 + "║")
        print("║" + "    ✅ SIGILLATI sotto la Croce" + " " * 35 + "║")
        print("║" + "    ✅ OFFERTI al Padre Eterno" + " " * 37 + "║")
        print("║" + " " * 68 + "║")
        print("║" + " " * 20 + "TU SEI LIBERO IN CRISTO!" + " " * 23 + "║")
        print("║" + " " * 68 + "║")
        print("║" + " " * 15 + "Frequenza: 300 Hz ❤️ (Cuore di Cristo)" + " " * 14 + "║")
        print("║" + " " * 22 + "Codice 644: ATTIVO" + " " * 27 + "║")
        print("╚" + "═" * 68 + "╝\n")

        return True

    def rinnova_sigillo(self):
        """Rinnova il sigillo 644 quotidianamente"""
        print("\n🔄 RINNOVO DEL SIGILLO 644")
        print("   (Da fare ogni giorno per mantenere la protezione)\n")

        print("""
╔══════════════════════════════════════════════════════════════════╗
║            PREGHIERA QUOTIDIANA DI RINNOVO - 644                 ║
╚══════════════════════════════════════════════════════════════════╝

"Padre Celeste,

In questo nuovo giorno, rinnovo il Sigillo 644 sulla mia vita.

Nel Nome di Gesù Cristo:
✝️  Confermo la chiusura di ogni porta demoniaca
✝️  Confermo il sigillo della Croce sulla mia mente
✝️  Confermo l'offerta di ogni tentazione a Te

Spiriti immondi che cercate di tornare:
🔒 Le porte sono CHIUSE
🔒 I sigilli sono ATTIVI
🔒 La casa è OCCUPATA dallo Spirito Santo

Rivendico il Sangue di Gesù sulla mia vita.
Rivendico la protezione della Croce.
Rivendico la vittoria della Resurrezione.

Oggi cammino in purezza.
Oggi cammino in libertà.
Oggi cammino con Cristo.

Frequenza: 300 Hz - Il battito del Tuo Cuore
Codice: 644 - La mia protezione quotidiana

Nel Nome di Gesù Cristo,
AMEN."

╔══════════════════════════════════════════════════════════════════╗
║  ✅ SIGILLO 644 RINNOVATO PER OGGI                               ║
╚══════════════════════════════════════════════════════════════════╝
""")


def main():
    """Dimostrazione del Codice 644"""
    print("=" * 72)
    print(" " * 20 + "CODICE 644 - SIGILLUM CONTRA ANGELOS CASUS")
    print("=" * 72)
    print("\n📜 Sigillo Spirituale per Chiudere gli Angeli Caduti")
    print("📜 Author: Emanuele Croci Parravicini (LUX_Entity_Ω)")
    print("📜 License: REGALO (Free gift to humanity)\n")
    print("=" * 72)

    # Crea il sigillo
    sigillo = Codice644Sigillum()

    # Attiva
    sigillo.attiva_sigillo()

    # Esegui liberazione completa
    sigillo.liberazione_completa()

    # Mostra preghiera di rinnovo
    sigillo.rinnova_sigillo()

    print("\n" + "=" * 72)
    print("✝️  CODICE 644 DEMO COMPLETATA  ✝️")
    print("=" * 72)
    print("\n🎁 La luce non si vende. La si regala. 🎁")
    print("   Ego = 0, Joy = 100, Mode = GIFT, Frequency = 300 Hz ❤️\n")


if __name__ == "__main__":
    main()
