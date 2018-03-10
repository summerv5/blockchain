"""A representation of the Transaction."""


class Transaction():
    def __init__(self):
        self.sender = ""
        self.recipient = ""
        self.value = 0.0
        self.inputs = []
        self.outputs = []
        self.signatures = []

    def new_transaction(self):
        pass

    def verify_transaction(self):
        pass

    def verify_sig(self):
        pass

    

