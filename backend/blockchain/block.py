import time
import sys
sys.path.append('backend')
from util.crypto_hash import crypto_hash
#from backend.util.crypto_hash import crypto_hash


GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    Unit of storage for the Blockchain
      stores transactions and supports a cryptocurrency
    """
    def __init__ (self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
        
    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce}'

            )
     
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
     
    @staticmethod   
    def mine_block(last_block, data):
         # mines a block based on given last_block and data
         #   until a block hash is found that meets the difficulty
         #   of the number of leading zeroes proof of work requirement
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = last_block.difficulty
        nonce = 0
        #hash = f'{timestamp}-{last_hash}' #temporary for testing
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
        
        while hash[0:difficulty] != '0' * difficulty:
            nonce +=1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
            
        return Block(timestamp, last_hash, hash, data, difficulty, nonce)


    @staticmethod
    def genesis():
        # generate the first block
        return Block(**GENESIS_DATA)
    
    
    @staticmethod
    def is_valid_block(last_block, block):
        """
        Validate block by enforcing the following rules
        -block must have the proper last_hash reference
        -block must meet the proof of work requment (number of 0s)
        -block hash must be a valid combo of the block fields
        """
        if block.last_hash != last_block.hash:
            raise Exception('The block last_hash must be correct')
        
        if block.hash[0:block.difficulty] != '0' * block.difficulty:
            raise Exception('The proof of Work requirement was not met')
        
        if (abs(last_block.difficulty - block.difficulty) > 1):
            raise Exception('The block difficulty can only be changed by 1')
        
        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
        )
        
        if block.hash != reconstructed_hash:
            raise Exception('The block hash does not match, it is not correct')          

        
def main():
    #block = Block('test_foo')
    #print(block)
    #print(f'block.py __name__: {__name__}')
    
    #genesis_block = Block.genesis()
    #block = Block.mine_block(genesis_block, 'firstblock - genesis')
    #print(block)

    #test block validation
    genesis_block = Block.genesis()
    bad_block = Block.mine_block(Block.genesis(), 'foo')
    #comment the following line out to test a good block
    bad_block.last_hash = 'evil_data'
    try:
        Block.is_valid_block(genesis_block, bad_block)
    except Exception as e:
        print(f'is_valid_block: {e}')
    
if __name__ == '__main__':
    # only prints if called directly, not if called from blockchain.py
    main()
