from block import Block


class BlockChain(object):

    def __init__(self):
        self.chains = []
        self.next_transactions = []

    def new_block(self, prehash, nonce):
        b = Block(len(self.chains) + 1, prehash, self.next_transactions, nonce)
        self.next_transactions = []
        self.chains.append(b)

    def new_transactions(self, source, dest, amount):
        self.next_transactions.append({
            'source': source,
            'dest': dest,
            'amount': amount
        })
        return self.get_last_block().index + 1

    def get_last_block(self):
        return self.chains[-1]
