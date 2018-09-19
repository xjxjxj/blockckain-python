import hashlib
import random
import time

class Block:
    def __init__(self,transactions,timestamp,data='',previous_hash='0',nounce=0):
        self.transactions=transactions
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=previous_hash
        self.nounce=nounce
        self.hash=self.cal_hash()

    def cal_hash(self):
        comb=str(self.timestamp)+str(self.data)+str(self.previous_hash)+str(self.nounce)
        for tran in self.transactions:
            comb+=str(tran)
        return hashlib.sha256(bytes(comb,'utf-8')).hexdigest()

    def POW(self,diff):
        start=0
        while [v for v in self.hash[start:diff]]!=['0' for v in range(start,diff)]:
            self.nounce+=1
            self.hash=self.cal_hash()
        print ("Successfully!")


class Transactions:
    def __init__(self,src_addr,dst_addr,amount):
        self.src_addr=src_addr
        self.dst_addr=dst_addr
        self.amount=amount

    def __str__(self):
        return str(self.src_addr)+"send"+str(self.amount)+"to"+str(self.dst_addr)


class BlockChain:
    def __init__(self):
        self.diff=3
        self.chain=[self.genesis_block()]
        self.pending_transactions=[]
        self.reward=1.2

    def genesis_block(self):
        first_transaction=Transactions("ssc","ssc",100)
        return Block([first_transaction],int(time.time()),'创世块')

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def transaction_record(self,tran):
        self.pending_transactions.append(tran)

    def mine(self,addr):
        new_block=Block(self.pending_transactions,int(time.time()),'ok')
        new_block.POW(self.diff)
        self.chain.append(new_block)
        self.pending_transactions=[Transactions('',addr,self.reward)]

    def add_block(self,block):
        block.previous_hash=self.get_latest_block().hash
        block.POW(self.diff)
        self.chain.append(block)
        
    def get_balance(self,my_addr):
        balance=0
        for block in self.chain:
            for tran in block.transactions:
                if tran.src_addr==my_addr:
                    balance-=tran.amount
                elif tran.dst_addr==my_addr:
                    balance+=tran.amount
        return balance

    def check_chain(self):
        for i in range(1,len(self.chain)):
            current_block=self.chain[i]
            previous_block=self.chain[i-1]
            if (current_block.previous_hash!=previous_block.hash) or (current_block.hash!=current_block.cal_hash):
                return False
        return True




if __name__=='__main__':
    """
    测试
    """
    print("ok")











