from datetime import datetime
from main import Block

# Function that creates the first block with current time and generic data
def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")

# function that creates the next block, given the last block on the chain you# want to mine on
def next_block(last_block, nonce=0):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = "Hey! I'm block" + str(this_index)
    this_previous_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_previous_hash)

# function that creates a complete blockchain based on the given numbers of block
def complete_chain(num_blocks, blockchain, previous_block):
    for i in range(0, num_blocks):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))
