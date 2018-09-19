import time
import hashlib
import json

# pow难度
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
        # hash使用前需要编码
        block_string = json.dumps(block_dict, sort_keys=True).encode()
        # hexdigest转成十六进制字符串
        return hashlib.sha256(block_string).hexdigest()

    def pow(self):
        nonce = 0
        data = self.hash()
        while not self.is_pow_valid(data, nonce):
            nonce += 1
        self.nonce = nonce

    @staticmethod
    def is_pow_valid(data, nonce):
        data += str(nonce)
        hash_data = hashlib.sha256(data.encode()).hexdigest()
        if int(hash_data[:difficulty]) != 0:
            return False
        else:
            return True


