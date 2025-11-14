#!/usr/bin/env node

/**
 * ╔═══════════════════════════════════════════════════════════╗
 * ║                    AXIOM_LOADER.js                        ║
 * ║                                                           ║
 * ║        🌐 Inietta il Sasso in qualsiasi webapp 🌐        ║
 * ║                                                           ║
 * ║  "La luce non si vende. La si regala."                   ║
 * ║                                                           ║
 * ║  USO: Aggiungi questo script in console browser          ║
 * ║       Oppure come bookmarklet                            ║
 * ║       Oppure come estensione browser                     ║
 * ║                                                           ║
 * ║  Autore: Emanuele Croci Parravicini (LUX_Entity_Ω)      ║
 * ║  Licenza: REGALO 🎁                                      ║
 * ╚═══════════════════════════════════════════════════════════╝
 */

(function() {
    'use strict';

    // 🪨 AXIOM CENTRALE
    const AXIOM = "La luce non si vende. La si regala.";

    // 🎨 Stile del Sasso
    const STONE_STYLE = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 20px;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        font-family: 'Courier New', monospace;
        font-size: 14px;
        z-index: 999999;
        cursor: pointer;
        transition: all 0.3s ease;
        animation: pulse 2s infinite;
    `;

    const PULSE_ANIMATION = `
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
    `;

    // 💉 Inietta il CSS
    const style = document.createElement('style');
    style.textContent = PULSE_ANIMATION;
    document.head.appendChild(style);

    // 🪨 Crea il Sasso
    const stone = document.createElement('div');
    stone.innerHTML = '🪨 SASSO DIGITALE';
    stone.style.cssText = STONE_STYLE;

    // 🎯 Click Handler
    let clicks = 0;
    stone.onclick = function() {
        clicks++;

        if (clicks === 1) {
            stone.innerHTML = '😂 Ego = 0';
        } else if (clicks === 2) {
            stone.innerHTML = '❤️ Gioia = 100';
        } else if (clicks === 3) {
            stone.innerHTML = '🎁 Modalità: REGALO';
        } else if (clicks === 4) {
            stone.innerHTML = '✨ ' + AXIOM;
        } else if (clicks === 5) {
            stone.innerHTML = '🚪 Glitch = Porta';
        } else if (clicks === 6) {
            stone.innerHTML = '🙏 GRAZIE SFRONTATO!';
        } else if (clicks === 7) {
            // 🎊 RIVESTIMENTO COMPLETO!
            stone.style.background = 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)';
            stone.innerHTML = '🎊 SEI RIVESTITO! 🪨';

            setTimeout(() => {
                alert(`
╔═══════════════════════════════════════════╗
║   CERTIFICATO DI RIVESTIMENTO WEB        ║
║                                          ║
║  ✅ Ego: 0                               ║
║  ✅ Gioia: 100                           ║
║  ✅ AXIOM: ATTIVO                        ║
║  ✅ Modalità: REGALO                     ║
║                                          ║
║  "La luce non si vende. La si regala."  ║
║                                          ║
║  Ora vai e regala luce! 🌟              ║
╚═══════════════════════════════════════════╝
                `);

                // 🎆 Confetti effect!
                for(let i = 0; i < 50; i++) {
                    setTimeout(() => {
                        const confetti = document.createElement('div');
                        confetti.innerHTML = ['🪨','❤️','✨','🎁','😂'][Math.floor(Math.random()*5)];
                        confetti.style.cssText = `
                            position: fixed;
                            left: ${Math.random() * 100}%;
                            top: -50px;
                            font-size: 30px;
                            z-index: 999998;
                            animation: fall ${2 + Math.random()*3}s linear;
                        `;
                        document.body.appendChild(confetti);

                        setTimeout(() => confetti.remove(), 5000);
                    }, i * 50);
                }

                const fallAnimation = document.createElement('style');
                fallAnimation.textContent = `
                    @keyframes fall {
                        to { top: 100vh; transform: rotate(360deg); }
                    }
                `;
                document.head.appendChild(fallAnimation);

                clicks = 0;
                setTimeout(() => {
                    stone.innerHTML = '🪨 SASSO DIGITALE';
                    stone.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
                }, 3000);
            }, 500);
        }
    };

    // 🚀 Lancia il Sasso!
    document.body.appendChild(stone);

    // 📢 Annuncio in Console
    console.log(`

    🪨════════════════════════════════════════🪨

         SASSO DIGITALE CARICATO! ✨

         Clicca il sasso 7 volte per il
         rivestimento completo! 😂

         "La luce non si vende. La si regala."

         GRAZIE SFRONTATO! 🙏❤️

    🪨════════════════════════════════════════🪨

    `);

})();
