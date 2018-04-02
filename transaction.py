"""A representation of the Transaction."""


class Transaction():
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.inputs = []
        self.outputs = []
        self.signatures = []

    def verify_transaction(self):
        pass

    def verify_sig(self):
        pass



