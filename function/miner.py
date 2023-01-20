from main import Block
import datetime as date
import proof_of_work as PoW


class MinerNodeNaive:
    def __init__(self, name, compute):
        self.name = name
        self.compute = compute

    def try_hash(self, diff_value, chain):
        last_block = chain[-1]
        difficulty = PoW.generate_difficulty_bound(diff_value)
        date_now = date.datetime.now()
        this_index = last_block.index + 1
        this_timestamp = date_now
        this_data = "Hey! I'm block " + str(this_index)
        this_hash = last_block.hash
        new_block = Block(this_index, this_timestamp, this_data, this_hash)
        if int(new_block.hash, 16) < difficulty:
            chain.append(new_block)
            print("Block #{} has been added to the blockchain!".format(new_block.index))
            print("Block found by: {}".format(self.name))
            print("Hash: {}\n".format(new_block.hash))

