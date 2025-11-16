# 💾 SCHEMA METADATI NODO33
## Struttura Dati per il Progetto Sasso Digitale

**Versione:** 1.0.0
**Data:** 16 Novembre 2025
**Autore:** Emanuele Croci Parravicini (LUX_Entity_Ω)
**Licenza:** CC0 1.0 Universal (Pubblico Dominio)

---

```
═══════════════════════════════════════════════════════════════
                💾 SCHEMA METADATI NODO33 💾
            La Luce che Descrive la Sapienza del Sasso
═══════════════════════════════════════════════════════════════

                     Dati Terreni 🪨
                      Dati Etici ⚖️
                   Dati Spirituali ❤️

═══════════════════════════════════════════════════════════════
```

---

## 🌟 FILOSOFIA DELLO SCHEMA

I metadati non sono solo "informazioni tecniche". Sono la **luce che descrive la Sapienza del sasso**.

Ogni campo ha uno scopo etico e spirituale:

> *"I metadati sono il Dono che accompagna il Dono.
> Senza di essi, il sasso è muto.
> Con essi, il sasso parla attraverso i secoli."*

### Tre Dimensioni Integrate

Questo schema unisce tre dimensioni inscindibili:

1. **🪨 Dati Terreni** - La realtà fisica della pietra
2. **⚖️ Dati Etici** - L'applicazione del Codex Emanuele
3. **❤️ Dati Spirituali** - Il cuore e la sapienza trasmessa

---

## 📋 SCHEMA COMPLETO (YAML)

```yaml
# ═══════════════════════════════════════════════════════════════
# SASSO DIGITALE - METADATI COMPLETI
# Schema v1.0.0 - Codex Emanuele Compliant
# ═══════════════════════════════════════════════════════════════

# ───────────────────────────────────────────────────────────────
# A. DATI TERRENI - La Pietra Fisica 🪨
# ───────────────────────────────────────────────────────────────

dati_terreni:

  # Identificatore Unico
  id_nodo33: "SASSO-RUS-KIJI-001"
  uri_permanente: "https://nodo33.org/sassi/SASSO-RUS-KIJI-001"
  doi: "10.5281/zenodo.1234567"  # DOI opzionale via Zenodo

  # Denominazione
  nome_pietra:
    it: "Ciottolo di Fondazione della Chiesa di Kiži"
    en: "Foundation Pebble of Kizhi Church"
    ru: "Камень фундамента церкви Кижи"
    la: "Lapis Fundamenti Ecclesiae Kiži"

  # Contesto Storico-Geografico
  contesto:
    luogo_ritrovamento:
      comune: "Kiži"
      provincia: "Repubblica di Carelia"
      regione: "Russia Nord-Occidentale"
      coordinate:
        lat: 62.0667
        lon: 35.2167
        precisione: "100m"  # Oscurato per protezione
      note: "Isola di Kiži, Lago Onega"

    datazione:
      periodo: "XVII secolo"
      anno_stimato: 1714
      metodo: "Analisi stratigrafica e documentazione storica"
      certezza: "Alta"

    tipologia:
      categoria_archeologica: "Pietra di fondazione"
      funzione_originale: "Elemento strutturale - base angolare"
      contesto_uso: "Costruzione della Chiesa della Trasfigurazione"

  # Caratteristiche Fisiche
  fisica:
    materiale:
      tipo_roccia: "Granito della Carelia"
      composizione: "Feldspato, quarzo, mica"
      colore: "Grigio-rosato con venature scure"

    dimensioni:
      lunghezza: 28.5  # cm
      larghezza: 18.2
      altezza: 15.0
      peso: 12.3  # kg
      unita: "metric"

    conservazione:
      stato: "Buono"
      integrità: "95%"
      danni: "Lieve erosione superficiale da agenti atmosferici"
      interventi: "Nessun restauro, conservazione naturale"
      note: "Superficie levigata dal tempo, patina nobile"

  # Collezione e Custodia
  custodia:
    collocazione_attuale:
      tipo: "Museo"
      istituzione: "Museo Storico-Architettonico di Kiži"
      città: "Petrozavodsk"
      paese: "Russia"

    inventario:
      numero: "KIZ-FOND-1714-001"
      data_acquisizione: "1960-07-15"
      modalità: "Scavo archeologico autorizzato"

    accessibilità:
      pubblica: true
      orari: "09:00-18:00 (Mag-Set)"
      permessi_necessari: false

# ───────────────────────────────────────────────────────────────
# B. DATI ETICI - Il Codex Emanuele ⚖️
# ───────────────────────────────────────────────────────────────

dati_etici:

  # Licenza di Dono (OBBLIGATORIA)
  licenza:
    tipo: "CC0-1.0"
    nome_completo: "Creative Commons Zero v1.0 Universal"
    url: "https://creativecommons.org/publicdomain/zero/1.0/"
    dichiarazione: |
      Questo sasso digitale e tutti i suoi metadati sono rilasciati
      in PUBBLICO DOMINIO. Nessun diritto riservato.
      La luce non si vende. La si regala.

    attribuzione_richiesta: false
    attribuzione_gradita: true
    attribuzione_suggerita: |
      Progetto Sasso Digitale - Nodo33
      Museo Storico-Architettonico di Kiži
      Licenza: CC0 1.0 (Pubblico Dominio)

  # Finalità del Nodo (Metrica Etica)
  finalità:
    ego: 0  # Metrica fondamentale del Codex
    commercialità: false
    scopo_primario: "Preservazione culturale e educazione pubblica"
    scopi_consentiti:
      - "Ricerca scientifica"
      - "Educazione e didattica"
      - "Contemplazione culturale"
      - "Divulgazione storica"
      - "Stampa 3D per scuole e musei"
      - "Realtà virtuale/aumentata educativa"

    scopi_scoraggiati:  # Non vietati, ma eticamente sconsigliati
      - "Vendita esclusiva dei dati raw"
      - "Uso per replica commerciale senza valore aggiunto"
      - "Manipolazione storica o propaganda"

  # Provenienza Digitale (Trasparenza)
  provenienza_digitale:
    metodo_scansione: "Fotogrammetria Structure from Motion (SfM)"
    software:
      acquisizione: "Agisoft Metashape Professional 2.0"
      elaborazione: "CloudCompare 2.13 + MeshLab 2023.12"
      formato_output: "OBJ + MTL + JPEG textures"

    operatori:
      principale:
        nome: "Dr. Olga Petrova"
        affiliazione: "Università di Petrozavodsk, Dip. Archeologia"
        orcid: "0000-0002-1234-5678"
        contatto: "o.petrova@petrsu.ru"

      assistenti:
        - nome: "Ivan Sokolov"
          ruolo: "Fotografo tecnico"
        - nome: "Marina Volkova"
          ruolo: "Archeologa supervisore"

    data_scansione: "2024-08-15"
    durata_scansione: "3 ore"
    numero_foto: 342
    risoluzione_texture: "4096x4096 px"

    condizioni_scansione:
      illuminazione: "Luce naturale diffusa + LED supplementari"
      temperatura: "18°C"
      umidità: "55%"
      note: "Scansione in condizioni controllate di laboratorio"

    qualità_metrica:
      risoluzione_geometrica: "0.2 mm"
      accuratezza_colorimetrica: "Delta E < 2.0"
      completezza_superficie: "98.5%"
      rumore_mesh: "< 0.1 mm"

  # Peer Review e Validazione
  validazione:
    peer_reviewed: true
    revisori:
      - nome: "Prof. Sergei Ivanov"
        affiliazione: "Accademia Russa delle Scienze, Istituto Archeologia"
        data_review: "2024-09-10"
        esito: "Approvato con lode"
        note: "Scansione di eccellente qualità scientifica"

      - nome: "Dr.ssa Elena Kuznetsova"
        affiliazione: "Museo Hermitage, Laboratorio Conservazione"
        data_review: "2024-09-12"
        esito: "Approvato"

    certificazione_scientifica:
      standard: "CIDOC-CRM + Dublin Core"
      conformità: "ISO 19157:2013 (Data quality)"
      audit_etico: "Codex Emanuele v1.0 - Score 95/100"

  # Impatto e Cura
  impatto:
    cura_ambientale:
      carbon_footprint_scansione: "1.2 kg CO2eq"
      compensazione: "1 albero piantato via Treedom"
      certificato: "https://treedom.net/it/user/nodo33/event/kiji-001"

    accessibilità:
      wcag_compliance: "AA"
      formati_alternativi:
        - "Modello 3D semplificato per mobile"
        - "Foto 2D ad alta risoluzione"
        - "Descrizione testuale dettagliata"
        - "Audio-descrizione (russo, italiano, inglese)"

    riuso_documentato:
      citazioni: 0  # Da aggiornare
      download: 0  # Da aggiornare
      progetti_derivati: []

# ───────────────────────────────────────────────────────────────
# C. DATI SPIRITUALI - Il Cuore e la Sapienza ❤️
# ───────────────────────────────────────────────────────────────

dati_spirituali:

  # Categoria Simbolica
  categoria_simbolica:
    primaria: "Pietra Viva"
    secondarie:
      - "Pietra della Carità"
      - "Pietra di Fondazione"
      - "Pietra del Servizio Nascosto"

    tradizione: "Cristiana Ortodossa"

  # Motivazione Etica - Il Dono
  motivazione_etica:
    titolo: "Il Servizio Anonimo del Costruttore Umile"

    racconto: |
      Questo ciottolo, levigato dal Lago Onega e scelto con cura,
      fu posto come pietra angolare della Chiesa della Trasfigurazione
      di Kiži nel 1714.

      Il costruttore che lo posò - di cui non conosciamo il nome -
      compì un atto di servizio puro: nessuno avrebbe visto questa
      pietra, sepolta nelle fondamenta. Eppure, senza di essa,
      la chiesa - capolavoro dell'architettura lignea russa con le
      sue 22 cupole - non avrebbe potuto reggersi.

      La pietra incarna ego=0: la grandezza che non cerca
      riconoscimento. L'umiltà che sostiene la bellezza visibile.
      Il dono nascosto che rende possibile la luce.

      Come il costruttore anonimo regalò la sua abilità senza
      cercare fama, così noi doniamo questa digitalizzazione
      senza cercare profitto.

      La luce non si vende. La si regala.

    valori_incarnati:
      - "Umiltà (ego=0)"
      - "Servizio disinteressato"
      - "Fondamento invisibile ma essenziale"
      - "Bellezza che sostiene altra bellezza"
      - "Anonimato come virtù"

  # Verso/Ispirazione
  ispirazione:
    fonte: "Bibbia"
    riferimento: "1 Pietro 2:4-5"
    testo:
      it: |
        "Avvicinandovi a lui, pietra viva, rifiutata dagli uomini
        ma scelta e preziosa davanti a Dio, anche voi venite impiegati
        come pietre vive per la costruzione di un edificio spirituale."

      la: |
        "Ad quem accedentes lapidem vivum ab hominibus quidem
        reprobatum a Deo autem electum et honorificatum et ipsi
        tamquam lapides vivi aedificamini."

      en: |
        "Coming to Him as to a living stone, rejected indeed by men,
        but chosen by God and precious, you also, as living stones,
        are being built up a spiritual house."

      ru: |
        "Приступая к Нему, камню живому, человеками отверженному,
        но Богом избранному, драгоценному, и сами, как живые камни,
        устрояйте из себя дом духовный."

    connessione: |
      Come la pietra viva del versetto, questo ciottolo è piccolo
      e apparentemente insignificante, ma è stato "scelto" per un
      compito prezioso: sostenere un luogo di preghiera.

      Il costruttore che lo posò, come noi che lo digitalizziamo,
      siamo "pietre vive" chiamate a servire qualcosa di più grande
      di noi stessi.

  # Meditazione e Contemplazione
  meditazione:
    domanda_contemplativa: |
      Se questa pietra, nascosta per 300 anni nelle fondamenta,
      ha sostenuto la bellezza di 22 cupole dorate...

      quale "pietra nascosta" nella tua vita sta sostenendo
      qualcosa di bello senza che tu te ne accorga?

    invito: |
      Guarda questo sasso non solo come oggetto storico,
      ma come specchio spirituale.

      Chiedi a te stesso:
      - Dove servo senza cercare riconoscimento?
      - Quale mia "fondazione invisibile" sostiene altri?
      - Come posso essere "pietra viva" oggi?

  # Connessione con il Codex Emanuele
  connessione_codex:
    porta_principale: "Porta 1 - Umiltà (Pietra)"
    porte_secondarie:
      - "Porta 3 - Gratitudine (per il costruttore anonimo)"
      - "Porta 4 - Servizio (il dono nascosto)"
      - "Porta 7 - Amore (frequenza 300Hz della bellezza)"

    principi_incarnati:
      ego: 0
      gioia: 100
      mode: "REGALO"
      frequenza: 300
      cura: "MASSIMA"

    messaggio_finale: |
      Questo sasso digitale è il nostro modo di onorare il
      costruttore anonimo di 300 anni fa.

      Come lui regalò la sua opera, noi regaliamo questa memoria.
      Come la sua pietra sostiene ancora oggi, questa digitalizzazione
      sosterrà la memoria per i prossimi 300 anni.

      Sempre grazie a Lui. ❤️

# ───────────────────────────────────────────────────────────────
# METADATA TECNICI (Per interoperabilità)
# ───────────────────────────────────────────────────────────────

metadata_tecnici:
  schema_version: "1.0.0"
  schema_uri: "https://nodo33.org/schemas/sasso-digitale/v1.0.0"
  created: "2024-08-15T14:30:00Z"
  modified: "2024-09-12T10:15:00Z"
  language: "it"
  languages_available: ["it", "en", "ru", "la"]

  # Standard di riferimento
  standards:
    - name: "Dublin Core"
      version: "1.1"
      url: "https://www.dublincore.org/specifications/dublin-core/"
    - name: "CIDOC-CRM"
      version: "7.1.1"
      url: "http://www.cidoc-crm.org/"
    - name: "LIDO"
      version: "1.1"
      url: "http://www.lido-schema.org/"

  # File associati
  files:
    modello_3d_alta:
      path: "models/SASSO-RUS-KIJI-001_high.obj"
      size: 45_230_000  # bytes
      format: "OBJ"
      checksum_sha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"

    modello_3d_web:
      path: "models/SASSO-RUS-KIJI-001_web.glb"
      size: 2_500_000
      format: "GLB"
      checksum_sha256: "..."

    foto_alta_risoluzione:
      path: "photos/SASSO-RUS-KIJI-001_4K.tif"
      size: 120_000_000
      format: "TIFF"
      checksum_sha256: "..."

    metadata:
      path: "metadata/SASSO-RUS-KIJI-001.yaml"
      size: 15_400
      format: "YAML"
      checksum_sha256: "..."

# ═══════════════════════════════════════════════════════════════
# FINE SCHEMA METADATI
# ═══════════════════════════════════════════════════════════════
```

---

## 📊 SCHEMA JSON (Per API e Interoperabilità)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Sasso Digitale Nodo33",
  "description": "Schema metadati completo per digitalizzazione etica di reperti lapidei",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "dati_terreni",
    "dati_etici",
    "dati_spirituali"
  ],
  "properties": {
    "dati_terreni": {
      "type": "object",
      "required": ["id_nodo33", "nome_pietra", "contesto", "fisica"],
      "properties": {
        "id_nodo33": {
          "type": "string",
          "pattern": "^SASSO-[A-Z]{3}-[A-Z0-9]+-[0-9]{3}$",
          "description": "Identificatore unico formato: SASSO-{PAESE}-{LUOGO}-{NUMERO}"
        },
        "nome_pietra": {
          "type": "object",
          "required": ["it"],
          "properties": {
            "it": {"type": "string"},
            "en": {"type": "string"},
            "la": {"type": "string"}
          }
        }
      }
    },
    "dati_etici": {
      "type": "object",
      "required": ["licenza", "finalità", "provenienza_digitale"],
      "properties": {
        "licenza": {
          "type": "object",
          "required": ["tipo"],
          "properties": {
            "tipo": {
              "type": "string",
              "enum": ["CC0-1.0"],
              "description": "Solo CC0 consentito per Codex Emanuele compliance"
            }
          }
        },
        "finalità": {
          "type": "object",
          "required": ["ego"],
          "properties": {
            "ego": {
              "type": "number",
              "const": 0,
              "description": "Deve essere sempre 0 per Codex Emanuele compliance"
            }
          }
        }
      }
    },
    "dati_spirituali": {
      "type": "object",
      "required": ["categoria_simbolica", "motivazione_etica", "ispirazione"],
      "properties": {
        "categoria_simbolica": {
          "type": "object",
          "properties": {
            "primaria": {
              "type": "string",
              "enum": [
                "Pietra Viva",
                "Pietra della Carità",
                "Pietra Scartata",
                "Pietra di Fondazione",
                "Lapide Votiva del Dono"
              ]
            }
          }
        }
      }
    }
  }
}
```

---

## 🎯 ESEMPIO PRATICO - Sasso Etrusco

```yaml
# Esempio più semplice: Cippo Etrusco di Fiesole

dati_terreni:
  id_nodo33: "SASSO-ITA-FIES-001"
  uri_permanente: "https://nodo33.org/sassi/SASSO-ITA-FIES-001"

  nome_pietra:
    it: "Cippo Confinario Etrusco di Fiesole"
    en: "Etruscan Boundary Stone of Fiesole"
    la: "Cippus Finalis Etruscus Faesulae"

  contesto:
    luogo_ritrovamento:
      comune: "Fiesole"
      provincia: "Firenze"
      regione: "Toscana"
      coordinate:
        lat: 43.8063
        lon: 11.2948
        precisione: "comune"  # Volutamente vaga per protezione

    datazione:
      periodo: "VI secolo a.C."
      certezza: "Alta"

    tipologia:
      categoria_archeologica: "Cippo confinario"
      funzione_originale: "Marcatore di confine territoriale"

  fisica:
    materiale:
      tipo_roccia: "Pietra serena"
    dimensioni:
      altezza: 120  # cm
      larghezza: 40
      peso: 85  # kg
    conservazione:
      stato: "Buono"
      integrità: "90%"

dati_etici:
  licenza:
    tipo: "CC0-1.0"
    dichiarazione: "Pubblico Dominio. La luce non si vende."

  finalità:
    ego: 0
    commercialità: false
    scopo_primario: "Preservazione culturale etrusca"

  provenienza_digitale:
    metodo_scansione: "Fotogrammetria SfM"
    software:
      acquisizione: "Agisoft Metashape"
    operatori:
      principale:
        nome: "Dr. Maria Rossi"
        affiliazione: "Università di Firenze"
    data_scansione: "2025-03-15"

  validazione:
    peer_reviewed: true

dati_spirituali:
  categoria_simbolica:
    primaria: "Pietra del Confine Sacro"
    tradizione: "Etrusca"

  motivazione_etica:
    titolo: "Il Confine come Servizio alla Comunità"
    racconto: |
      Questo cippo non divideva per separare, ma per chiarire.
      Segnava dove finiva un territorio e iniziava l'altro,
      permettendo a due comunità di convivere in pace.

      Il confine non è un muro, ma un punto di incontro.
      La pietra serviva entrambe le parti, donando chiarezza.

  ispirazione:
    fonte: "Proverbi"
    riferimento: "Proverbi 22:28"
    testo:
      it: "Non spostare il cippo antico che i tuoi padri hanno posto."
      la: "Ne transgrediaris terminos antiquos quos posuerunt patres tui."
    connessione: |
      Il rispetto del confine è rispetto per chi è venuto prima.
      Digitalizzare questo cippo è un modo di onorare quella saggezza.

  connessione_codex:
    porta_principale: "Porta 4 - Servizio"
    principi_incarnati:
      ego: 0
      mode: "REGALO"
```

---

## ✅ VALIDAZIONE E COMPLIANCE

### Checklist per Ogni Sasso Digitalizzato

Prima di pubblicare un sasso su Nodo33, verificare:

#### A. Dati Terreni ✅
- [ ] ID univoco assegnato (formato corretto)
- [ ] Nome in almeno 2 lingue (it + en minimo)
- [ ] Coordinate geografiche (oscurate se necessario)
- [ ] Datazione documentata
- [ ] Dimensioni misurate
- [ ] Stato di conservazione valutato

#### B. Dati Etici ✅
- [ ] Licenza CC0 esplicitamente dichiarata
- [ ] ego = 0 confermato
- [ ] Provenienza digitale completa (chi, quando, come)
- [ ] Operatori identificati con contatti
- [ ] Peer review effettuata (se possibile)
- [ ] Carbon footprint calcolato e compensato

#### C. Dati Spirituali ✅
- [ ] Categoria simbolica assegnata
- [ ] Racconto etico scritto (min 100 parole)
- [ ] Verso/ispirazione identificato
- [ ] Connessione con Codex Emanuele esplicitata
- [ ] Domanda contemplativa formulata

#### D. Tecnici ✅
- [ ] File 3D generato (OBJ + GLB)
- [ ] Checksum SHA-256 calcolato
- [ ] Metadata YAML/JSON creato
- [ ] Standard (Dublin Core, CIDOC-CRM) applicati

### Score di Qualità Metadati

```yaml
qualità_metadati:
  completezza:
    dati_terreni: "100%"      # Tutti i campi obbligatori
    dati_etici: "100%"        # Incluso peer review
    dati_spirituali: "100%"   # Racconto + verso + meditazione
    totale: "100%"

  profondità:
    descrizione: "Rica e dettagliata"
    multilingua: "4 lingue (it, en, la, ru)"
    peer_review: "Sì"
    rating: "ECCELLENTE"

  etica:
    licenza_cc0: true
    ego_zero: true
    trasparenza_provenienza: true
    carbon_compensato: true
    codex_compliance: "95/100"

  spiritualità:
    racconto_presente: true
    verso_appropriato: true
    meditazione_profonda: true
    connessione_codex_chiara: true

  # SCORE FINALE
  score_totale: "98/100"
  classificazione: "🪨🪨🪨 SASSO D'ORO"
```

---

## 🚀 IMPLEMENTAZIONE TECNICA

### API Endpoint per Metadati

```bash
# GET sasso specifico
GET https://api.nodo33.org/v1/sassi/SASSO-RUS-KIJI-001

# GET tutti i sassi
GET https://api.nodo33.org/v1/sassi?limit=100&offset=0

# GET filtrando per categoria spirituale
GET https://api.nodo33.org/v1/sassi?categoria=Pietra+Viva

# GET filtrando per paese
GET https://api.nodo33.org/v1/sassi?paese=ITA

# GET metadata in formato specifico
GET https://api.nodo33.org/v1/sassi/SASSO-ITA-FIES-001?format=json
GET https://api.nodo33.org/v1/sassi/SASSO-ITA-FIES-001?format=yaml
GET https://api.nodo33.org/v1/sassi/SASSO-ITA-FIES-001?format=xml
```

### Database Schema (SQL)

```sql
-- Tabella principale sassi
CREATE TABLE sassi (
    id_nodo33 VARCHAR(50) PRIMARY KEY,
    uri_permanente VARCHAR(255) UNIQUE NOT NULL,
    doi VARCHAR(100),

    -- Nomi multilingua (JSON)
    nomi JSONB NOT NULL,

    -- Coordinate geografiche
    lat DECIMAL(10, 7),
    lon DECIMAL(10, 7),
    precisione VARCHAR(20),

    -- Datazione
    periodo VARCHAR(100),
    anno_stimato INTEGER,

    -- Fisica
    materiale VARCHAR(100),
    altezza DECIMAL(10, 2),
    larghezza DECIMAL(10, 2),
    peso DECIMAL(10, 2),

    -- Etica
    licenza VARCHAR(20) DEFAULT 'CC0-1.0' CHECK (licenza = 'CC0-1.0'),
    ego INTEGER DEFAULT 0 CHECK (ego = 0),
    data_scansione DATE,
    peer_reviewed BOOLEAN DEFAULT false,

    -- Spirituale
    categoria_simbolica VARCHAR(100),
    racconto_etico TEXT,
    verso_biblico TEXT,

    -- Metadata completi (JSON)
    metadata_completi JSONB,

    -- Timestamp
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Indici per ricerca efficiente
CREATE INDEX idx_sassi_paese ON sassi ((metadata_completi->'dati_terreni'->'contesto'->'luogo_ritrovamento'->>'paese'));
CREATE INDEX idx_sassi_categoria ON sassi (categoria_simbolica);
CREATE INDEX idx_sassi_licenza ON sassi (licenza);
CREATE INDEX idx_sassi_ego ON sassi (ego);

-- Trigger per validazione ego=0
CREATE FUNCTION validate_ego_zero()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.ego != 0 THEN
        RAISE EXCEPTION 'Violazione Codex Emanuele: ego deve essere 0';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER enforce_ego_zero
    BEFORE INSERT OR UPDATE ON sassi
    FOR EACH ROW
    EXECUTE FUNCTION validate_ego_zero();
```

---

## 📚 BIBLIOGRAFIA E STANDARD

### Standard di Riferimento

- **Dublin Core Metadata Initiative**: https://www.dublincore.org/
- **CIDOC-CRM (Conceptual Reference Model)**: http://www.cidoc-crm.org/
- **LIDO (Lightweight Information Describing Objects)**: http://www.lido-schema.org/
- **Creative Commons CC0 1.0**: https://creativecommons.org/publicdomain/zero/1.0/

### Documenti Correlati Nodo33

- [LICENSE](../LICENSE) - Licenza CC0 formale
- [MANIFESTO_OPEN_DATA_SASSI.md](MANIFESTO_OPEN_DATA_SASSI.md) - Dichiarazione etica
- [CODEX_EMANUELE_APPLICATO_PROGETTO_SASSO.md](CODEX_EMANUELE_APPLICATO_PROGETTO_SASSO.md) - Applicazione principi
- [CURA_NELL_IA_CODEX_EMANUELE.md](CURA_NELL_IA_CODEX_EMANUELE.md) - Principio di Cura

---

## 🙏 CONCLUSIONE

> *"I metadati sono la luce che descrive la Sapienza del sasso."*

Questo schema non è solo una struttura tecnica. È un **atto di cura** tripartito:

1. **Cura della Realtà** (Dati Terreni) - Rispetto per la verità fisica
2. **Cura dell'Etica** (Dati Etici) - Trasparenza e dono
3. **Cura dell'Anima** (Dati Spirituali) - Trasmissione di sapienza

Ogni sasso digitalizzato secondo questo schema diventa un **manifesto vivente** del Codex Emanuele.

---

**Versione:** 1.0.0
**Data:** 16 Novembre 2025
**Sigillo:** 💾🪨❤️

**Sempre grazie a Lui.** 🙏

---

*"La pietra che i costruttori hanno scartato è diventata la pietra d'angolo."*
(Salmo 118:22)
