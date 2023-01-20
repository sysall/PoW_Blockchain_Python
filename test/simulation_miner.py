from function.miner import MinerNodeNaive
from main import Block
import random as rand

#In this file I try to simulate a bunch of different miners with different compute powers. 
# However this isn't completely indicative of how a real system works.

#Initialize multiple miners on the network
ESMT_Miner = MinerNodeNaive("ESMT Miner", 10)
UCAD_Miner = MinerNodeNaive("UCAD Miner", 5)
ESP_Miner = MinerNodeNaive("ESP Miner", 2)
ISM_Miner = MinerNodeNaive("ISM Miner", 1)

miner_array = [ESMT_Miner, UCAD_Miner, ESP_Miner, ISM_Miner]

def create_compute_simulation(miner_array):
    compute_array = []
    for miner in miner_array:
        for i in range(miner.compute):
            compute_array.append(miner.name)
    return(compute_array)

compute_simulation_array = create_compute_simulation(miner_array)
rand.shuffle(compute_simulation_array)

chain_length = 20
blockchain_distributed = [Block.create_genesis_block()]
genesis_block_dist = blockchain_distributed[0]
chain_difficulty = [rand.randint(2,4) for i in range(chain_length)]

for i in range(len(chain_difficulty)):
    while len(blockchain_distributed) < i + 2:
        next_miner_str = rand.sample(compute_simulation_array, 1)[0]
        next_miner = ESMT_Miner #random default (go bears)
        for miner in miner_array:
            if next_miner_str == miner.name:
                next_miner = miner
        next_miner.try_hash(chain_difficulty[i], blockchain_distributed)



