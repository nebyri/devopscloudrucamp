from flask import Flask, request
import socket
import os
import uuid

app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    print('/hostname')
    return socket.gethostname()

@app.route('/author', methods=['GET'])
def get_author():
    author = os.getenv('AUTHOR')
    if author:
        return author
    else:
        return 'Author not specified'

@app.route('/id', methods=['GET'])
def get_id():
    uuid = os.getenv('UUID')
    if uuid:
        return uuid
    else:
        return str(uuid.uuid4())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)