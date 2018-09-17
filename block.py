import time
import hashlib
import json

difficulty = 10

class Block(object):
    def __init__(self, index, prehash, transactions, nonce):
        self.id = index
        self.time_stamp = int(time.time())
        self.pre_hash = prehash
        self.transactions = transactions
        self.nonce = nonce

    def hash(self):
        block_dict = {
            'index': self.id,
            'timestamp': self.time_stamp,
            'prehash': self.pre_hash,
            'transactions': self.transactions,
            'nonce': self.nonce
        }
        block_string = json.dumps(block_dict, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def pow(self):
        
