from flask import Flask;


app = Flask(__name__)


@app.route("/hello")
def  hello():
    with open("hello.txt", 'w') as hello:
        hello.write("hello world")      
    return "updated the file"

@app.route('/')
def home():
    with open("hello.txt", 'r') as hello:
        return hello.read()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)