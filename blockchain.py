from block import Block
import requests


class BlockChain(object):

    def __init__(self):
        self.chains = []
        self.current_transactions = []
        self.nodes = set()

    def new_block(self, nonce):
        prehash = self.get_last_block().hash()
        b = Block(len(self.chains) + 1, prehash, self.current_transactions, nonce)
        self.current_transactions = []
        self.chains.append(b)

    def add_node(self, node):
        self.nodes.add(node)

    def new_transaction(self, source, dest, amount):
        self.current_transactions.append({
            'source': source,
            'dest': dest,
            'amount': amount
        })
        return self.get_last_block().index + 1

    def get_last_block(self):
        return self.chains[-1]

    def is_chain_valid(self):
        for i in range(1, len(self.chains)):
            if self.chains[i].pre_hash != self.chains[i - 1].hash():
                self.resolve_fork()
                return False
            if self.chains[i].is_pow_valid(self.chains[i].hash(), self.chains[i].nonce):
                self.resolve_fork()
                return False

        return True

    def resolve_fork(self):
        new_chain = []
        for node in self.nodes:
            response=requests.get(node)
        self.chains = new_chain


def mine(bc, address):
    index = bc.new_transaction(
        source='0',
        dest=address,
        amount=1
    )

    block = Block(
        index=index,
        prehash=bc.get_last_block().hash(),
        transactions=bc.current_transactions,
        nonce=0,
    )
    # 工作量证明
    block.pow()
    # 上链
    bc.new_block(block.nonce)
