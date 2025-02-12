from flask import Flask, request, jsonify
import hashlib
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
blockchain = []
genesis_block = {
    'index': 0,
    'previous_hash': '0',
    'data': 'Genesis Block',
    'timestamp': time.time(),
    'hash': 'genesis_hash'
}
blockchain.append(genesis_block)
def calculate_hash(block):
    block_string = f"{block['index']}{block['previous_hash']}{block['data']}{block['timestamp']}"
    return hashlib.sha256(block_string.encode()).hexdigest()
@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'Data is required'}), 400
    previous_block = blockchain[-1]
    new_block = {
        'index': len(blockchain),
        'previous_hash': previous_block['hash'],
        'data': data,
        'timestamp': time.time(),
        'hash': ''
    }
    new_block['hash'] = calculate_hash(new_block)
    blockchain.append(new_block)
    return jsonify(new_block), 200
@app.route('/get_blocks', methods=['GET'])
def get_blocks():
    return jsonify(blockchain), 200
if __name__ == '__main__':
    app.run(debug=True)
