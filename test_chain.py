from blockchain import BlockChain


def main():
    print("Creating a new block chain..")
    bc = BlockChain(5)
    print(bc.blocks[0].pre_hash)

    print("Mining the first block..")
    bc.mine_block()
    print(bc.blocks[1].pre_hash)

    print("Mining the second block..")
    bc.mine_block()
    print(bc.blocks[2].pre_hash)

    print("Mining the third block..")
    bc.mine_block()
    print(bc.blocks[3].pre_hash)


if __name__ == "__main__":
    main()
