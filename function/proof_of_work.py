import random as rand
import time
from main import Block
from function import chain_function

def generate_nonce(length=20):
    return ''.join([str(rand.randint(0, 9)) for i in range(length)])

def generate_difficulty_bound(difficulty=1):
    diff_str = ""
    for i in range(difficulty):
        diff_str += '0'
    for i in range(64 - difficulty):
        diff_str += 'F'
    diff_str = "0x" + diff_str
    return int(diff_str, 16)

# Given a previous block and a difficulty metric, finds a nonce that results in a lower hash value
def find_next_block(last_block, difficulty, nonce_length):
    difficulty_bound = generate_difficulty_bound(difficulty)
    start = time.process_time()
    new_block = chain_function.next_block(last_block)
    hashes_tried = 1
    while int(new_block.hash,16) > difficulty_bound:
        nonce = generate_nonce(nonce_length)
        new_block = Block(new_block.index, new_block.timestamp, new_block.data,new_block.previous_hash, nonce)
        hashes_tried += 1
    time_taken = time.process_time() - start
    return time_taken, hashes_tried, new_block
