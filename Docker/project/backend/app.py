from flask import Flask,jsonify,Request;
from data import get_names

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/api',methods=['GET'])
def api():
    data = get_names()
    res = {'data':data}
    return jsonify(res)

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0', debug=True)