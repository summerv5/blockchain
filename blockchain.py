import random
import string
from hashlib import sha256
from block import Block

""" A representation of the Block Chain. """

class BlockChain():
    def __init__(self):
        self.blocks = []
        self.difficulty = 4

    def new_block(self):
        pass

    def pow(self, hash_str):
        # A basic Proof of Work.

        sha = sha256()
        found_proof = False

        while found_proof == False:
            attempt = self.guess(hash_str)
            sha.update(attempt)

            if sha.hexdigest()[:self.difficulty] == "".zfill(self.difficulty):
                found_proof = True

        return attempt

    @staticmethod
    def guess(hash_str, size = 25):
        # Randomly generates guess hash.

        guess = ''.join(random.choice(string.ascii_lowercase +
                                      string.ascii_uppercase +
                                      string.digits) for x in range(size))

        attempt = hash_str + guess
        return attempt
