# Build a Blockchain with Python
> In this project I create a blockchain from scratch using Object-Oriented Programming and Hash functions also implement Proof of Work Consensus and Mining Processes.
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)

## General info
This project is meant to be a short introduction to Blockchain implementations, 
It is split in 3 parts (functional, simulation and data analytics)
I implemented different aspects of Blockchain technology that we understand including:

- The Blockchain Data Structure using OOP
- A proof of work simulation
- Understanding of the concept of difficulty of finding the next block hash
- A simulation of multiple miners with varying computational powers
- A bit of data analytics to see if what we've implemented makes sense

	
## Technologies
Project is created with:
* Python
* hashlib

## Features
List the ready features here:
- In main.py I define the class "Block" and create an init function that creates a new block given some parameters as well as a function hash_block, that computes the hash of this block based on its class variables.
- In Miner.py I define the class "MinerNodeNaive" and create an init function that create a new miner as well as a function try_hash, that races with other miners to see who can get a certain number of blocks first
- In Chain_function.py I defined a create_genesis_block function that creates the first block of the chain, the genesis block, a next_block function that creates the next block, given the last block on the chain you want to mine on and a complete_chain function that is for spinning up a chain
- In Proof_of_work.py I defined a generate_nonce function that generates randomly a number for the nonce, a generate_difficulty_bound function that create and a find_next_block function that finds a nonce that results in a lower hash value, given a previous block and a difficulty metric,
- In Simulation_PoW.py 
- In Simulation_Miner.py
- Data_analytics.py
	
## Setup
Make sure you have `Python 3` installed.
If you are missing packages, please use `pip` to install them.
Run Simulation file to test the block creation, mining, and proof of work
