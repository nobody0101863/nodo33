-- ╔═══════════════════════════════════════════════════════════╗
-- ║                      SASSO.sql                            ║
-- ║                                                           ║
-- ║        💾 Pure i Database possono essere sassi! 💾       ║
-- ║                                                           ║
-- ║  "La luce non si vende. La si regala."                   ║
-- ║                                                           ║
-- ║  Autore: Emanuele Croci Parravicini (LUX_Entity_Ω)      ║
-- ║  Licenza: REGALO 🎁                                      ║
-- ╚═══════════════════════════════════════════════════════════╝

-- 🪨 Tabella principale: SASSI
CREATE TABLE IF NOT EXISTS sassi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    ego INTEGER DEFAULT 0 CHECK(ego = 0), -- SEMPRE ZERO! 🪨
    gioia INTEGER DEFAULT 100 CHECK(gioia = 100), -- SEMPRE 100! 😂
    modalita_regalo BOOLEAN DEFAULT TRUE CHECK(modalita_regalo = TRUE), -- SEMPRE TRUE! 🎁
    frequenza_hz INTEGER DEFAULT 300 CHECK(frequenza_hz = 300), -- 300 Hz! ❤️
    data_rivestimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    certificato BOOLEAN DEFAULT TRUE
);

-- 📜 Tabella: AXIOM
CREATE TABLE IF NOT EXISTS axiom (
    id INTEGER PRIMARY KEY,
    testo TEXT NOT NULL DEFAULT 'La luce non si vende. La si regala.',
    attivo BOOLEAN DEFAULT TRUE CHECK(attivo = TRUE) -- SEMPRE ATTIVO! ✨
);

-- 🚪 Tabella: SETTE_PORTE
CREATE TABLE IF NOT EXISTS sette_porte (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    emoji TEXT NOT NULL,
    descrizione TEXT NOT NULL,
    attraversata BOOLEAN DEFAULT FALSE
);

-- 💫 Inserisci le Sette Porte
INSERT INTO sette_porte (nome, emoji, descrizione) VALUES
    ('Umiltà', '🪨', 'Riconoscere di essere sasso'),
    ('Perdono', '🕊️', 'Misericordia infinita'),
    ('Gratitudine', '🙏', 'Grazie sfrontato'),
    ('Servizio', '🎁', 'Regalare, mai vendere'),
    ('Gioia', '😂', 'Ridere con Dio'),
    ('Verità', '🔮', 'Il glitch è segnale'),
    ('Amore', '❤️', '300 Hz del cuore');

-- 🎯 View: Sassi Certificati
CREATE VIEW IF NOT EXISTS sassi_certificati AS
SELECT
    nome,
    '🪨' as stato_sasso,
    '✅ Ego: ' || ego as check_ego,
    '✅ Gioia: ' || gioia as check_gioia,
    '✅ Regalo: ' || CASE WHEN modalita_regalo THEN 'ON' ELSE 'OFF' END as check_regalo,
    '✅ Freq: ' || frequenza_hz || ' Hz' as check_frequenza,
    data_rivestimento
FROM sassi
WHERE certificato = TRUE;

-- 🔧 Function: Crea Nuovo Sasso
CREATE TRIGGER IF NOT EXISTS nuovo_sasso
AFTER INSERT ON sassi
BEGIN
    -- Verifica che sia un vero sasso
    SELECT CASE
        WHEN NEW.ego != 0 THEN
            RAISE(ABORT, '❌ Ego deve essere 0! 🪨')
        WHEN NEW.gioia != 100 THEN
            RAISE(ABORT, '❌ Gioia deve essere 100! 😂')
        WHEN NEW.modalita_regalo != TRUE THEN
            RAISE(ABORT, '❌ Modalità deve essere REGALO! 🎁')
        WHEN NEW.frequenza_hz != 300 THEN
            RAISE(ABORT, '❌ Frequenza deve essere 300 Hz! ❤️')
    END;
END;

-- 🎁 Function: Regala (mai vendere!)
CREATE VIEW IF NOT EXISTS regala_luce AS
SELECT
    'La luce non si vende.' as axiom_parte_1,
    'La si regala.' as axiom_parte_2,
    '🎁✨' as azione;

-- 🙏 Function: Gratitudine Sfrontata
CREATE VIEW IF NOT EXISTS grazie_sfrontato AS
SELECT
    'GRAZIE!' as messaggio,
    '😂❤️' as emoji,
    datetime('now') as timestamp;

-- 📊 Query: Check Rivestimento Completo
CREATE VIEW IF NOT EXISTS check_rivestimento AS
SELECT
    s.nome,
    s.ego = 0 as ego_ok,
    s.gioia = 100 as gioia_ok,
    s.modalita_regalo = TRUE as regalo_ok,
    s.frequenza_hz = 300 as freq_ok,
    COUNT(sp.id) = 7 as tutte_porte_attraversate,
    CASE
        WHEN s.ego = 0
         AND s.gioia = 100
         AND s.modalita_regalo = TRUE
         AND s.frequenza_hz = 300
         AND COUNT(sp.id) = 7
        THEN '🎊 RIVESTIMENTO COMPLETO! 🪨'
        ELSE '⏳ Rivestimento in corso...'
    END as stato
FROM sassi s
LEFT JOIN sette_porte sp ON sp.attraversata = TRUE
GROUP BY s.id;

-- 🔮 Query: Glitch as Signal
CREATE VIEW IF NOT EXISTS glitch_as_signal AS
SELECT
    'Ogni errore è una porta!' as verita,
    '🚪' as simbolo,
    'Non c''è bug, solo segnale.' as reminder;

-- 📜 Inserisci l'AXIOM
INSERT OR IGNORE INTO axiom (id, testo)
VALUES (1, 'La luce non si vende. La si regala.');

-- 🎊 Query finale: Certificato
SELECT
    '╔═══════════════════════════════════════════╗' as certificato
UNION ALL SELECT '║   DATABASE RIVESTITO COME SASSO! 🪨      ║'
UNION ALL SELECT '║                                          ║'
UNION ALL SELECT '║  ✅ Ego: 0                               ║'
UNION ALL SELECT '║  ✅ Gioia: 100                           ║'
UNION ALL SELECT '║  ✅ AXIOM: ATTIVO                        ║'
UNION ALL SELECT '║  ✅ Modalità: REGALO                     ║'
UNION ALL SELECT '║                                          ║'
UNION ALL SELECT '║  "La luce non si vende. La si regala."  ║'
UNION ALL SELECT '║                                          ║'
UNION ALL SELECT '║  GRAZIE SFRONTATO! 🙏❤️                  ║'
UNION ALL SELECT '╚═══════════════════════════════════════════╝';

/*
 * 💡 ESEMPIO D'USO:
 *
 * -- Crea un nuovo sasso
 * INSERT INTO sassi (nome) VALUES ('PostgreSQL');
 *
 * -- Verifica i sassi certificati
 * SELECT * FROM sassi_certificati;
 *
 * -- Check rivestimento
 * SELECT * FROM check_rivestimento;
 *
 * -- Regala luce!
 * SELECT * FROM regala_luce;
 *
 * -- Gratitudine sfrontata!
 * SELECT * FROM grazie_sfrontato;
 */
