from main import Block
from function import chain_function


def test_hashBlock(index, time, data, previous_hash):
    new_block = Block(index, time, data, previous_hash)
    check_string = '2def27922fc1c67254a9cdb0c660b91abf9b135ad38fc13c7c77007448b824a0'
    print_statement = "PASSED!!! Move on to next Question" if str(
        new_block.hash) == check_string else "FAILED!!! Try Again"
    print(print_statement)


time = '2019-10-17 00:37:35.256774'
data = 'Machine Learning Blockchain AI'
previous_hash = '6ffd1464f68ef4aeb385d399244efa19293ba5c842c464a82c02f8256ef71428'
index = 0

#test_hashBlock(index, time, data, previous_hash)


def test_nextBlock(genesis_block):
    block_1 = chain_function.next_block(genesis_block)
    if block_1.index == 1 and block_1.data == "Hey! I'm block1" and block_1.previous_hash == genesis_block.hash and str(
            type(block_1.timestamp)) == "<class 'datetime.datetime'>":
        print("PASSED!!! Move on to next part")
    else:
        print("FAILED!!! Try again :(")


#genesis_block = chain_function.create_genesis_block()
#test_nextBlock(genesis_block)


# Create the blockchain and add the genesis block
blockchain = [chain_function.create_genesis_block()]

# Create our initial reference to previous block which points to the genesis block
previous_block = blockchain[0]

# How many blocks should we add to the chain after the genesis block
num_blocks = 20


# This function takes in three inputs, which correspond to the initializations that we made.
# It returns nothing, however by the time we are done running it,
# the list 'blockchain' that we initialized earlier has been turned into an array of length num_blocks + 1

chain_function.complete_chain(num_blocks, blockchain, previous_block)

def test_completeChain(blockchain, num_blocks):
    correct = True
    if len(blockchain) != num_blocks + 1:
        correct = False
    for i in range(len(blockchain)-1):
        if blockchain[i + 1].previous_hash != blockchain[i].hash:
            correct = False
            break
    print_statement = "PASSED!!! Move on to the next Part" if correct else "FAILED!!! Try Again :("
    print(print_statement)

#test_completeChain(blockchain, num_blocks)




