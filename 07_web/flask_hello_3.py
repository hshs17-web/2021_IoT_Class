from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    '''

@app.route("/led/on")
def first():
    return '''
        <p>LED ON!</p>
        <a href="/">Go Home</a>
    '''

@app.route("/second")
def second():
    return '''
        <p>Second Page</p>
        <a href="/">Go Home</a>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0")