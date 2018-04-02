from transaction import Transaction
from hashlib import sha256
import time

"""A representation of the block."""


class Block():
    def __init__(self, transactions, nonce, pre_hash = None):
        self.transactions = transactions
        self.merkle_root = self.gen_merkle_root()
        self.time_stamp = self.cur_milliseconds()
        self.nonce = nonce
        self.pre_hash = pre_hash

    def add_transaction(self, sender, recipient, val):
        """
        Adds a new transaction to current block
        :param sender: <str> Address of the sender.
        :param recipient: <str> Address of the recipient.
        :param val: <float> The value sent from sender to recipient.
        :return:
        """

        tran = Transaction(sender, recipient, val)
        self.transactions.append(tran)

    def hash(self):
        """
        Returns the hash of the block.
        :return: <str>
        """

        return sha256(f'{self.time_stamp}{self.nonce}{self.merkle_root}{self.pre_hash}'.encode()).hexdigest()

    def gen_merkle_root(self):
        """
        Generates the Merkle tree root from a list of transactions.
        Loops through the transactions and compute the hash of every two transactions.
        Duplicate the process until there is only one hash left, that is the merkle root.

        :param transactions: <list> A list of transactions.
        :return: <str> The Merkle root.
        """

        if len(self.transactions) < 1:
            return ""

        s = len(self.transactions)
        t = []

        for i in (self.transactions[x: x + 2] for x in range(0, s, 2)):
            if len(i) == 2:
                dh = self.dhash(i[0] + i[1])
            else:
                dh = self.dhash(i[0] + i[0])

            t.append(dh)

        if len(t) == 1:
            return t[0]
        else:
            return self.gen_merkle_root()

    @staticmethod
    def dhash(target):
        """
        Generates double hash that uses SHA-256. hash(hash(p))
        :param target: <str>
        :return: <str>
        """

        sha = sha256(target.encode())
        return sha256(sha.digest()).hexdigest()

    @staticmethod
    def cur_milliseconds():
        """
        Generates the milliseconds of the current datetime.
        :return: <int>
        """

        t = time.time()
        return int(round(t * 1000))






