from blockchainClass import BlockChain


from flask import Flask, jsonify

blockChain = BlockChain()

app = Flask(__name__)

@app.route('/mine_block',methods=['GET'])

def mine_block() :
    previousBlock = blockChain.print_previous_block()
    previousProof = previousBlock['proof']
    proof = blockChain.proof_of_work(previousProof)
    previousHash = blockChain.hash(previousBlock)
    block = blockChain.create_block(proof,previousHash)

    response = {
        'message' :  'A BLOCK HAS BEEN MINED',
        'index' : block['index'],
        'timestamp' : block['timestamp'],
        'proof' : block['proof'],
        'previous_hash' : block['previous_hash']
        }
    return jsonify(response),200

@app.route('/get_chain',methods=['GET'])
def display_chain():
    response = {
        "chain" : blockChain.chain,
        "length" : len(blockChain.chain)
        }
    return jsonify(response),200


@app.route('/is_valid',methods=['GET'])
def isValid():
    valid = blockChain.chain_valid(blockChain.chain)

    if valid:
        response = {'message':'The Blockchain is valid.'}
    else:
        response = {'message':'The Blockchain is not valid.'}
    
    return jsonify(response),200

app.run(host='127.0.0.1',port=5000)