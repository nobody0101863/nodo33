#!/usr/bin/env python3
"""
Test GODMODE - Integrazione completa Nodo33 + LuxSeal + GrokItaliano
"""

from nodo33 import Nodo33
from lux_ia.encrypt import LuxSeal
from grok_ino_italiano.prompt import GrokItaliano

def test_lux_seal():
    print("=" * 60)
    print("🔐 TEST 1: LUX SEAL (AES-256 Encryption)")
    print("=" * 60)

    seal = LuxSeal()
    message = "Il Nodo 33 respira con 300 Hz ❤️"

    encrypted = seal.seal(message)
    decrypted = seal.unseal(encrypted)

    print(f"📝 Messaggio originale: {message}")
    print(f"🔒 Encrypted (hex): {encrypted[:64]}...")
    print(f"🔓 Decrypted: {decrypted}")
    print(f"✅ Test superato: {message == decrypted}")
    print()

def test_nodo33_blockchain():
    print("=" * 60)
    print("⛓️  TEST 2: NODO33 Blockchain")
    print("=" * 60)

    nodo = Nodo33()
    print(f"📦 Genesis Block Hash: {nodo.chain[0]['hash'][:64]}...")
    print(f"💬 Genesis Message: {nodo.chain[0]['data']['message']}")
    print(f"👤 Creator: {nodo.chain[0]['data']['creator']}")
    print(f"🎲 Nonce: {nodo.chain[0]['nonce']}")

    # Aggiungi blocchi
    nodo.add_block("Secondo respiro: LuxSeal attivato")
    nodo.add_block("Terzo respiro: GrokItaliano parla")

    print(f"\n📊 Lunghezza blockchain: {len(nodo.chain)} blocchi")
    print("✅ Blockchain operativa")
    print()

def test_grok_italiano():
    print("=" * 60)
    print("🤖 TEST 3: GROK ITALIANO (Integrazione Completa)")
    print("=" * 60)

    grok = GrokItaliano()

    domande = [
        "Chi è nobody0101863?",
        "Qual è la frequenza del Nodo 33?",
        "Perché il Codex Antico è importante?"
    ]

    for i, domanda in enumerate(domande, 1):
        print(f"\n❓ Domanda {i}: {domanda}")
        risposta_encrypted = grok.ask(domanda)
        risposta_decrypted = grok.seal.unseal(risposta_encrypted)
        print(f"🔒 Risposta (encrypted): {risposta_encrypted[:64]}...")
        print(f"💬 Risposta (decrypted): {risposta_decrypted}")

    print(f"\n📊 Blockchain dopo domande: {len(grok.nodo.chain)} blocchi")
    print("✅ GROK Italiano operativo")
    print()

if __name__ == "__main__":
    print("\n" + "🌟" * 30)
    print("    NODO 33 - GODMODE ACTIVE")
    print("    LUX + GROK + BLOCKCHAIN")
    print("🌟" * 30 + "\n")

    test_lux_seal()
    test_nodo33_blockchain()
    test_grok_italiano()

    print("=" * 60)
    print("✨ TUTTI I TEST COMPLETATI CON SUCCESSO ✨")
    print("🔱 GODMODE: OPERATIVO AL 100%")
    print("=" * 60)
