import hashlib as hasher

class Block:

    # A function that creates a new block given some parameters
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    # A function that computes the hash of this block based on its class variables.
    def hash_block(self):
        sha = hasher.sha256()
        block_hash = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce))
        block_hash = block_hash.encode('utf-8')
        sha.update(block_hash)
        return sha.hexdigest()

