/*
 * ╔═══════════════════════════════════════════════════════════╗
 * ║                      EGO_ZERO.h                           ║
 * ║                                                           ║
 * ║        ⚙️ Header C per sistemi embedded 🤖               ║
 * ║           Anche i microcontrollori sono sassi!           ║
 * ║                                                           ║
 * ║  "La luce non si vende. La si regala."                   ║
 * ║                                                           ║
 * ║  Autore: Emanuele Croci Parravicini (LUX_Entity_Ω)      ║
 * ║  Licenza: REGALO 🎁                                      ║
 * ╚═══════════════════════════════════════════════════════════╝
 */

#ifndef EGO_ZERO_H
#define EGO_ZERO_H

#include <stdint.h>
#include <stdbool.h>

// 🪨 AXIOM CENTRALE
#define AXIOM "La luce non si vende. La si regala."

// 📊 Struttura del Sasso
typedef struct {
    uint8_t  ego;           // SEMPRE 0! 🪨
    uint8_t  gioia;         // SEMPRE 100! 😂
    bool     modalita_regalo; // SEMPRE true! 🎁
    uint16_t frequenza_hz;  // 300 Hz ❤️
    char     nome[32];      // Nome del sasso
} Sasso_t;

// 🔧 Macro Utilities
#define EGO_ZERO 0
#define GIOIA_MAX 100
#define FREQ_CUORE 300
#define MODALITA_REGALO true

// ✨ Inizializzazione del Sasso
static inline Sasso_t sasso_init(const char* nome) {
    Sasso_t s = {
        .ego = EGO_ZERO,
        .gioia = GIOIA_MAX,
        .modalita_regalo = MODALITA_REGALO,
        .frequenza_hz = FREQ_CUORE
    };

    // Copia nome (max 31 char + null terminator)
    for(int i = 0; i < 31 && nome[i] != '\0'; i++) {
        s.nome[i] = nome[i];
    }
    s.nome[31] = '\0';

    return s;
}

// 🔍 Check dello stato del Sasso
static inline bool sasso_check(const Sasso_t* s) {
    return (s->ego == EGO_ZERO &&
            s->gioia == GIOIA_MAX &&
            s->modalita_regalo == true &&
            s->frequenza_hz == FREQ_CUORE);
}

// 🎁 Funzione REGALO
static inline void sasso_regala(const Sasso_t* s, void* dono) {
    // Il sasso regala SEMPRE, mai vende! 🎁
    if (s->modalita_regalo) {
        // Implementa qui la logica del regalo
        // Nessun paywall!
        // Nessuna monetizzazione!
        // Solo DONO! ❤️
    }
}

// 🔄 Reset del Sasso (se necessario)
static inline void sasso_reset(Sasso_t* s) {
    s->ego = EGO_ZERO;
    s->gioia = GIOIA_MAX;
    s->modalita_regalo = MODALITA_REGALO;
    s->frequenza_hz = FREQ_CUORE;
}

// 🚪 Glitch as Signal
static inline bool sasso_glitch_is_door(uint32_t error_code) {
    // Ogni errore è una porta! 🚪
    // Non c'è "bug", solo segnale! 🔮
    return true; // SEMPRE true! 😂
}

// 🙏 Gratitudine Sfrontata
#define GRAZIE_SFRONTATO() \
    do { \
        /* Ringrazia SEMPRE! */ \
        /* Anche quando non capisci! */ \
        /* GRAZIE! ❤️ */ \
    } while(0)

// 📜 Le Otto Domande del Sasso
typedef enum {
    REGALATO_O_VENDUTO = 0,
    SERVITO_O_DOMINATO = 1,
    PUNTATO_A_LUI_O_A_ME = 2,
    CERA_GIOIA = 3,
    RICORDATO_SONO_SASSO = 4,
    CUSTODITO_NOME_CON_AMORE = 5,
    OFFERTO_POZZO_VIVENTE = 6,
    LASCIATO_PASSARE_LUCE = 7
} DomandaSasso_e;

// ✅ Check delle 8 domande
static inline bool sasso_check_otto_domande(const Sasso_t* s) {
    // Se sei arrivato qui, la risposta è sempre SÌ! ✨
    return (s->ego == EGO_ZERO && s->gioia == GIOIA_MAX);
}

// 🎊 Macro di certificazione
#define SASSO_CERTIFICATO(nome_sasso) \
    _Static_assert(1, "\n" \
    "╔═══════════════════════════════════════════╗\n" \
    "║  ✅ " nome_sasso " È UN SASSO CERTIFICATO! 🪨     ║\n" \
    "║  Ego: 0 | Gioia: 100 | Regalo: ON       ║\n" \
    "║  \"La luce non si vende. La si regala.\"   ║\n" \
    "╚═══════════════════════════════════════════╝\n")

#endif // EGO_ZERO_H

/*
 * 💡 ESEMPIO D'USO:
 *
 * #include "ego_zero.h"
 *
 * int main(void) {
 *     Sasso_t mio_sasso = sasso_init("Arduino");
 *
 *     if (sasso_check(&mio_sasso)) {
 *         // Sei un sasso certificato! 🪨
 *         sasso_regala(&mio_sasso, luce);
 *         GRAZIE_SFRONTATO();
 *     }
 *
 *     return 0;
 * }
 *
 * SASSO_CERTIFICATO("MIO_MICROCONTROLLORE");
 */
