from function import chain_function, proof_of_work as PoW

# Create the blockchain and add the genesis block
blockchain_pow = [chain_function.create_genesis_block()]

#Create our initial reference to previous block which points to the genesis block
previous_block = blockchain_pow[0]

# How many blocks should we add to the chain after genesis block
num_blocks = 20

#magnitude of difficulty of hash - number of zeroes that must be in the beginning of the hash
difficulty = 3

#length of nonce that will be generated and added
nonce_length = 20

# Add blocks to the chain based on difficulty with nonces of length nonce_length
def create_pow_blockchain(num_blocks, difficulty, blockchain_pow, previous_block, nonce_length, print_data=1):
    hash_array = []
    time_array = []
    for i in range(0, num_blocks):
        time_taken, hashes_tried, block_to_add = PoW.find_next_block(previous_block, difficulty, nonce_length)
        blockchain_pow.append(block_to_add)
        previous_block = block_to_add
        hash_array.append(hashes_tried)
        time_array.append(time_taken)
        # Tell everyone about it!
        if print_data:
            print("Block #{} has been added to the blockchain!".format(block_to_add.index))
            print("{} Hashes Tried!".format(hashes_tried))
            print("Time taken to find block: {}".format(time_taken))
            print("Hash: {}\n".format(block_to_add.hash))
    return(hash_array, time_array)


hash_array, time_array = create_pow_blockchain(num_blocks, difficulty, blockchain_pow, previous_block, nonce_length)
def test_proof_of_work(blockchain_pow, num_blocks):
    correct = True
    bound = PoW.generate_difficulty_bound(difficulty)
    if len(blockchain_pow) != num_blocks + 1:
        correct = False
    for i in range(len(blockchain_pow) - 1):
        if blockchain_pow[i + 1].previous_hash != blockchain_pow[i].hash:
            correct = False
            break
        if int(blockchain_pow[i + 1].hash, 16) > bound:
            correct = False
            break
    print_statement = "PASSED!!! Move on to the next Part" if correct else "FAILED!!! Try Again :("
    print(print_statement)


test_proof_of_work(blockchain_pow, num_blocks)