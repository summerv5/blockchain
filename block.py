from transaction import Transaction
from hashlib import sha256
from datetime import datetime

"""A representation of the block."""


class Block():
    def __int__(self, pre_hash, merkle_root, transactions, time_stamp, nonce):
        self.pre_hash = pre_hash
        self.merkle_root = merkle_root
        self.transactions = transactions
        self.time_stamp = time_stamp
        self.nonce = nonce

    def new_block(self):
        pass

    def add_transaction(self, trans):
        # Adds a new transaction to current block

        if trans is None:
            raise ValueError("Transaction cannot be none!")

        self.transactions.append(trans)

    def hash(self):
        # Returns the hash of the block.
        return sha256(self.pre_hash +
                      str(self.time_stamp) +
                      str(self.nonce) +
                      self.merkle_root).hexdigest()


def get_mroot(transactions):
    # Generates the Merkle tree root from a list of transactions.

    s = len(transactions)
    t = []

    for i in (transactions[x: x + 2] for x in range(0, s, 2)):
        if len(i) == 2:
            dh = dhash(i[0] + i[1])
        else:
            dh = dhash(i[0] + i[0])

        t.append(dh)

    if len(t) == 1:
        return t[0]
    else:
        return get_mroot(t)


def dhash(str):
    # A double hash method that uses SHA-256.

    sha = sha256(str.encode())
    return sha256(sha.digest()).hexdigest()






