from flask_cors import CORS
from flask import Flask, make_response, jsonify

app = Flask(__name__)
CORS(app)


#asdasdasd 
#asdasdasd
@app.route('/start', methods=['GET'])
def start():
    #asdasdasd
    return "bu bir get meth"

@app.route('/post', methods=['POST'])
def start2():
    return "bu bir post method"
    
if __name__ == '__main__':
    app.run(debug=True)
    
