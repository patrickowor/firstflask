From flask import Flask 
app = Flask(__name__)

@app.route('/<str: name>')
def main(name):
    return 'hello'+ name

if __name__ == '__main__':
    app.run(debug = true) 
