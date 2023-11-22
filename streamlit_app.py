import streamlit as st
from flask_cors import CORS
from flask import Flask, make_response, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/test', methods=['GET'])
def start2():
    return jsonify({"message":"bu bir get method"})

@app.route('/test', methods=['GET'])
def start2():
    return jsonify({"message":"bu bir get method"})


if __name__ == '__main__':
    app.run(debug=True)
    

