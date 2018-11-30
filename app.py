from flask import Flask

app = Flask(__name__)

@app.route("/api/v1/hello")
def print_hello():
    return "hello world"

if __name__== '__main__':
    app.run(debug=True)