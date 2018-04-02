from hashlib import sha256
from block import Block

""" A representation of the Block Chain. """


class BlockChain():
    def __init__(self, difficulty):
        self.blocks = []
        self.difficulty = difficulty

        # Creates the genesis block
        self.new_block(pow = 100)

    def new_block(self, pow, pre_hash = None):
        """
        Creates a new Block in the chain.
        :param pow: <int>
        :param pre_hash: <str>
        :return:
        """

        block = Block(transactions = [], nonce = pow, pre_hash = pre_hash)
        self.blocks.append(block)

    def mine_block(self):
        """
        Find a block that uses the proof of work algorithm.
        :return: <Block> The new block.
        """

        last_block = self.blocks[-1]
        last_proof = last_block.nonce
        pre_hash = last_block.hash()

        proof = self.pow(last_proof)
        return self.new_block(proof, pre_hash)

    def pow(self, last_proof):
        """
        A basic Proof of Work algorithm.
        Find a proof p' so that hash(pp') contains leading zeros, where p is previous work.
        The numbers of leading zeros is defined as difficulty.

        :param last_proof: <int>
        :return: <int>
        """

        sha = sha256()
        found_proof = False
        work = -1

        while found_proof is False:
            work += 1
            sha.update(f'{last_proof}{work}'.encode())

            if sha.hexdigest()[:self.difficulty] == "".zfill(self.difficulty):
                found_proof = True

        return work

    def is_valid_chain(self):
        """
        Verify the validation of the block chain with a simple method:
        The hash of previous block on current block header must be the same of the computation of previous block.

        :return: <bool>
        """

        pass

