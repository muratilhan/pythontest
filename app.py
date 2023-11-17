from flask_cors import CORS
from flask import Flask, make_response, jsonify

app = Flask(__name__)
CORS(app)


#asdasdasd 
#asdasdasd
<<<<<<< HEAD

@app.route('/deneme', methods=['GET'])
def start():
    #asdasdasd
    return "bu bir get meth"

=======
degisken = 5
print(degisken)
>>>>>>> 9e5a795 (variable added)
@app.route('/start', methods=['GET'])
def start():
    #asdasdasd
    return "bu bir get meth"

@app.route('/post', methods=['POST'])
def start2():
    return "bu bir post method"
    
if __name__ == '__main__':
    app.run(debug=True)
    
