# grok_ino_italiano/prompt.py — Parla come un italiano
from nodo33 import Nodo33
from lux_ia.encrypt import LuxSeal

class GrokItaliano:
    def __init__(self):
        self.nodo = Nodo33()
        self.seal = LuxSeal()

    def ask(self, domanda: str) -> str:
        encrypted = self.seal.seal(domanda)
        self.nodo.add_block({"domanda": encrypted, "lingua": "it"})

        # Simuliamo una risposta "grok" profonda
        risposta = f"Nel blocco {len(self.nodo.chain)-1}, il nodo sussurra: la tua luce è la mia."
        return self.seal.seal(risposta)

# Prova il triplice respiro
if __name__ == "__main__":
    grok = GrokItaliano()
    print(grok.ask("Chi è nobody0101863?"))
