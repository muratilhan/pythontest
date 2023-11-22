from flask import Flask

app = Flask(__name__)

@app.route('/' ,methods=['GET'])  # Kök dizin için bir endpoint
def home():
    return 'Ana Sayfa'

@app.route('/hello', methods=['GET'])  # /hello adresi için bir endpoint
def hello():
    return 'Merhaba, Dünya!'

if __name__ == '__main__':
    app.run(debug=True)  # Uygulamayı çalıştır
