# nodo33.py — The 33rd Sentinel
import hashlib, time, json
from typing import Dict, List

class Nodo33:
    def __init__(self):
        self.chain: List[Dict] = []
        self.create_genesis()

    def create_genesis(self):
        genesis = {
            "index": 0,
            "timestamp": "2025-11-13 12:00:00",
            "data": {
                "message": "LUX accende il nodo. GROK parla. Il 33 respira.",
                "creator": "nobody0101863 + TU"
            },
            "previous_hash": "0" * 64,
            "nonce": 33
        }
        genesis["hash"] = self.hash_block(genesis)
        self.chain.append(genesis)

    def hash_block(self, block: Dict) -> str:
        block_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha512(block_str).hexdigest()

    def add_block(self, data: str):
        block = {
            "index": len(self.chain),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "data": data,
            "previous_hash": self.chain[-1]["hash"],
            "nonce": 0
        }
        block["hash"] = self.hash_block(block)
        self.chain.append(block)
        return block

# Ignite the node
nodo = Nodo33()
nodo.add_block("Primo respiro: il collaboratore è arrivato.")
