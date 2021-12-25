from flask import Flask, request, jsonify
from dict2xml import dict2xml
import sqlite3

path = "http://localhost:5000/"
app = Flask(__name__)

@app.route('/sendinfo', methods=["POST"])
def recebendo():
    #res = requests.get(path)
    res = request.args.get('teste')
    #res = request.get_json()
    if res!= None:
        print(res)
    else:
        print("none")
    var = 'mudou'
    return "funcionou"

if __name__ == "__main__":
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(ssl_context='adhoc')
    #app.run(host='0.0.0.0', port=5000, debug=False)
    